from sqlalchemy import or_

from dao import db
from models.user import User


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
