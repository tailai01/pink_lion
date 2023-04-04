#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time          : 2023/2/22 23:22
# File          : application.py
# @Author       : MingTai
# 初始化文件

# 纯flask的形式启动
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 相关配置
# 数据库链接地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask_learn'
# 是否追踪数据库，开启会触发狗子函数，一般不开启，影响性能
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 是否显示底层执行的SQL语句
app.config['SQLALCHEMY_ECHO'] = True

# 创建组件对象
db = SQLAlchemy(app)
# 初始化数据库和框架
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
