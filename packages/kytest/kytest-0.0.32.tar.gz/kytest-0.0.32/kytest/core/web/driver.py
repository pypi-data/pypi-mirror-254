"""
@Author: kang.yang
@Date: 2023/5/12 20:49
"""
from kytest.utils.log import logger
from kytest.utils.common import general_file_path, cut_and_upload
from playwright.sync_api import sync_playwright, expect


class WebDriver:

    def __init__(
            self,
            browserName: str,
            headless: bool = False,
            state: dict = None,
            maximized: bool = False,
            window_size: list = None
    ):
        """
        浏览器驱动
        @param browserName: 浏览器类型，默认chrome，还支持firefox和webkit
        @param headless: 是否使用无头模式
        @param state: 使用state.json加载登录态
        @param maximized: 是否使用全屏模式
        @param window_size: 指定窗口分辨率，如[1920, 1080]
        """
        logger.info("初始化playwright驱动")
        if headless is True and window_size is None:
            window_size = [1920, 1080]

        self.playwright = sync_playwright().start()
        _kwargs = {"headless": headless}
        if maximized and window_size is None:
            _kwargs["args"] = ['--start-maximized']
        if browserName == 'firefox':
            self.browser = self.playwright.firefox.launch(**_kwargs)
        elif browserName == 'webkit':
            self.browser = self.playwright.webkit.launch(**_kwargs)
        else:
            self.browser = self.playwright.chromium.launch(**_kwargs)

        _context_kwargs = {"storage_state": state}
        if maximized and window_size is None:
            _context_kwargs["no_viewport"] = True
        if window_size:
            _context_kwargs["viewport"] = {'width': window_size[0], 'height': window_size[1]}
        self.context = self.browser.new_context(**_context_kwargs)
        self.page = self.context.new_page()

    def switch_tab(self, locator):
        logger.info("开始切换tab")
        with self.page.expect_popup() as popup_info:
            locator.click()
        self.page = popup_info.value

    def open(self, url):
        logger.info(f"访问页面: {url}")
        self.page.goto(url)

    def storage_state(self, path=None):
        logger.info("保存浏览器状态信息")
        if not path:
            raise ValueError("路径不能为空")
        self.context.storage_state(path=path)

    @property
    def page_content(self):
        """获取页面内容"""
        logger.info("获取页面内容")
        content = self.page.content()
        logger.info(content)
        return content

    def set_cookies(self, cookies: list):
        logger.info("添加cookie并刷新页面")
        self.context.add_cookies(cookies)
        self.page.reload()

    def screenshot(self, file_name=None):
        filename, file_path = general_file_path(file_name)
        self.page.screenshot(path=file_path)
        logger.info(f"保存至: {file_path}")
        return cut_and_upload(file_path)

    def close(self):
        logger.info("关闭浏览器")
        self.page.close()
        self.context.close()
        self.browser.close()
        self.playwright.stop()

    def assert_title(self, title: str, timeout: int = 5):
        logger.info(f"断言页面标题等于: {title}")
        expect(self.page).to_have_title(title,
                                        timeout=timeout * 1000)

    def assert_url(self, url: str, timeout: int = 5):
        logger.info(f"断言页面url等于: {url}")
        expect(self.page).to_have_url(url,
                                      timeout=timeout * 1000)


if __name__ == '__main__':
    pass
