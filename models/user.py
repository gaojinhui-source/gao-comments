from dao import db


class User(db.Model):
    __tableName__ = "user"

    id = db.Column("id", db.BigInteger, primary_key=True)
    name = db.Column("nickname", db.String(256), nullable=False)
    phone = db.Column("phone", db.String(32), nullable=False)
    email = db.Column("email", db.String(64), unique=True, nullable=False)
    sex = db.Column("sex", db.Integer, nullable=True)
    create_time = db.Column("ctime", db.DateTime, nullable=False, server_default=db.text("0000-00-00 00:00:00"))
    update_time = db.Column("mtime", db.DateTime, nullable=False, server_default=db.text("0000-00-00 00:00:00"))

    def __repr__(self):
        return "user  id:{}, name:{}, phone:{}, email:{}, sex:{}".format(
            self.id, self.name, self.phone, self.email, self.sex
        )


class UserWXMap:
    __tableName__ = "qywx_user_map"

    id = db.Column("id", db.BigInteger, primary_key=True)
    wx_id = db.Column("wx_id", db.BigInteger, nullable=False)
    user_id = db.Column("user_id", db.BigInteger, nullable=False)
    create_time = db.Column("ctime", db.DateTime, nullable=False, server_default=db.text("0000-00-00 00:00:00"))
    update_time = db.Column("mtime", db.DateTime, nullable=False, server_default=db.text("0000-00-00 00:00:00"))

    def __repr__(self):
        return "user  id:{}, wx_id:{}, user_id:{}, ctime:{}, mtime:{}".format(
            self.id, self.wx_id, self.user_id, self.create_time, self.update_time
        )
