# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# flask-sqlacodegen "mysql+pymysql://root:123456@127.0.0.1:3306/flask_learn" --tables mmall_user --outfile "app_run/app/common/models/mmall_user.py" --flask
class MmallUser(db.Model):
    __tablename__ = 'mmall_user'

    id = db.Column(db.Integer, primary_key=True, info='用户表id')
    username = db.Column(db.String(50), nullable=False, unique=True, info='用户名')
    password = db.Column(db.String(50), nullable=False, info='用户密码，MD5加密')
    email = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    question = db.Column(db.String(100), info='找回密码问题')
    answer = db.Column(db.String(100), info='找回密码答案')
    role = db.Column(db.Integer, nullable=False, info='角色0-管理员,1-普通用户')
    create_time = db.Column(db.DateTime, nullable=False, info='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, info='最后一次更新时间')
