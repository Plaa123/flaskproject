# views.py 路由+ 视图函数

from flask import Blueprint, request
from .models import *
# 蓝图
blue = Blueprint('user',__name__)

@blue.route('/')
def index():
    return 'index'
@blue.route('/hello')
def hello():
    return 'hello'

# 请求与响应
# request 请求
# response:响应
# http一次前后端交互：先请求，后响应
# request：客户端向服务器发送的请求,服务器在接收到客户端的请求后，会自动创建request对象
# 由flask框架创建，request对象不可修改
# 属性：
# URL 完整请求地址
# base_url 去掉get参数的URL
# host_url只有主句和端口号的URL
# path 路由中的路径
# method 请求方法
# remote_addr 请求的客户端地址
# args get请求参数
# form post请求参数
# files 文件上传
# headers 请求头
# cookies 请求中的cookie
# ImmutableMultiDicti 类型：
# 类似字典的数据结构，与字典的区别，可以存在相同的键
# args和form 都是ImmutableMultiDict的对象
# ImmutableMultiDict 中数据获取方式：
# dict['uname'] 或dicti.get('uname')
# 获取指定key 对应的所有值：dict.getlist('uname')


@blue.route('/request/',methods=['GET','POST'])
def get_request():
    pass
    print(request)

    # 重要属性
    print(request.method) # 请求方法 POST 或GET
    # get请求的参数
    # ImmutableMultiDict :类字典对象，区别是可以出现重复的key
    print(request.args) # ImmutableMultiDict([('name', 'zhangsan'), ('name', 'lisi'), ('age', '33'), ('age', '22')])
    # print(request.args['name'],request.args['age']) # zhangsan 33
    # print(request.args.get('name')) # zhangsan
    # print(request.args.getlist('name')) # ['zhangsan', 'lisi']

    # Post 请求的参数
    print(request.form) # ImmutableMultiDict([('name', 'lucy'), ('age', '20')])
    print(request.form.get('name')) # lucy

    # cookie
    print(request.cookies) #ImmutableMultiDict([('name', 'hello')])

    print(request.url) # http://127.0.0.1:5001/request/?name=zhangsan&age=33&name=lisi&age=22
    print(request.path) # /request/
    print(request.base_url) # http://127.0.0.1:5001/request/
    print(request.host_url) # http://127.0.0.1:5001/
    print(request.files) # 文件内容ImmutableMultiDict([])
    print(request.remote_addr) # 客户端的IP Host: 127.0.0.1:5001
    print(request.headers) # 请求头User-Agent: python-requests/2.32.5
    print(request.user_agent) # 用户代理，包括浏览器和操作系统的信息 python-requests/2.32.5


    return "request ok!"
