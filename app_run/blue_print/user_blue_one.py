#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time          : 2023/2/22 22:42
# File          : user_blue_one.py
# @Author       : MingTai

from flask import Blueprint

user_blue = Blueprint('user_blue', __name__)


@user_blue.route('/get_user_detail')
def get_user_detail():
    return 'get_user_detail'


@user_blue.route('/get_user_info')
def get_user_info():
    return 'get_user_info'
