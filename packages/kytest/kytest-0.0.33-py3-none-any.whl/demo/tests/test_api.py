"""
@Author: kang.yang
@Date: 2023/11/16 17:52
"""
import kytest


class TestApiDemo(kytest.ApiCase):
    """接口demo"""

    def test_normal_req(self):
        url = '/qzd-bff-app/qzd/v1/home/getToolCardListForPc'
        headers = {
            "user-agent-web": "X/b67aaff2200d4fc2a2e5a079abe78cc6"
        }
        params = {"type": 2}
        self.post(url, headers=headers, json=params)
        self.assertEq('data[*].showType', 2)


if __name__ == '__main__':
    """仅执行本模块"""
    kytest.main(api_host='https://app-test.qizhidao.com')

