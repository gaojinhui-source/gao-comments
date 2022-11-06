from flask import render_template, request, jsonify, make_response, redirect, url_for, session
from dao import db, redis
from models.user import User
from restful import route_user
from util import const
from util.utils import Util
from service.user import UserService


@route_user.route("/hello", methods=["GET"])
def hello():
    eng = db.get_engine()
    print(eng.connect().execute("select 1"))
    return render_template("pages/hello.html")


@route_user.route("/register", methods=["POST"])
def register():
    email = request.form["email"]
    resp = {}
    if len(email.lstrip()) <= 0 or not Util.validateEmail(email):
        resp['code'] = 403
        resp['msg'] = "您的邮箱格式有误, 请重新输入"
        return jsonify(resp)

    nickname = request.form["nickname"]
    if len(nickname.lstrip()) <= 0:
        resp['code'] = 403
        resp['msg'] = "您的用户名设置不规范，请重新设置"
        return jsonify(resp)

    phone = request.form["phone"]
    if len(phone) <= 0 or Util.validatePhone(phone):
        resp['code'] = 403
        resp['msg'] = "您的电话号码格式有误，请重新设置"
        return jsonify(resp)

    sex = int(request.form["sex"])
    if sex != 1 and sex != 0:
        resp['code'] = 403
        resp['msg'] = "您的性别设置有误，请重新设置"
        return jsonify(resp)

    user = User(name=nickname, phone=phone, email=email, sex=sex)
    UserService.add_user(user)
    return render_template("pages/login.html")


@route_user.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("pages/login.html", form={})

    resp = {}
    mobile_code = request.values.get("verification_code")
    mobile_number = request.values.get("mobile")
    print(
        "verify-code:{}, phone:{}".format(mobile_code, mobile_number)
    )

    sms_key = "sms_code:%s" % mobile_number
    if redis.get(sms_key) != mobile_code:
        resp['code'] = 403
        resp['msg'] = "您输入的验证码有误，请重新输入"
        return jsonify(resp)

    # 查询用户
    user = User(phone=mobile_number)
    user_result = UserService.query_user(user)
    if user_result is None:
        resp['code'] = 403
        resp['msg'] = "用户不存在，请重新输入"
        return jsonify(resp)

    response = make_response(redirect(url_for("comment.getList")))
    response.set_cookie(
        const.AUTH_COOKIE_NAME, "{}".format(user_result.id), 60 * 60 * 24
    )  # cookie保存1天
    redis.set("user_{}".format(user_result.id), user_result.id)
    # 登录成功后删除短信验证码
    redis.delete(sms_key)
    return response


@route_user.route("/logout", methods=["GET"])
def user_logout():
    response = make_response(redirect(url_for("user.login")))
    response.delete_cookie(const.AUTH_COOKIE_NAME)
    return response
