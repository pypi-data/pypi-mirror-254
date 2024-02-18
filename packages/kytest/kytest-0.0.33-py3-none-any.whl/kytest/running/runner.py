import inspect
import os
import re
import shutil
import subprocess
import pytest
import json

from typing import Union, Literal
from kytest.utils.allure_util import AllureData
from kytest.running.conf import App
from kytest.utils.log import logger
from kytest.utils.config import config
from multiprocessing import Process


def _get_case_list(path: str):
    # 获取所有用例文件的完整路径列表
    _total_file_list = []
    for root, dirs, files in os.walk(path):
        if 'pycache' in root:
            continue
        files_str = ''.join(files)
        if '.py' not in files_str:
            continue
        files = [item for item in files if item != '__init__.py']
        if files:
            for _file in files:
                _total_file_list.append(os.path.join(root, _file))

    # 获取path目录下的用例原始字符串
    cases_str = subprocess.run(['pytest', path, '--collect-only'], capture_output=True, text=True).stdout

    # 把所有的标签拿出来
    lines = cases_str.split("\n")
    result = []

    for line in lines:
        match = re.search(r"<(.*?)>", line)
        if match:
            item = match.group(1)
            result.append(item)

    # 解析成用例列表
    case_list = []
    current_package = ''
    current_module = ''
    current_class = ''
    for item in result:
        if 'Package' in item:
            current_package = item.split(" ")[1]
        if 'Module' in item:
            current_module = item.split(" ")[1]
        if 'Class' in item:
            current_class = item.split(" ")[1]
        if 'Function' in item:
            _function = item.split(" ")[1].split("[")[0]
            _file_path = f"{current_package}/{current_module}"
            for item in _total_file_list:
                if _file_path in item:
                    _file_path = item
                    break
            print(f"{_file_path}::{current_class}::{_function}")
            case_list.append(f"{_file_path}::{current_class}::{_function}")

    # 去重
    print("去重后：")
    case_list = sorted(list(set(case_list)))
    for case in case_list:
        print(case)

    return case_list


def _move_file(source_dir, target_dir):
    # 获取源目录中的所有文件名列表
    file_list = os.listdir(source_dir)

    for file in file_list:
        # 构建源文件的完整路径
        source_file = os.path.join(source_dir, file)

        if not os.path.isdir(source_file):  # 判断是否为文件而非子目录
            # 构建目标文件的完整路径
            target_file = os.path.join(target_dir, file)

            try:
                # 移动文件至目标目录
                shutil.move(source_file, target_file)

                print('已移动文件：', file)
            except Exception as e:
                print('移动文件时发生错误：', str(e))


def _change_name_and_historyId(device_id, report_path):
    _allure = AllureData(result_path=report_path)
    result_list = _allure.get_files()
    for result in result_list:
        content = _allure.get_file_content(result)
        # 获取name，给name带上-{serial}的后缀
        content["name"] = content["name"] + "-" + device_id
        # 获取historyId，在后面带上-{serial}的后缀
        content["historyId"] = content["historyId"] + "-" + device_id
        # content重新写入回result中
        with open(result, "w") as f:
            f.write(json.dumps(content))


