#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time          : 2023/2/22 22:42
# File          : admin_blue_two.py
# @Author       : MingTai
from flask import Blueprint

admin_blue = Blueprint('admin_blue', __name__)


@admin_blue.route('/get_admin_detail')
def get_admin_detail():
    return 'get_admin_detail'


@admin_blue.route('/get_admin_info')
def get_admin_info():
    return 'get_admin_info'
