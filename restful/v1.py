import random
import string
from captcha.image import ImageCaptcha
from flask import Response, session, request, jsonify
from dao import redis
from restful import route_v1
from util.utils import send_message


@route_v1.route("/captcha", methods=["GET"])
def get_captcha():
    img_code = ''.join(random.sample(string.digits + string.ascii_lowercase, 4))
    captcha = ImageCaptcha(width=120, height=50)  # 生成图片
    img = captcha.generate(img_code)
    session['imageCode'] = img_code.lower()
    print(session['imageCode'])
    return Response(img)


@route_v1.route("/verification-code", methods=["POST"])
def get_mobile_captcha():
    resp = {}
    param = {}
    data = request.data
    jsonify()
    mobile = request.form["mobile"]
    captcha_code = request.form["captcha"]
    if captcha_code.lower() != session['imageCode'].lower():
        resp['code'] = 403
        resp['msg'] = "图形验证码不正确，请重新输入"
        return jsonify(resp)
    sms_code = random.randint(100000, 999999)
    send_message(sms_code, mobile)
    sms_key = "sms_code:%s" % mobile
    redis.set(sms_key, sms_code, ex=300)
    print("<<<验证码>>>", sms_code)
    return jsonify(msg="验证码已发送，请注意查收", code=200)





