import kytest
from kytest import *
from pages.adr_page import DemoPage


@story('测试demo')
class TestAdrDemo(kytest.AdrCase):
    def start(self):
        self.page = DemoPage(self.driver)
        self.set_act = '.me.MeSettingActivity'

    @title('进入设置页')
    def test_go_setting(self):
        self.page.adBtn.click_exists()
        self.page.myTab.click()
        self.page.setBtn.click()
        self.assert_act(self.set_act)
        self.screenshot("设置页")

    @title('进入全部服务')
    def test_all_service(self):
        self.page.adBtn.click_exists()
        self.page.moreService.click()
        # self.sleep(5)
        self.screenshot('全部服务页')


