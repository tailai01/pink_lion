#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time          : 2023/2/22 23:22
# File          : register_route.py
# @Author       : MingTai
from app_run.app.application import app
from app_run.blue_print.admin_blue_two import admin_blue
from app_run.blue_print.user_blue_one import user_blue

app.register_blueprint(admin_blue, url_prefix='/admin')
app.register_blueprint(user_blue, url_prefix='/user')


# @app.route('/')
# def hello():
#     return 'hello i am mingtai'


# # 单独作为注册路由文件
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
