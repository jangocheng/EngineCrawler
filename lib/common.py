#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def write_file(filename,results_urls):
    # 将url保存到文件
    print "[*] Saving results to file: %s" % filename
    with open(str(filename), 'at') as f:
        for url in results_urls:
            f.write(url + os.linesep)