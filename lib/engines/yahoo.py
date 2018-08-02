#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import unquote
from lib import my_enumerator
from bs4 import BeautifulSoup

class Yahoo_enum(my_enumerator.Enumrator_base_threaded):

    '''
    雅虎搜索引擎
    search.yahoo.com
    '''

    def __init__(self,options,q=None):
        super(Yahoo_enum, self).__init__(options,q=q)
        self.base_url = 'https://search.yahoo.com/search?p={}&b={}'
        self.q = q

    def _get_page(self):

        pages = []
        for pn in range(0,(self.page - 1) * 10,10):
            pages.append(pn)
        return pages

    def send_request(self):
        pages = self._get_page()
        for pn in pages:
            url = self.base_url.format(self.search_rules, pn+1)
            try:
                response = self.session.get(url,headers=self.headers,timeout=self.timeout)
            except Exception:
                pass
            else:
                self._extract_url(response)
        return self.urls

    def _extract_url(self, resp):
        '''
        雅虎搜索返回的url结果：
        yahoo_encryption_url = '
        http://r.search.yahoo.com/_ylt=AwrgDaPBKfdaMjAAwOBXNyoA;_ylu=X3oDMTByb2lvbXVuBGNvbG8DZ3ExBHBvcwMxBHZ0aWQDBHNlYwNzcg--/RV=2/RE=1526176322/RO=10/RU=
        http://berkeleyrecycling.org/page.php?id=1
        /RK=2/RS=6rTzLqNgZrFS8Kb4ivPrFbBBuFs-'
        '''
        soup = BeautifulSoup(resp.text, "lxml")
        try:
            a_tags = soup.find_all("a", " ac-algo fz-l ac-21th lh-24")
            for a_tag in a_tags:
                yahoo_encryption_url = a_tag['href']
                yahoo_decrypt_url = unquote(yahoo_encryption_url)   # 解码
                split_url = yahoo_decrypt_url.split('http://')
                if len(split_url) == 1:
                    result_https_url = 'https://' + split_url[0].split('https://')[1].split('/R')[0] # 获取返回https协议的url
                    self.urls.append(result_https_url)
                    print '[-]Yahoo: ' + result_https_url
                else:
                    result_http_url = 'http://' + split_url[2].split('/R')[0] # 获取返回http协议的url
                    print '[-]Yahoo: ' + result_http_url
                    self.urls.append(result_http_url)
        except Exception:
            pass