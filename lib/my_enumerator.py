#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import requests
import threading
import multiprocessing

class Enumrator_base(object):

    '''最基础的搜索引擎枚举器'''

    def __init__(self,options):
        self.session = requests.Session()
        self.headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        }
        self.timeout = 25
        self.search_rules = options.rule
        self.page = options.page
        self.base_url = ''
        self.urls = []

    # 要抓取的网页
    def _get_page(self):
        '''子类应重写这个方法'''
        return

    # 发送http
    def send_request(self):
        '''子类应重写这个方法'''
        return

    # 提取url
    def _extract_url(self,resp):
        '''子类应重写这个方法'''
        return

    # 检查http返回错误
    def _check_response_errors(self,resp):
        '''子类应重写这个方法'''
        return

    # 延时请求以避免被机器人检测
    def _should_sleep(self):
        sleep(2)
        return

class Enumrator_base_threaded(multiprocessing.Process,Enumrator_base):

    '''多进程枚举器'''

    def __init__(self,options,lock=threading.Lock(),q=None):
        Enumrator_base.__init__(self,options)
        multiprocessing.Process.__init__(self)
        self.lock = lock
        self.q = q

    def run(self):
        url_list = self.send_request()  # 实例通过调用start()方法，自动调用run()方法
        for url in url_list:
            self.q.append(url)