#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Ryze
# @Email  : 2868280595@qq.com
# @Time   : 2023-08-24 12:51
# @Desc   : 功能描述
from sqlalchemy.orm import declarative_base, sessionmaker
from flask_login import UserMixin

from app.model import db, login_manager

# 申明基类对象
Base = declarative_base()


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    def __init__(self, username, password):
        self.username = username
        self.password = password

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10))
    password = db.Column(db.String(20))

    def verify_password(self, password):
        return self.password == password

    def __repr__(self):
        return '<User {}>'.format(self.username)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

