#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Ryze
# @Email  : 2868280595@qq.com
# @Time   : 2023-08-24 23:16
# @Desc   : 功能描述

from flask import Blueprint


userBlueprint = Blueprint('user', __name__, template_folder='templates', url_prefix="/user")


from . import users
