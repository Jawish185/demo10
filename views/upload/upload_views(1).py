#! /usr/bin/python3
# -*- coding:utf-8 -*-

import tornado.web
import os
from tornado.escape import json_decode
import logging
from logging.handlers import TimedRotatingFileHandler
import json


#从commons中导入http_response方法
from common.commons import (
    http_response,
    save_files
)

#从配置文件中导入错误码
from conf.base import (
    ERROR_CODE,
    SERVER_HEADER
)
  
 
########## Configure logging #############
logFilePath = "log/upload/upload.log"
logger = logging.getLogger("Upload")  
logger.setLevel(logging.DEBUG)  
handler = TimedRotatingFileHandler(logFilePath,  
                                   when="D",  
                                   interval=1,  
                                   backupCount=30)  
formatter = logging.Formatter('%(asctime)s \
%(filename)s[line:%(lineno)d] %(levelname)s %(message)s',)  
handler.suffix = "%Y%m%d"
handler.setFormatter(formatter)
logger.addHandler(handler)
 
 
class UploadFileHandle(tornado.web.RequestHandler):
    """handle /upload/file request, upload image and save it to static/image/
    :param image: upload image
    """
        
    def post(self):
        try:
            #获取入参
            image_metas = self.request.files['image']
        except:
            #获取入参失败时，抛出错误码及错误信息
            logger.info("UploadFileHandle: request argument incorrect")
            http_response(self, ERROR_CODE['1001'], 1001)
            return 
            
        image_url = ""
        image_path_list = []
        if image_metas:
            #获取当前的路径
            pwd = os.getcwd()
            save_image_path = os.path.join(pwd, "static/image/")
            logger.debug("UploadFileHandle: save image path: %s" %save_image_path)
            file_name_list = save_files(image_metas, save_image_path)
            image_path_list = [SERVER_HEADER + "/static/image/" + i for i in file_name_list]
            ret_data = {"imageUrl": image_path_list}
            #返回图片下载地址给客户端
            self.write(json.dumps({"data": {"msg": ret_data, "code": 0}}))
        else:
            logger.info("UploadFileHandle: image stream is empty")
            http_response(self, ERROR_CODE['2001'], 2001)