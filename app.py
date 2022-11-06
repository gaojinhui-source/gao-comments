import datetime

from flask import Flask, session
from dao import db
from restful.v1 import route_v1
from restful.comment import route_comment
from restful.user import route_user

import config

if __name__ == '__main__':
    server = Flask(__name__)
    server.config.from_object(config)
    server.secret_key = "understaffed"
    server.permanent_session_lifetime = datetime.timedelta(seconds=10 * 60)

    # 初始化dao
    db.init_app(server)

    # 注册蓝图
    server.register_blueprint(route_comment, url_prefix="/comment")
    server.register_blueprint(route_user, url_prefix="/user")
    server.register_blueprint(route_v1, url_prefix="/v1")

    server.run()
