# pip install yagmail==0.15.293
import traceback
import yagmail

from kytest.utils.allure_util import get_allure_data
from kytest.utils.log import logger
from kytest.testdata import get_now_datetime


class Mail:
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.username = user
        self.password = password

    def send_email(self, receivers, subject, contents, attachments=None):
        """
        发送邮件
        @param receivers: 收件人列表
        @param subject: 邮件主题
        @param contents: 邮件内容
        @param attachments: 附件文件的绝对路径
        @return:
        """
        try:
            logger.info(f'开始发送邮件~')
            # 初始化服务对象直接根据参数给定，更多参考SMTP(）内部
            server = yagmail.SMTP(host=self.host, port=self.port,
                                  user=self.username, password=self.password)
            # 发送内容，设置接受人等信息，更多参考SMTP.send()内部
            server.send(to=receivers,
                        subject=subject,
                        contents=contents,
                        attachments=attachments)
            server.close()
        except Exception:
            logger.info(f'发送失败~')
            print('traceback.format_exc(): {}'.format(traceback.format_exc()))
            return False

        # 无任何异常表示发送成功
        logger.info(f'发送成功~')
        return True

    def send_report(self, to_list, title, report_url):
        allure_data = get_allure_data('report')
        total = allure_data.get('total')
        passed = allure_data.get('passed')
        fail = total - passed
        rate = allure_data.get('rate')

        # 邮件内容
        title = f'{title}({get_now_datetime(strftime=True)})'
        body_str = '\n\n共 {0} 个用例，通过 {1} 个，失败 {2} 个，通过率 {3}%，详见: {4}'\
            .format(total, passed, fail, rate, report_url)

        # 发送邮件
        if fail > 0:
            self.send_email(to_list, title, body_str)
        else:
            logger.info('用例全部成功，无需通知~')


if __name__ == '__main__':
    pass





