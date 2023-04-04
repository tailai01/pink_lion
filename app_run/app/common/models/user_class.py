#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time          : 2023/2/22 23:43
# File          : user_class.py
# @Author       : MingTai
from flask_sqlalchemy import SQLAlchemy
from app_run.app.application import db


class User(db.Model):
    Host = db.Column(db.String(80), primary_key=True)
    id = db.Column(db.Integer, primary_key=True, info='用户表id')
    username = db.Column(db.String(50), nullable=False, unique=True, info='用户名')
    password = db.Column(db.String(50), nullable=False, info='用户密码，MD5加密')
    email = db.Column(db.String(50))
    phone = db.Column(db.String(20))


if __name__ == '__main__':
    db.create_all()
