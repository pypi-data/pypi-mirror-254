"""
@Author: kang.yang
@Date: 2023/11/16 17:48
"""
import kytest
from pages.image_page import ImagePage


class TestImageDemo(kytest.IosCase):
    """ocr识别demo"""

    def start(self):
        self.keyword = "南山文体通"
        self.page = ImagePage(self.driver)

    def test_nanshan_wtt(self):
        self.page.searchBtn.click()
        self.page.searchInput.\
            input(self.keyword)
        self.page.searchResult.click()
        self.page.schoolEntry.click()
        self.sleep(5)


if __name__ == '__main__':
    kytest.main(
        udid='00008101-000E646A3C29003A',
        bundle_id='com.tencent.xin'
    )
