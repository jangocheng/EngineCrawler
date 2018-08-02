#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import my_enumerator
from bs4 import BeautifulSoup

class Teoma_enum(my_enumerator.Enumrator_base_threaded):

    '''
    Teoma搜索引擎
    '''

    def __init__(self,options,q=None):
        super(Teoma_enum,self).__init__(options,q=q)
        self.headers = {
            'Host':'www.teoma.com',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        }
        self.base_url = 'http://www.teoma.com/web?q={}&page={}'
        self.q =q

    def _get_page(self):
        pages = []
        for pn in range(1,self.page,1):
            pages.append(pn)
        return pages

    def send_request(self):
        pages = self._get_page()
        for pn in pages:
            url = self.base_url.format(self.search_rules,pn)
            try:
                response = self.session.get(url, headers=self.headers, timeout=self.timeout)
            except Exception:
                pass
            else:
                self._extract_url(response)
        return self.urls

    def _extract_url(self,resp):
        soup = BeautifulSoup(resp.text, "lxml")
        cite_tags = soup.find_all('cite', 'algo-display-url')
        for cite_tag in cite_tags:
            url = cite_tag.get_text()
            self.urls.append(url)
            print '[-]Teoma: ' + cite_tag.get_text()