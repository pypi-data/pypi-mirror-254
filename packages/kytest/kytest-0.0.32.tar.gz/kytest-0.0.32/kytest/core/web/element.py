"""
@Author: kang.yang
@Date: 2023/5/13 10:16
"""
import time

from kytest.utils.log import logger
from playwright.sync_api import expect
from kytest.utils.exceptions import KError
from kytest.core.web.driver import WebDriver
from kytest.utils.common import calculate_time


class WebElem:
    """
    通过selenium定位的web元素
    """

    def __init__(self,
                 driver: WebDriver = None,
                 xpath: str = None,
                 css: str = None,
                 text: str = None,
                 placeholder: str = None,
                 role: str = None,
                 name: str = None,
                 label: str = None,
                 alt_text: str = None,
                 title: str = None,
                 test_id: str = None,
                 index: int = None,
                 _debug: bool = False):
        """

        @param driver: 浏览器驱动
        @param xpath: xpath定位
        @param css: css定位
        @param text: 文本定位
        @param placeholder: 输入框placeholder定位
        @param role: role定位
        @param name: 配合role定位使用
        @param label: label定位
        @param alt_text: alt_text定位
        @param title: 控件title定位
        @param test_id: test_id定位，需要标签加上data-testid属性
        @param index: 识别到多个控件时，根据index获取其中一个
        @param _debug: 截图并圈选位置，用于调试
        """
        self._xpath = xpath
        self._css = css
        self._text = text
        self._placeholder = placeholder
        self._role = role
        self._name = name
        self._label = label
        self._alt_text = alt_text
        self._title = title
        self._test_id = test_id
        self._index = index

        self._kwargs = {}
        if self._xpath is not None:
            self._kwargs['xpath'] = self._xpath
        if self._css is not None:
            self._kwargs['css'] = self._css
        if self._text is not None:
            self._kwargs['text'] = self._text
        if self._placeholder is not None:
            self._kwargs['placeholder'] = self._placeholder
        if self._role is not None:
            self._kwargs['role'] = self._role
        if self._name is not None:
            self._kwargs['name'] = self._name
        if self._label is not None:
            self._kwargs['label'] = self._label
        if self._alt_text is not None:
            self._kwargs['alt_text'] = self._alt_text
        if self._title is not None:
            self._kwargs['title'] = self._title
        if self._test_id is not None:
            self._kwargs['test_id'] = self._test_id
        if self._index is not None:
            self._kwargs['index'] = self._index

        self._driver = driver
        self._debug = _debug

    def __get__(self, instance, owner):
        """pm模式的关键"""
        if instance is None:
            return None

        self._driver = instance.driver
        return self

    # 公共方法
    @calculate_time
    def find(self, timeout=10):
        """查找指定的一个元素"""
        element = None
        if self._text:
            # logger.info(f"根据文本定位: {self._text}")
            element = self._driver.page.get_by_text(self._text)
        if self._placeholder:
            # logger.info(f"根据输入框默认文本定位: {self._placeholder}")
            element = self._driver.page.get_by_placeholder(self._placeholder)
        if self._role:
            # logger.info(f"根据role进行定位: {self._role}")
            if self._name:
                element = self._driver.page.get_by_role(role=self._role,
                                                        name=self._name)
            else:
                element = self._driver.page.get_by_role(role=self._role)
        if self._label:
            # logger.info(f"根据label进行定位: {self._label}")
            element = self._driver.page.get_by_label(self._label)
        if self._alt_text:
            # logger.info(f"根据alt_text进行定位: {self._alt_text}")
            element = self._driver.page.get_by_alt_text(self._alt_text)
        if self._title:
            # logger.info(f"根据title进行定位: {self._title}")
            element = self._driver.page.get_by_title(self._title)
        if self._test_id:
            # logger.info(f"根据test_id进行定位: {self._test_id}")
            element = self._driver.page.get_by_test_id(self._test_id)

        if self._css:
            # logger.info(f"根据css selector定位: {self._css}")
            element = self._driver.page.locator(self._css)
        if self._xpath:
            # logger.info(f"根据xpath定位: {self._xpath}")
            element = self._driver.page.locator(self._xpath)

        if self._index:
            element = element.nth(self._index)

        try:
            element.wait_for(timeout=timeout*1000)
            logger.info("查找成功")
            if self._debug is True:
                element.evaluate('(element) => element.style.border = "2px solid red"')
                time.sleep(1)
                self._driver.screenshot("查找成功")
            return element
        except:
            logger.info("查找失败")
            self._driver.screenshot("查找失败")
            raise KError(f"{self._kwargs} 查找失败")

    def exists(self, timeout=5):
        logger.info(f'判断元素 {self._kwargs} 是否存在')
        _element = self.find(timeout=timeout)
        _is_visible = _element.is_visible(timeout=1000*timeout)
        logger.info(_is_visible)
        return _is_visible

    # 属性
    @property
    def text(self):
        logger.info(f"获取 {self._kwargs} 文本属性")
        elems = self.find().all()
        text = [elem.text_content() for elem in elems]
        logger.info(text)
        return text

    # 其他方法
    def click(self, timeout=5):
        logger.info(f"点击 {self._kwargs}")
        self.find(timeout=timeout).click()

    def click_exists(self, timeout=5):
        logger.info(f"元素 {self._kwargs} 存在才点击")
        if self.exists(timeout=timeout):
            self.click(timeout=timeout)

    def input(self, text, timeout=5, enter=False):
        logger.info(f"输入文本: {text}")
        _element = self.find(timeout=timeout)
        _element.fill(text)
        if enter is True:
            time.sleep(1)
            _element.press('Enter', timeout=timeout*1000)

    def input_exists(self, text, timeout=5, enter=False):
        logger.info(f"元素 {self._kwargs} 才输入文本 {text}")
        if self.exists(timeout=timeout):
            self.input(text, timeout=timeout, enter=enter)

    def enter(self, timeout=5):
        logger.info("点击enter")
        self.find(timeout=timeout).press("Enter")

    def check(self, timeout=5):
        logger.info("选择选项")
        self.find(timeout=timeout).check()

    def select(self, value: str, timeout=5):
        logger.info("下拉选择")
        self.find(timeout=timeout).select_option(value)

    def assert_visible(self, timeout=5):
        logger.info(f"断言 {self._kwargs} 可见")
        expect(self.find(timeout=timeout)).to_be_visible()

    def assert_hidden(self, timeout=5):
        logger.info(f"断言 {self._kwargs} 被隐藏")
        expect(self.find(timeout=timeout)).to_be_hidden()

    def assert_text_cont(self, text: str, timeout=5):
        logger.info(f"断言 {self._kwargs} 包含文本: {text}")
        expect(self.find(timeout=timeout)).to_contain_text(text)

    def assert_text_eq(self, text: str, timeout=5):
        logger.info(f"断言 {self._kwargs} 文本等于: {text}")
        expect(self.find(timeout=timeout)).to_have_text(text)


