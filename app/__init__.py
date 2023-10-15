#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Ryze
# @Email  : 2868280595@qq.com
# @Time   : 2023-08-24 1:26
# @Desc   : 功能描述

from flask import Flask
from app.model.users import login_manager

from app.model import db
from app.config import Config

app1 = Flask(__name__)
app1.config.from_object(Config)


db.init_app(app1)
login_manager.init_app(app1)


from app.web import userBlueprint
app1.register_blueprint(userBlueprint)
