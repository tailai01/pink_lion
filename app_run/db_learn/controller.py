#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time          : 2023/2/22 22:33
# File          : controller.py
# @Author       : MingTai
from flask import Flask

from app_run.blue_print.admin_blue_two import admin_blue
from app_run.blue_print.user_blue_one import user_blue

# 纯flask的形式启动
app = Flask(__name__)

app.register_blueprint(admin_blue, url_prefix='/admin')
app.register_blueprint(user_blue, url_prefix='/user')


@app.route('/')
def hello():
    return 'hello i am mingtai'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
