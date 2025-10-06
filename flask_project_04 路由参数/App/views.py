# views.py 路由+ 视图函数
import uuid

from flask import blueprints, Blueprint
from .models import *
# 蓝图
blue = Blueprint('user',__name__)

@blue.route('/')
def index():
    return 'index'
@blue.route('/hello')
def hello():
    return 'hello'

# 路由参数
# string 接受任何没有(/)的字符串，默认
# int 接受整型
# float 接受浮点数
# path 接受路径 ，可接受斜线/
# uuid 只接受uuid 字符串，唯一码，一种生成规则
# any 可以同时指定多种路径，进行限定


# string
# @blue.route('/string/<string:username>/')
# def get_string(username):
#     print(username,type(username))
#     return 'hello {}'.format(username)
# int
# @blue.route('/int/<int:id>/')
# def get_int(id):
#     print(id,type(id))
#     return 'id： {}'.format(id) # 直接返回id 报错

# float
# @blue.route('/float/<float:money>/')
# def get_float(money):
#     print(money,type(money))
#     return  'money:${}'.format(money)

# path 支持/的字符串
# @blue.route('/path/<path:url>/')
# def get_path(url):
#     print(url,type(url))
#     return 'path:{}'.format(url)

# uuid:
@blue.route('/uuid/<uuid:id>')
def get_uuid(id):
    print(type(id))
    return str(id)

@blue.route('/getuuid/')
def get_uuid2():
    import uuid
    id = uuid.uuid4()
    print(type(id))
    return 'uuid:{}'.format(id)

# any:从列出的项目中选一个
@blue.route('/any/<any(apple,banana,orange):fruit>/')
def anyfruit(fruit):
    print(type(fruit))
    return str(fruit)

# methods
# 默认不支持post
# 如果需要同时支持post 和get ,就设置methods
@blue.route('/methods/',methods=['GET','POST'])
def get_methods():
    print(type('method'))
    return 'methods'