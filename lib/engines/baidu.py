#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import my_enumerator
from bs4 import BeautifulSoup

class Baidu_enum(my_enumerator.Enumrator_base_threaded):

    '''
    百度搜索引擎
    www.baidu.com
    '''

    def __init__(self,options,q=None):
        super(Baidu_enum, self).__init__(options,q=q)
        self.base_url = 'https://www.baidu.com/s?wd={}&pn={}'
        self.q = q

    def _get_page(self):

        '''获取要爬取的网页数量'''

        pages = []
        for pn in range(0,(self.page - 1) * 10,10):
            pages.append(pn)
        return pages

    def send_request(self):
        pages = self._get_page()
        for pn in pages:
            url = self.base_url.format(self.search_rules,pn)
            try:
                response = self.session.get(url,headers=self.headers,timeout=self.timeout)
            except Exception:
                pass
            else:
                self._extract_url(response)
        return self.urls


    def _extract_url(self,resp):

        '''从返回的html中提取url'''

        soup = BeautifulSoup(resp.text, "lxml")
        html_divs = soup.find_all("a", attrs={'data-click': re.compile(r'.'), 'class': None})
        for div in html_divs:
            try:
                response = self.session.get(div['href'], headers=self.headers, timeout=self.timeout)
                if response.status_code == 200:
                    url = response.url
                    self.urls.append(url)
                    print  '[-]Baidu: ' + url
            except Exception:
                pass

if __name__ == '__main__':
    Baidu_enum()