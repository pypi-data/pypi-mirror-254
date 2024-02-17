"""
@Author: kang.yang
@Date: 2023/11/16 17:36
"""
from kytest import Page, IosElem as Elem


class ImagePage(Page):
    searchBtn = Elem(text="搜索",
                     className="XCUIElementTypeSearchField")
    searchInput = Elem(className="XCUIElementTypeSearchField")
    searchResult = Elem(xpath="//Table/Cell[2]")
    schoolEntry = Elem(image="../data/校园场馆.png")
