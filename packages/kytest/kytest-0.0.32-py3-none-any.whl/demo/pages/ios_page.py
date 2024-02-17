"""
@Author: kang.yang
@Date: 2023/11/16 17:36
"""
from kytest import Page, IosElem as Elem


class DemoPage(Page):
    adBtn = Elem(label='close white big')
    myTab = Elem(label='我的')
    setBtn = Elem(label='settings navi')
    about = Elem(text="关于企知道")
