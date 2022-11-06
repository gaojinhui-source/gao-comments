import random
import string
from captcha.image import ImageCaptcha
from flask import Response, session, request, jsonify, make_response, redirect, url_for
from dao import redis
from models.user import UserWXMap
from restful import route_v1
from service.user import UserService
from util import const
from util.const import WECHAT_ACCESS_TOKEN
from util.utils import send_message
from flask_restful.reqparse import RequestParser
import requests


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
    parser = RequestParser()
    parser.add_argument('mobile')
    parser.add_argument('captcha')
    args = parser.parse_args()

    mobile = args.mobile
    captcha_code = args.captcha
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


@route_v1.route("/wechat_login", methods=["GET"])
def get_wechat_login():
    qcode = request.args.get("code")
    corp_id = request.args.get("appid")
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=" + corp_id + "&corpsecret=" + WECHAT_ACCESS_TOKEN
    r = requests.get(url)
    m = r.json()
    token = m["access_token"]
    u = "https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token="+token+"&code="+qcode+"&debug=1"
    r = requests.get(u)
    m1 = r.json()
    uid = m1["userid"]
    u = UserService.query_user_by_wx_id(UserWXMap(wx_id=uid))
    response = make_response(redirect(url_for("comment.getList")))
    response.set_cookie(
        const.AUTH_COOKIE_NAME, "{}".format(u.id), 60 * 60 * 24
    )  # cookie保存1天
    redis.set("user_{}".format(u.id), u.id)
    return response

