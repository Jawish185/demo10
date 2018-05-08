#!/usr/bin/python3
# -*- coding:utf-8 -*-


from __future__ import unicode_literals
from .upload_views import (
    UploadFileHandle
)

urls = [
    #从/upload/file过来的请求，将调用upload_views里面的UploadFileHandle类
    (r'file', UploadFileHandle)
]