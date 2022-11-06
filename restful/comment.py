from flask import request, jsonify, redirect, url_for, render_template

from models.comment import Comment
from restful import route_comment
from service.comment import CommentService
from service.user import UserService
from util import const


@route_comment.route("/add/", methods=["POST"])
def add():
    resp = {}
    user = UserService.get_user_from_token(request.cookies[const.AUTH_COOKIE_NAME])
    if user is None:
        resp['code'] = 403
        resp['msg'] = "用户未登录"
        return jsonify(resp)

    content = request.form["content_body"]
    if len(content) <= 0:
        resp['code'] = 403
        resp['msg'] = "留言消息不能为空"
        return jsonify(resp)

    comment = Comment(content=content, user_id=user.id)
    CommentService.add_comment(comment)
    return redirect(url_for("comment.list"))


@route_comment.route("/remove", methods=["DELETE"])
def remove():
    resp = {}
    user = UserService.get_user_from_token(request.cookies[const.AUTH_COOKIE_NAME])
    if user is None:
        resp['code'] = 403
        resp['msg'] = "用户未登录"
        return jsonify(resp)

    comment_id = request.args["comment_id"]
    user_id = user.id
    comment = Comment(id=comment_id, user_id=user_id)

    CommentService.remove_comment(comment)
    return redirect(url_for("comment.getList"))


@route_comment.route("/update", methods=["PUT"])
def update():
    resp = {}
    user = UserService.get_user_from_token(request.cookies[const.AUTH_COOKIE_NAME])
    if user is None:
        resp['code'] = 403
        resp['msg'] = "用户未登录"
        return jsonify(resp)

    content = request.form["content_body"]
    comment_id = request.form["comment_id"]
    comment = Comment(content=content, id=comment_id, user_id=user.id)

    CommentService.update_comment(comment)
    return redirect(url_for("comment.getList"))


@route_comment.route("/list/", methods=["GET"])
def getList():

    resp = {}
    user = UserService.get_user_from_token(request.cookies[const.AUTH_COOKIE_NAME])
    if user is None:
        resp['code'] = 403
        resp['msg'] = "用户未登录"
        return jsonify(resp)

    # TODO 分页，但是前端貌似暂不支持
    messages_list = CommentService.list_comments(user.id)
    return render_template("pages/messages.html", messages=messages_list, user=user)
