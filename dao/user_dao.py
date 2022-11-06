from sqlalchemy import or_

from dao import db
from models.user import User, UserWXMap


class UserDao:

    @staticmethod
    def add_user(user):
        db.session.add(user)
        db.session.commit()
        db.session.close()

    @staticmethod
    def query_user(user):
        record = (
            db.session.query(User)
            .filter(
                or_(User.phone == user.phone, user.phone is None),
                or_(User.id == user.id, user.id is None),
            )
            .first()
        )
        print(record)
        return record

    @staticmethod
    def query_user_by_wx_id(wx2user):
        record = (
            db.session.query(UserWXMap)
            .filter_by(user_id=wx2user.id)
            .first()
        )

        res = (
            db.session.query(User)
            .filter_by(User.id == record.id, record.id is None)
            .first()
        )

        print(res)
        return res
