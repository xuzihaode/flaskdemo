from flask import Flask
import 配置文件
from 扩展插件 import db, mail
from 模型 import UserModel
from 蓝图.权限 import bp as auth_bp
from 蓝图.问答 import bp as qa_bp
from flask_migrate import Migrate

app = Flask(__name__)
# 绑定配置文件
app.config.from_object(配置文件)

db.init_app(app)
migrate = Migrate(app, db)

mail.init_app(app)


app.register_blueprint(auth_bp)
app.register_blueprint(qa_bp)

if __name__ == '__main__':
    app.run()
