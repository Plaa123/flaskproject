# views.py 路由+ 视图函数
import datetime

from flask import Blueprint, render_template, request, redirect
from .models import *
# 蓝图
blue = Blueprint('user',__name__)

# 首页
@blue.route('/')
@blue.route('/home/')
def home():
    # 4.获取cookie
    username= request.cookies.get('user')
    return render_template('home.html',username=username)

# 登录
@blue.route('/login/',methods=['GET','POST'])
def login():
    # get:访问登录页面
    if request.method == 'GET':
        return render_template('login.html')
    # post:实现登录功能
    elif request.method == 'POST':
        pass
        # 1.获取前段提交过来的数据
        username = request.form.get('username')
        password = request.form.get('password')
        # 2.模拟登录，用户名和密码验证
        if username=='lisi' and password=='123':
            # 登录成功
            response = redirect('/home/')
        # 3.设置cookie,不能有中文
            # response.set_cookie('user',username) # 默认浏览器关闭则cookie失效

            # max_age：过期时间,默认是秒
            # response.set_cookie('user',username,max_age=3600*24*7) # 7天后过期
            # expires：指定的datetime日期
            response.set_cookie('user',username,max_age=3600*24*7,expires=datetime.datetime(2025,12,30))
            return response

        else:
            return '用户名或密码错误'
# 注销
@blue.route('/logout/')
def logout():
    response = redirect('/home/')
    response.delete_cookie('user')
    return response



