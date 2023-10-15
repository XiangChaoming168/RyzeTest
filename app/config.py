#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Ryze
# @Email  : 2868280595@qq.com
# @Time   : 2023-08-24 19:45
# @Desc   : 功能描述

num = 1

class Config(object):
    SECRET_KEY = "ryze"
    # 步骤1：配置创建数据库参数
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + "ryze.db"  # 数据库存放位置
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
