import pymysql
import redis as redis
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy

db = _SQLAlchemy()


pymysql.install_as_MySQLdb()

redis = redis.StrictRedis(
    host="127.0.0.1", port=6379, decode_responses=True, password=""
)