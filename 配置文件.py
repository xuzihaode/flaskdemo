# 数据库配置信息
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'oa'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮箱配置信息
MAIL_SERVER = 'smtp.qq.com',
MAIL_USE_SSL = True,
MAIL_PORT = '465',
MAIL_USERNAME = '邮箱账户',
MAIL_PASSWORD = '授权码'
MAIL_DEFAULT_SENDER = '邮箱账户'
