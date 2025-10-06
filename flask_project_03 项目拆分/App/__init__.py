# __init__.py初始化文件,创建flask 应用
from flask import Flask
from .views import blue

def create_app():
    app = Flask(__name__)

    # 注册蓝图
    app.register_blueprint(blueprint=blue)
    # app.config.from_pyfile('config.py')
    return app