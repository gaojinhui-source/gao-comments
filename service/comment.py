from dao.comments_dao import UserDao
from models.comment import Comment


class CommentService:
    """
        Comment 服务层
    """

    @staticmethod
    def add_comment(comment):
        UserDao.add_comment(comment)

    @staticmethod
    def remove_comment(comment):
        # TODO 检测该留言是否存在
        UserDao.remove_comment(comment)

    @staticmethod
    def list_comments(user_id):
        return UserDao.list_comments(user_id)

    @staticmethod
    def update_comment(comment):
        # TODO 检测该留言是否存在
        UserDao.update_comment(comment)
