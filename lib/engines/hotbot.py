#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import my_enumerator
from bs4 import BeautifulSoup

class Hotbot_enum(my_enumerator.Enumrator_base_threaded):

    '''
    hotbot 搜索引擎
    www.hotbot.com
    '''

    def __init__(self,options,q=None):
        super(Hotbot_enum, self).__init__(options,q=q)
        self.base_url = 'https://www.hotbot.com/web?q={}&offset={}'
        self.headers = {
            'Host':'www.hotbot.com',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Upgrade-Insecure-Requests':'1',
        }
        self.q = q

    def _get_page(self):
        pages = []
        for pn in range(0,(self.page-1)*10,10):
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
        div_tags = soup.find_all('div', 'site-title')
        for div_tag in div_tags:
            for a_tag in div_tag:
                url = a_tag['href']
                self.urls.append(url)
                print '[-]Hotbot: ' + url