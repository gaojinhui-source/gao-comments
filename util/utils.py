import json
import re
from flask import jsonify
from ronglian_sms_sdk import SmsSDK


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

def send_mail():
    msg = Message(theme, sender='1308454615@qq.com', recipients=[username],body=content)        #使用Messgae方法
    mail.send(msg)              #使用Mail类中的send()方法
    return '邮件发送成功'
