#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Ryze
# @Email  : 2868280595@qq.com
# @Time   : 2023-08-24 12:54
# @Desc   : 功能描述

from contextlib import contextmanager
from flask import current_app
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.orm import declarative_base, sessionmaker

# 申明基类对象
Base = declarative_base()


__all__ = ["db"]


# class SQLAlchemy(_SQLAlchemy):
#     @contextmanager
#     def auto_commit(self, throw=True):
#
#         try:
#             yield
#             self.session.commit()
#         except Exception as e:
#             self.session.rollback()
#             current_app.logger.exception('%r' % e)
#             if throw:
#                 raise e


db = SQLAlchemy()
