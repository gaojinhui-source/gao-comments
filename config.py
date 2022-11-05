# Flask相关
JSON_AS_ASCII = False

# MySQL相关
DEBUG = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = (
    "mysql://root:123456@127.0.0.1:3306/flask_demo"
)
SQLALCHEMY_ENCODING = "utf-8"

# 邮件相关
MAIL_SERVER = 'smtp.163.com'  # 电子邮件服务器的主机名或IP地址
MAIL_PORT = '25'  # 电子邮件服务器的端口
MAIL_USE_TLS = True  # 启用传输层安全
MAIL_USERNAME = 'g23230014@163.com'  # os.environ.get('MAIL_USERNAME') #邮件账户用户名
MAIL_PASSWORD = 'NGPHVLNSRDICQRYN'  # os.environ.get('MAIL_PASSWORD'