class FraElem(WebElem):

    def __init__(self,
                 driver: WebDriver = None,
                 frame: str = None,
                 xpath: str = None,
                 css: str = None,
                 text: str = None,
                 placeholder: str = None,
                 index: int = None):
        """

        @param driver: 浏览器驱动
        @type frame: frame定位方式，使用正常的css定位方式即可
        @param xpath: 根据xpath进行定位
        @param css: 根据css selector进行定位
        @param text: 根据标签的文本定位
        @param placeholder: 根据输入框的placeholder定位
        """
        super().__init__(driver,
                         xpath,
                         css,
                         text,
                         placeholder,
                         index)
        self._driver = driver

        self._frame_loc = frame
        self._xpath = xpath
        self._css = css
        self._text = text
        self._placeholder = placeholder
        self._index = index

        self._kwargs = {}
        if self._frame_loc is not None:
            self._kwargs['frame'] = self._frame_loc
        if self._xpath is not None:
            self._kwargs['xpath'] = self._xpath
        if self._css is not None:
            self._kwargs['css'] = self._css
        if self._text is not None:
            self._kwargs['text'] = self._text
        if self._placeholder is not None:
            self._kwargs['placeholder'] = self._placeholder
        if self._index is not None:
            self._kwargs['index'] = self._index

    @calculate_time
    def find(self, timeout=5):
        element = None
        if self._text:
            logger.info(f"根据文本定位: {self._text}")
            element = self._driver.page.frame_locator(self._frame_loc).\
                get_by_text(self._text)
        if self._placeholder:
            logger.info(f"根据输入框默认文本定位: {self._placeholder}")
            element = self._driver.page.frame_locator(self._frame_loc).\
                get_by_placeholder(self._placeholder)
        if self._css:
            logger.info(f"根据css定位: {self._css}")
            element = self._driver.page.frame_locator(self._frame_loc).locator(self._css)
        if self._xpath:
            logger.info(f"根据xpath定位: {self._xpath}")
            element = self._driver.page.frame_locator(self._frame_loc).locator(self._xpath)
        if self._index:
            element = element.nth(self._index)

        try:
            element.wait_for(timeout=timeout*1000)
            logger.info("查找成功")
            return element
        except:
            logger.info("查找失败")
            self._driver.screenshot("查找失败")
            raise KError(f"{self._kwargs} 查找失败")


if __name__ == '__main__':
    pass

