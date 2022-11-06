import json
import re
from flask import jsonify
from ronglian_sms_sdk import SmsSDK
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header


class Util:

    @staticmethod
    def validateEmail(email):
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) is not None:
            return True
        else:
            return False

    @staticmethod
    def isEmoji(content):
        if not content:
            return False
        if u"\U0001F600" <= content <= u"\U0001F64F":
            return True
        elif u"\U0001F300" <= content <= u"\U0001F5FF":
            return True
        elif u"\U0001F680" <= content <= u"\U0001F6FF":
            return True
        elif u"\U0001F1E0" <= content <= u"\U0001F1FF":
            return True
        else:
            return False

    @staticmethod
    def validatePhone(phone):
        pattern = re.compile(r'^(13[0-9]|14[0|5|6|7|9]|15[0|1|2|3|5|6|7|8|9]|'
                             r'16[2|5|6|7]|17[0|1|2|3|5|6|7|8]|18[0-9]|'
                             r'19[1|3|5|6|7|8|9])\d{8}$')
        if pattern.search(phone):
            print("手机号码合法！")
        else:
            print("手机号码非法！")


def ops_renderJSON(code=200, msg="操作成功~~", data={}, flag=True):
    if not flag:
        code = 0

    resp = {'code': code, 'msg': msg, 'data': data}
    return jsonify(resp)


'''
写入文件
'''


def writeFile(file_path=None, data=None):
    with open(file_path, 'wb') as f:
        f.write(data)


def send_message(sms_code, mobile, expire=5):
    sms_sdk = SmsSDK(accId='8aaf0708842397dd018447225dd90b6b',
                     appId='8aaf0708842397dd018447225ef80b72',
                     accToken='5f858c1f45dc47e5a7bf057be8884cd8')
    tid = '1'
    datas = ("%s" % sms_code, "%s" % expire)

    res = sms_sdk.sendMessage(tid=tid, mobile=mobile, datas=datas)
    resd = json.loads(res)
    return res


def send_email(self, receiver):
    """发送邮件"""
    sender = 'g23230014@163.com'  # 邮箱账号和发件者签名
    # 定义发送邮件的内容，支持HTML和CSS样式
    content = f"这是一个测试邮件，您无需关注"
    message = MIMEText(content, 'html', 'utf-8')  # 实例化邮件对象，并指定邮件的关键信息
    # 指定邮件的标题，同样使用utf-8编码
    message['Subject'] = Header('测试邮件')
    message['From'] = sender
    message['To'] = receiver
    smtpObj = SMTP_SSL('smtp.qq.com')  # QQ邮件服务器的链接
    smtpObj.login(user='g23230014@163.com', password='NGPHVLNSRDICQRYN')  # 通过自己的邮箱账号和获取到的授权码登录QQ邮箱
    # 指定发件人、收件人和邮件内容
    smtpObj.sendmail(sender, receiver, str(message))
    smtpObj.quit()
