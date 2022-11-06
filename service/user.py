from dao import redis
from dao.user_dao import UserDao
from models.user import User
from util.utils import send_email


class UserService:

    @staticmethod
    def add_user(user):
        # TODO 验证邮箱是否可发送
        send_email(user.email)
        UserDao.add_user(user)

    @staticmethod
    def query_user(user):
        return UserDao.query_user(user)

    @staticmethod
    def get_user_from_token(param):
        union_id = redis.get("user_{}".format(param))
        user_query = User(id=union_id)
        return UserService.query_user(user_query)

    @staticmethod
    def query_user_by_wx_id(wx2user):
        return UserDao.query_user_by_wx_id(wx2user)
