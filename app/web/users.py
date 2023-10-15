#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Ryze
# @Email  : 2868280595@qq.com
# @Time   : 2023-08-24 23:17
# @Desc   : 功能描述

from flask import request, render_template, url_for, redirect, jsonify
from flask_login import login_user, login_required, logout_user, current_user

from app.model.users import User
from app.web import userBlueprint
from app import config


@userBlueprint.route('/login', methods=["GET", "POST"])
def login():
    form = request.form
    if request.method == 'POST':
        print(form.get("username"))
        user = User.query.filter_by(username=form.get("username")).first()
        if user and user.verify_password(user.password):
            login_user(user)

            return "hello %s" % user.username
        else:
            return "login fail!"

    return render_template('login.html')


@userBlueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.login'))


@userBlueprint.route('/welcome', methods=["GET"])
@login_required
def welcome():
    return render_template('welcome.html', user=current_user)


@userBlueprint.route('/v1', methods=["POST"])
def v1():
    data = request.get_json()
    return jsonify(data=data)


@userBlueprint.route('/v2', methods=["GET"])
def v2():
    config.num = config.num + 1
    return str(config.num)


@userBlueprint.route('/v3', methods=["GET"])
def v3():
    return str(config.num)
