"""
@Author: kang.yang
@Date: 2023/10/26 09:48
"""
import time
import json
import os

from urllib import parse
# from typing import Union
from kytest.utils.log import logger
from kytest.utils.config import config
from kytest.core.api.request import HttpReq
from kytest.core.ios.driver import IosDriver
from kytest.core.ios.element import IosElem
from kytest.core.web.driver import WebDriver
from kytest.core.web.element import WebElem
from kytest.core.android.driver import AdrDriver
from kytest.core.android.element import AdrElem
from kytest.running.conf import App


class ApiCase(HttpReq):
    """
    测试用例基类，所有测试用例需要继承该类
    """
    # ---------------------初始化-------------------------------
    def start_class(self):
        """
        Hook method for setup_class fixture
        :return:
        """
        pass

    def end_class(self):
        """
        Hook method for teardown_class fixture
        :return:
        """
        pass

    @classmethod
    def setup_class(cls):
        cls().start_class()

    @classmethod
    def teardown_class(cls):
        cls().end_class()

    def start(self):
        """
        Hook method for setup_method fixture
        :return:
        """
        pass

    def end(self):
        """
        Hook method for teardown_method fixture
        :return:
        """
        pass

    def setup_method(self):
        self.start_time = time.time()

        self.start()

    def teardown_method(self):
        self.end()

        take_time = time.time() - self.start_time
        logger.info("用例耗时: {:.2f} s".format(take_time))

    # 公共方法
    @staticmethod
    def sleep(n: float):
        """休眠"""
        logger.info(f"暂停: {n}s")
        time.sleep(n)


class AdrCase(HttpReq):
    """
    测试用例基类，所有测试用例需要继承该类
    """

    driver: AdrDriver = None

    # ---------------------初始化-------------------------------
    def start_class(self):
        """
        Hook method for setup_class fixture
        :return:
        """
        pass

    def end_class(self):
        """
        Hook method for teardown_class fixture
        :return:
        """
        pass

    @classmethod
    def setup_class(cls):
        cls().start_class()

    @classmethod
    def teardown_class(cls):
        cls().end_class()

    def start(self):
        """
        Hook method for setup_method fixture
        :return:
        """
        pass

    def end(self):
        """
        Hook method for teardown_method fixture
        :return:
        """
        pass

    def setup_method(self):
        self.start_time = time.time()

        # device_id = config.get_app("serial")
        # pkg_name = config.get_app("package")
        self.driver = AdrDriver(App.serial, App.package)
        if App.auto_start is True:
            self.driver.start_app()

        self.start()

    def teardown_method(self):
        self.end()

        if App.auto_start is True:
            self.driver.stop_app()

        take_time = time.time() - self.start_time
        logger.info("用例耗时: {:.2f} s".format(take_time))

    # 公共方法
    @staticmethod
    def sleep(n: float):
        """休眠"""
        logger.info(f"暂停: {n}s")
        time.sleep(n)

    def screenshot(self, name: str):
        """截图"""
        self.driver.screenshot(name)

    # UI方法
    def elem(self, *args, **kwargs):
        return AdrElem(self.driver, *args, **kwargs)

    # 安卓方法
    def assert_act(self, activity_name: str, timeout=5):
        """断言当前页面的activity"""
        self.driver.assert_act(activity_name, timeout)


class IosCase(HttpReq):
    """
    测试用例基类，所有测试用例需要继承该类
    """

    driver: IosDriver = None

    # ---------------------初始化-------------------------------
    def start_class(self):
        """
        Hook method for setup_class fixture
        :return:
        """
        pass

    def end_class(self):
        """
        Hook method for teardown_class fixture
        :return:
        """
        pass

    @classmethod
    def setup_class(cls):
        cls().start_class()

    @classmethod
    def teardown_class(cls):
        cls().end_class()

    def start(self):
        """
        Hook method for setup_method fixture
        :return:
        """
        pass

    def end(self):
        """
        Hook method for teardown_method fixture
        :return:
        """
        pass

    def setup_method(self):
        self.start_time = time.time()

        # device_id = config.get_app("udid")
        # pkg_name = config.get_app("bundle_id")
        self.driver = IosDriver(App.udid, App.bundle_id)
        if App.auto_start is True:
            self.driver.start_app()

        self.start()

    def teardown_method(self):
        self.end()

        if App.auto_start is True:
            self.driver.stop_app()

        take_time = time.time() - self.start_time
        logger.info("用例耗时: {:.2f} s".format(take_time))

    # 公共方法
    @staticmethod
    def sleep(n: float):
        """休眠"""
        logger.info(f"暂停: {n}s")
        time.sleep(n)

    def screenshot(self, name: str):
        """截图"""
        self.driver.screenshot(name)

    # UI方法
    def elem(self, *args, **kwargs):
        return IosElem(self.driver, *args, **kwargs)


class WebCase(HttpReq):
    """
    测试用例基类，所有测试用例需要继承该类
    """

    driver: WebDriver = None

    # ---------------------初始化-------------------------------
    def start_class(self):
        """
        Hook method for setup_class fixture
        :return:
        """
        pass

    def end_class(self):
        """
        Hook method for teardown_class fixture
        :return:
        """
        pass

    @classmethod
    def setup_class(cls):
        cls().start_class()

    @classmethod
    def teardown_class(cls):
        cls().end_class()

    def start(self):
        """
        Hook method for setup_method fixture
        :return:
        """
        pass

    def end(self):
        """
        Hook method for teardown_method fixture
        :return:
        """
        pass

    def setup_method(self):
        self.start_time = time.time()

        browserName = config.get_web("browser_name")
        headless = config.get_web("headless")
        maximized = config.get_web("maximized")
        window_size = config.get_web("window_size")

        state_file = config.get_web("state_file")
        if not state_file:
            try:
                cookies = config.get_web("cookies")
                if not os.path.exists("data"):
                    os.makedirs("data")
                state_file = os.path.join("data", "state.json")
                state_json = {
                    "cookies": cookies
                }
                if cookies:
                    with open(state_file, "w") as f:
                        f.write(json.dumps(state_json))
            except Exception as e:
                print(e)
                state_file = None

        self.driver = WebDriver(
            browserName=browserName,
            headless=headless,
            state=state_file,
            maximized=maximized,
            window_size=window_size
        )

        self.start()

    def teardown_method(self):
        self.end()

        self.driver.close()

        take_time = time.time() - self.start_time
        logger.info("用例耗时: {:.2f} s".format(take_time))

    # 公共方法
    @staticmethod
    def sleep(n: float):
        """休眠"""
        logger.info(f"暂停: {n}s")
        time.sleep(n)

    def screenshot(self, name: str):
        """截图"""
        self.driver.screenshot(name)

    # UI方法
    def elem(self, *args, **kwargs):
        return WebElem(self.driver, *args, **kwargs)

    # web方法
    def assert_title(self, title: str, timeout: int = 5):
        """断言页面标题"""
        self.driver.assert_title(title, timeout)

    @staticmethod
    def is_url_has_http(url):
        """针对为空和只有路径的情况，使用默认host进行补全"""
        host = config.get_common("web_base_url")
        if url is None:
            url = host
        if 'http' not in url:
            url = parse.urljoin(host, url)
        return url

    def assert_url(self, url: str = None, timeout: int = 5):
        """断言页面url"""
        url = self.is_url_has_http(url)
        self.driver.assert_url(url, timeout)

    def open(self, url):
        """打开页面"""
        url = self.is_url_has_http(url)
        self.driver.open(url)
        # cookies = config.get_web("cookies")
        # if cookies:
        #     self.driver.set_cookies(cookies)

