# views.py 路由+ 视图函数

from flask import Blueprint, redirect, url_for
from .models import *
# 蓝图
blue = Blueprint('user',__name__)

@blue.route('/')
def index():
    return 'index'
@blue.route('/hello/')
def hello():
    return 'hello'
# redirect重定向
@blue.route('/redirect/')
def make_redirect():
    pass
    # 重定向的几种方式
    # return redirect('http://www.qq.com')
    # return redirect('/hello/')

    # url_for 反向解析，通过视图函数名反向寻找路由
    # url_for('蓝图名称'.‘视图函数名称’)
    ret = url_for('user.hello')
    print(ret)
    return redirect(ret)

    ret2 = url_for('user.hello',name='王五',age=18)
    return redirect(ret2)