def _app_main(path, serial, package, udid, bundle_id, ocr_api, start, is_all=False):
    # 修改配置
    App.serial = serial
    App.package = package
    App.udid = udid
    App.bundle_id = bundle_id
    App.ocr_service = ocr_api
    App.auto_start = start

    # 执行用例
    # 由于是多设备并发执行，所以要对报告目录进行区分，后面增加合并的能力(有空调研一下pytest-xdist的报告合并实现方式)
    report_path = "report"
    if is_all is True:
        if serial:
            report_path = f"report-{serial}"
            cmd_list = [path, '-sv', '--alluredir', report_path]
            logger.info(cmd_list)
            pytest.main(cmd_list)
            # 进行合并，修改result.json中的name和historyId
            _change_name_and_historyId(serial, report_path)

            # 把目录中的文件都移入report目录中
            if not os.path.exists('report'):
                os.makedirs('report')
            _move_file(report_path, 'report')

            # 删除原目录
            shutil.rmtree(report_path, ignore_errors=True)
        if udid:
            report_path = f"report-{udid}"
            cmd_list = [path, '-sv', '--alluredir', report_path]
            logger.info(cmd_list)
            pytest.main(cmd_list)
            # 进行合并
            _change_name_and_historyId(udid, report_path)

            # 把目录中的文件都移入report目录中
            if not os.path.exists('report'):
                os.makedirs('report')
            _move_file(report_path, 'report')

            # 删除原目录
            shutil.rmtree(report_path, ignore_errors=True)
    else:
        cmd_list = [path, '-sv', '--alluredir', report_path]
        logger.info(cmd_list)
        pytest.main(cmd_list)


