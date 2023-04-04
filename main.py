#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time          : 2023/2/22 22:23
# File          : main.py
# @Author       : MingTai
# app文件夹
from app_run.app.register_route import *

# 单独作为启动文件
# 启动后访问 http://10.240.229.210:5000/admin/get_admin_detail
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
