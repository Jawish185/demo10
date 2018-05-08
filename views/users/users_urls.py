#! /usr/bin/python3
# -*- coding:utf-8 -*-


from __future__ import unicode_literals
from .users_views import (
    RegistHandle,
    LoginHandle
)

urls = [
    #从/users/regist过来的请求，将调用users_views里面的RegistHandle类
    (r'regist', RegistHandle),
    (r'login', LoginHandle)
]
	