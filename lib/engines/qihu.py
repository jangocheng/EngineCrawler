#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib import my_enumerator
from bs4 import BeautifulSoup

class Qihu360_enum(my_enumerator.Enumrator_base_threaded):

    '''
    360搜索引擎
    www.so.com
    '''

    def __init__(self,options,q=None):
        super(Qihu360_enum,self).__init__(options,q=q)
        self.headers = {
            'Host': 'www.so.com',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        }
        self.base_url = 'https://www.so.com/s?q={}&pn={}'
        self.q = q

    def _get_page(self):
        pages = []
        for pn in range(0,self.page,1):
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
        soup = BeautifulSoup(resp.text, 'lxml')
        h3_tags = soup.find_all('h3', "res-title")
        for h3_tag in h3_tags:
            for a_tag in h3_tag:
                try:
                    data_url = a_tag['data-url']
                    print '[-]360: ' + data_url
                    self.urls.append(data_url)
                except TypeError:
                    pass
                except KeyError:
                   # = = 捕获了一个异常 调试代码的时候发现还有一个......
                    try:
                        href_url = a_tag['href']
                        print '[-]360: ' + a_tag['href']  # 现在可以打印获取a_tag['href']中的数据了
                        self.urls.append(href_url)
                    except KeyError:
                       pass