class TestMain(object):
    """
    Support for app、web、http
    """

    def __init__(
            self,
            path: str = None,
            api_host: str = None,
            headers: dict = None,
            package: str = None,
            serial: Union[str, list] = None,
            bundle_id: str = None,
            udid: Union[str, list] = None,
            ocr_api: str = None,
            start: bool = True,
            strategy: Union[
                Literal['full_serial', 'full_parallel', 'split_serial', 'split_parallel']] = 'full_serial',
            web_host: str = None,
            cookies: list = None,
            state: str = None,
            browser: str = None,
            headless: bool = False,
            maximized: bool = False,
            window_size: list = None,
            rerun: int = 0,
            xdist: bool = False
    ):
        """
        @param path: 用例路径
        @param api_host: 域名，用于接口测试和web测试
        @param headers: 请求头，用于接口测试和web测试
        @param package: 安卓包名，通过adb shell pm list packages | grep 'xxx'获取
        @param serial：安卓设备序列号，通过adb devices获取
        @param bundle_id：IOS应用包名，通过tidevice applist | grep 'xxx'获取
        @param udid：IOS设备uuid，通过tidevice list获取
        @param ocr_api: ocr识别服务api，用于安卓和ios测试
        @param start: 是否自动启动应用，用于安卓和ios测试
        @param strategy: 多设备执行模式
                - full_serial：每个设备都执行全部用例，串行执行
                - full_parallel：每个设备都执行全部用例，并发执行
                - split_serial：每个设备执行部分用例，串行执行
                - split_parallel：每个设备执行部分用例，并发执行
        @param web_host: 域名，用于接口测试和web测试
        @param cookies: 用于带上登录态，例如：
        [
            {
              "name": "token",
              "value": "xxx",
              "domain": ".qizhidao.com",
              "path": "/"
            }
        ]--- domain和path都不能为空
        @param state: 用户带上登录态，其实就是把cookies存到一个文件中
        @param browser: 浏览器类型，支持chrome、webkit、firefox
        @param headless: 是否开启无头模式，默认不开启
        @param maximized: 浏览器是否全屏
        @param window_size: 屏幕分辨率，[1920, 1080]
        @param rerun: 失败重试次数
        @param xdist: 是否并发执行，应该是多进程
        """
        # 公共参数保存
        common_data = {
            "base_url": api_host,
            "web_base_url": web_host,
            "headers": headers,
            "ocr_service": ocr_api
        }
        config.set_common_dict(common_data)
        # web参数保存
        web_data = {
            "cookies": cookies,
            "state_file": state,
            "browser_name": browser,
            "headless": headless,
            "maximized": maximized,
            "window_size": window_size
        }
        config.set_web_dict(web_data)
        # app参数保存
        App.serial = serial
        App.package = package
        App.udid = udid
        App.bundle_id = bundle_id
        App.ocr_service = ocr_api
        App.auto_start = start

        def _serial_execute(_path):
            # 执行用例
            cmd_list = [
                '-sv',
                '--reruns', str(rerun),
                '--alluredir', 'report', '--clean-alluredir'
            ]

            if _path is None:
                stack_t = inspect.stack()
                ins = inspect.getframeinfo(stack_t[1][0])
                file_dir = os.path.dirname(os.path.abspath(ins.filename))
                file_path = ins.filename
                if "\\" in file_path:
                    this_file = file_path.split("\\")[-1]
                elif "/" in file_path:
                    this_file = file_path.split("/")[-1]
                else:
                    this_file = file_path
                _path = os.path.join(file_dir, this_file)

            cmd_list.insert(0, _path)

            if xdist:
                cmd_list.insert(1, '-n')
                cmd_list.insert(2, 'auto')

            logger.info(cmd_list)
            pytest.main(cmd_list)

        def _parallel_execute(_params):
            if 'parallel' in strategy:
                if _params:
                    for param in _params:
                        pr = Process(target=_app_main, args=param)
                        pr.start()
            elif 'serial' in strategy:
                if _params:
                    for param in _params:
                        _app_main(*param)

        def _collect_case_and_split(device_id, _path):
            _path_list = [{item: []} for item in device_id]
            test_cases = _get_case_list(_path)
            print(test_cases)
            # 把用例均分成设备数量的份数
            n = len(device_id)
            _lists = [[] for _ in range(n)]
            for _i, item in enumerate(test_cases):
                index = _i % n  # 计算元素应该分配给哪个列表
                _lists[index].append(item)
            return _lists

        # 多设备执行策略
        if isinstance(serial, list) or isinstance(udid, list):
            params = []
            if isinstance(serial, list) and not isinstance(udid, list):
                if not serial:
                    _serial_execute(path)
                elif len(serial) == 1:
                    App.serial = serial[0]
                    _serial_execute(path)
                else:
                    # 清空上次执行的目录
                    shutil.rmtree("report", ignore_errors=True)
                    if 'full' in strategy:
                        for device in serial:
                            params.append((path, device, package, "", "", ocr_api, start, True))
                    else:
                        lists = _collect_case_and_split(serial, path)

                        for i in range(len(serial)):
                            _path = lists[i][0] if len(lists[1]) < 2 else ','.join(lists[i])
                            params.append((_path, serial[i], package, "", "", ocr_api, start))

                    # 多进程执行
                    _parallel_execute(params)

            elif isinstance(udid, list) and not isinstance(serial, list):
                if not udid:
                    _serial_execute(path)
                elif len(udid) == 1:
                    App.udid = udid[0]
                    _serial_execute(path)
                else:
                    # 清空上次执行的目录
                    shutil.rmtree(f'report', ignore_errors=True)
                    if 'full' in strategy:
                        for device in udid:
                            params.append((path, "", "", device, bundle_id, ocr_api, start, True))
                    else:
                        lists = _collect_case_and_split(udid, path)

                        for i in range(len(udid)):
                            params.append((lists[i], "", "", udid[i], bundle_id, ocr_api, start))

                    # 多进程执行
                    _parallel_execute(params)

            elif isinstance(serial, list) and isinstance(udid, list):
                raise KeyError('不支持安卓和IOS同时有多个设备')

        else:
            _serial_execute(path)

        # 公共参数重置
        common_data = {
            "base_url": None,
            "web_base_url": None,
            "headers": None,
            "ocr_service": None
        }
        # web参数重置
        web_data = {
            "cookies": None,
            "state_file": None,
            "browser_name": None,
            "headless": False,
            "maximized": False,
            "window_size": None
        }
        config.set_web_dict(web_data)
        config.set_common_dict(common_data)
        # App参数重置
        App.serial = None
        App.package = None
        App.udid = None
        App.bundle_id = None
        App.ocr_service = None
        App.auto_start = False


main = TestMain

if __name__ == '__main__':
    main()
