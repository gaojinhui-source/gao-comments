from dao.user_dao import UserDao


class UserService:

    @staticmethod
    def add_user(user):
        # TODO 验证邮箱是否可发送
        UserDao.add_user(user)

    @staticmethod
    def query_user(user):
        return UserDao.query_user(user)

    @staticmethod
    def get_user_from_token(param):
        pass
