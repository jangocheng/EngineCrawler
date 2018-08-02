#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import my_enumerator
from bs4 import BeautifulSoup

class Google_enum(my_enumerator.Enumrator_base_threaded):

    '''
    谷歌搜索引擎
    answer.run
    谷歌在国内被墙掉了，抓取镜像站的数据
    '''
    def __init__(self,options,q=None):
        super(Google_enum,self).__init__(options,q=q)
        self.base_url = 'http://google.answer.run/search?q={}&start={}'
        self.headers = {
            'Host':'google.answer.run',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Upgrade-Insecure-Requests':'1',
        }
        self.q = q

    def _get_page(self):

        pages = []
        for pn in range(0,(self.page -1 ) * 10,10):
            pages.append(pn)
        return pages

    def send_request(self):
        pages = self._get_page()
        for pn in pages:
            url = self.base_url.format(self.search_rules,pn)
            try:
                response = self.session.get(url,headers=self.headers,timeout=self.timeout)
                self._should_sleep()
            except Exception:
                pass
            else:
                self._extract_url(response)
        return self.urls

    def _extract_url(self,resp):
        soup = BeautifulSoup(resp.text, "lxml")
        cite_tages = soup.select("h3 a")
        for cite_tage in cite_tages:
            url = cite_tage['href']
            if url.startswith('http') or url.startswith('https'):
                self.urls.append(url)
                print '[-]Google: ' + url
            else:
                pass

    def _check_response_errors(self,resp):
        if 'Our systems have detected unusual traffic' in resp:
            print '[!] Error Google probably now is blocking our requests'
            print '[~] Finished now the Google Enumeration ......'
            return False
        return True