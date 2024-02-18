# 介绍

[Gitee](https://gitee.com/bluepang2021/kytest_project)

Android/IOS/Web/API automation testing framework based on pytest.

> 基于pytest的安卓/IOS/Web/API平台自动化测试框架，支持图像识别和OCR识别。

## 特点

* 集成`requests`/`playwright`/`facebook-wda`/`uiautomator2`
* 进阶定位方式：`图像识别定位`/`OCR识别定位`
* 集成`allure`, 支持HTML格式的测试报告
* 提供强大的`数据驱动`，支持json、yaml
* 提供丰富的断言
* 支持生成随机测试数据
* 支持设置用例依赖


## 三方依赖

* [测试报告：Allure](https://github.com/allure-framework/allure2)
* [拾取元素：weditor](https://github.com/alibaba/web-editor)
* [查看安卓设备id：adb](https://formulae.brew.sh/cask/android-platform-tools)
* [查看IOS设备id：tidevice](https://github.com/alibaba/tidevice)
* [IOS端代理：WebDriverAgent](https://github.com/appium/WebDriverAgent)

## Install

```shell
> pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ktest
```

## 🔬 Demo

[demo](/demo) 提供了丰富实例，帮你快速了解ktest的用法。

## 使用方式

### 安卓

* 不同机型设置
    - 小米：开启 “开发者选项” -> "USB调试（安全设置）允许通过usb调试修改权限或模拟点击"
    - OPPO：oppo存在权限监控，需要在开发者-> 开启 禁止权限监控 即可

* 定位方式
    - rid：根据resourceId属性定位
    - className：根据className属性定位
    - text：根据text属性定位
    - textCont：模糊匹配text属性
    - xpath：根据xpath定位
    - image：图像识别
    - ocr：ocr识别，依赖ocr服务
    - index：识别到多个元素时，根据索引选择其中一个

* 元素操作
    - click：点击
    - click_exists：元素存在才点击
    - input：输入
    - input_exists：元素存在才输入
    - input_pwd：输入密码（某些密码输入框）
    - clear：清空输入框
    - assert_exists：断言元素存在
    - assert_text：断言元素文本属性包含文本关键字


### IOS

* [安装WebDriverAgent](https://testerhome.com/topics/7220)

* 定位方式
    - name：根据name属性定位
    - label：根据label属性定位
    - labelCont：模糊匹配label属性
    - value：根据value属性定位
    - valueCont：模糊匹配value属性
    - text：根据text属性定位
    - textCont：模糊匹配text属性
    - className：根据className属性定位
    - xpath：根据xpath定位
    - image：图像识别
    - ocr：ocr识别，依赖ocr服务
    - index：识别到多个元素时，根据索引选择其中一个

* 元素操作
    - click：点击
    - click_exists：元素存在才点击
    - input：输入
    - input_exists：元素存在才输入
    - clear：清空输入框
    - assert_exists：断言元素存在
    - assert_text：断言元素文本属性包含文本关键字

### Web

* 定位方式
    - xpath：根据xpath定位
    - css：根据css selector定位
    - text：根据标签文本定位
    - placeholder：根据输入框placeholder定位
    - role：根据标签类型定位
    - name：配合role定位使用
    - label：根据label属性定位（？？？）
    - alt_text：根据alt_text属性定位（？？？）
    - title：根据title属性定位
    - test_id：根据test_id定位，标签需要设置data-testid属性
    - index：识别到多个元素时，根据索引选择其中一个

* 元素操作
    - click：点击
    - click_exists：存在才点击
    - input：输入
    - input_exists：元素存在才输入
    - enter：点击enter键
    - assert_visible：断言元素可见
    - assert_hidden：断言元素被隐藏
    - assert_text_cont：断言元素文本属性包含关键词
    - assert_text_eq：断言元素文本属性等于关键词

### 接口

* get请求
```python
url = '/qzd-bff-app/qzd/v1/home/getToolCardListForPc'
headers = {
    "user-agent-web": "X/b67aaff2200d4fc2a2e5a079abe78cc6"
}
params = {"type": 2}
self.get(url, headers=headers, params=params)
self.assert_eq('code', 0)
```

* post请求
```python
url = '/qzd-bff-app/qzd/v1/home/getToolCardListForPc'
headers = {
    "user-agent-web": "X/b67aaff2200d4fc2a2e5a079abe78cc6"
}
params = {"type": 2}
self.post(url, headers=headers, json=params)
self.assert_eq('code', 0)
```

* 文件上传
```python
path = '/qzd-bff-patent/patent/batch/statistics/upload'
files = {'static': open('../static/号码上传模板_1.xlsx', 'rb')}
self.post(path, files=files)
self.assert_eq('code', 0)
```

* form请求
```python
from kytest import FormEncoder

url = '/qzd-bff-patent/image-search/images'
file_data = (
    'logo.png',
    open('../data/logo.png', 'rb'),
    'image/png'
)
fields = {
    'key1': 'value1',  # 参数
    'imageFile': file_data  # 文件
}
form_data = FormEncoder(fields=fields)
headers = {'Content-Type': form_data.content_type}
self.post(url, data=form_data, headers=headers)
self.assert_eq("code", 0)
```
