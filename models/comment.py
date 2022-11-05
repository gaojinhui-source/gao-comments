import json

from dao import db


class Comment(db.Model):
    __tableName__ = 'comment'

    id = db.Column('id', db.BigInteger, primary_key=True)
    content = db.Column('content_body', db.String(4096), nullable=False)
    user_id = db.Column('user_id', db.BigInteger, nullable=False)
    create_time = db.Column('ctime', db.DateTime, nullable=False, server_default=db.text("0000-00-00 00:00:00"))
    update_time = db.Column('mtime', db.DateTime, nullable=False, server_default=db.text("0000-00-00 00:00:00"))

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def __repr__(self):
        return 'id: {} , content : {} , user_id : {} , create_time : {} , update_time : {}'.format(self.id,
                                                                                                   self.content,
                                                                                                   self.user_id,
                                                                                                   self.create_time,
                                                                                                   self.update_time)