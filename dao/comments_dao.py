from dao import db
from models.comment import Comment


class UserDao:

    @staticmethod
    def add_comment(comment):
        db.session.add(comment)
        db.session.commit()
        db.session.close()

    @staticmethod
    def remove_comment(comment):
        record = (
            db.session.query(Comment)
            .filter(Comment.id == comment.id, Comment.user_id == comment.user_id)
            .first()
        )
        if record is None:
            return
        db.session.delete(record)
        db.session.commit()
        db.session.close()

    @staticmethod
    def list_comments(user_id):
        comments = db.session.query(Comment).filter_by(user_id=user_id).all()
        return comments

    @staticmethod
    def update_comment(comment):
        print("query comment : {}".format(comment))
        record = (
            db.session.query(Comment)
            .filter_by(id=comment.id, user_id=comment.user_id)
            .first()
        )
        print("query result : {}", record)
        record.content = comment.content
        db.session.commit()
        db.session.close()
        
        