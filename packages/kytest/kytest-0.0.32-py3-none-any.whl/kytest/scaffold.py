import os.path

case_content = """import kytest

from pages.adr_page import DemoPage


@kytest.story('测试demo')
class TestAdrDemo(kytest.TestCase):
    def start(self):
        self.page = DemoPage(self.driver)

    @kytest.title('进入设置页')
    def test_go_setting(self):
        self.page.adBtn.click_exists(timeout=5)
        self.page.myTab.click()
        self.page.settingBtn.click()
        self.assert_act('.me.MeSettingActivity')
        self.screenshot("设置页")


if __name__ == '__main__':
    kytest.main(
        devices=["UJK0220521066836"],
        pkg_name='com.qizhidao.clientapp',
    )

"""

page_content = """from kytest import Page, AdrElem as Elem

'''
定位方式：优先选择rid
rid: 根据resourceId进行定位
text：根据text属性进行定位
className：根据className属性进行定位
xpath：根据xpath进行定位
index：获取定位到的第index个元素
'''


class DemoPage(Page):
    # APP首页
    adBtn = Elem(rid='bottom_btn', desc='广告关闭按钮')
    myTab = Elem(text='我的', desc='我的tab')
    spaceTab = Elem(text='科创空间', desc='科创空间tab')
    # 我的页
    settingBtn = Elem(rid='me_top_bar_setting_iv', desc='设置按钮')
    # 设置页
    title = Elem(rid='tv_actionbar_title', desc='设置页标题')
    agreementText = Elem(rid='agreement_tv_2', desc='服务协议链接')

"""

run_content = """import kytest


if __name__ == '__main__':
    # 执行多个用例文件，主程序入口

    kytest.main(
        path='tests',
        device_id="UJK0220521066836",
        pkg_name='com.qizhidao.clientapp',
    )

"""


def create_scaffold(project_name):
    """create scaffold with specified project name."""

    def create_folder(path):
        os.makedirs(path)
        msg = f"created folder: {path}"
        print(msg)

    def create_file(path, file_content=""):
        with open(path, "w", encoding="utf-8") as f:
            f.write(file_content)
        msg = f"created file: {path}"
        print(msg)

    # 新增测试数据目录
    root_path = project_name
    create_folder(root_path)
    create_folder(os.path.join(root_path, "tests"))
    create_folder(os.path.join(root_path, "pages"))
    create_folder(os.path.join(root_path, "report"))
    create_folder(os.path.join(root_path, "data"))
    create_folder(os.path.join(root_path, "screenshot"))
    create_file(
        os.path.join(root_path, "pages", "adr_page.py"),
        page_content,
    )
    create_file(
        os.path.join(root_path, "tests", "test_adr.py"),
        case_content,
    )
    create_file(
        os.path.join(root_path, "run.py"),
        run_content,
    )
