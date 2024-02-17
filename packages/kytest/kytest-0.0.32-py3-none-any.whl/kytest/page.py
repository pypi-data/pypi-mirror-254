"""
@Author: kang.yang
@Date: 2023/9/20 11:21
"""
from urllib import parse
from kytest.utils.config import config
from kytest.utils.exceptions import KError


class Page(object):
    """页面基类，用于pom模式封装"""

    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str = None):
        if getattr(self, 'url', None) is None:
            if url is None:
                raise KError('url不能为空')
        else:
            url = getattr(self, 'url')

        if not url.startswith('http'):
            host = config.get_common('web_base_url')
            if host is not None:
                url = parse.urljoin(host, url)
            else:
                raise KError('host不能为空')

        self.driver.open(url)
        # cookies = config.get_web("cookies")
        # if cookies:
        #     self.driver.set_cookies(cookies)




