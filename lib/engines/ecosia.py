#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import my_enumerator
from bs4 import BeautifulSoup
from urllib import quote

class Ecosia_enum(my_enumerator.Enumrator_base_threaded):

    '''
    Ecosia搜索引擎
    www.ecosia.org
    '''

    def __init__(self,options,q=None):
        super(Ecosia_enum,self).__init__(options,q=q)
        self.headers = {
            'Host':'www.ecosia.org',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        }
        self.base_url = 'https://www.ecosia.org/search?p={}&q={}'
        self.search_rules = quote(self.search_rules)  # 将传入搜索引擎的参数进行url编码以避免被机器人检测
        self.q = q

    def _get_page(self):
        pages = []
        for pn in range(0,self.page,1):
            pages.append(pn)
        return pages

    def send_request(self):
        pages = self._get_page()
        for pn in pages:
            url = self.base_url.format(pn,self.search_rules)
            try:
                response = self.session.get(url, headers=self.headers, timeout=self.timeout)
            except Exception:
                pass
            else:
                self._extract_url(response)
        return self.urls

    def _extract_url(self, resp):
        soup = BeautifulSoup(resp.text, "lxml")
        a_tags = soup.find_all('a', 'result-url js-result-url')
        for a_tag in a_tags:
            url = a_tag['href']
            self.urls.append(url)
            print '[-]Ecosia: ' + url
