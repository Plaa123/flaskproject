# views.py 路由+ 视图函数

from flask import blueprints, Blueprint
from models import *
# 蓝图
blue = Blueprint('user',__name__)

@blue.route('/')
def index():
    return 'index'
@blue.route('/hello')
def hello():
    return 'hello'
