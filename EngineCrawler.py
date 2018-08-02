#!/usr/bin/env python
# -*- coding: utf-8 -*-

import multiprocessing

from lib import my_parser
from lib.engines import baidu
from lib.engines import ecosia
from lib.engines import google
from lib.engines import hotbot
from lib.engines import qihu
from lib.engines import teoma
from lib.engines import yahoo

from lib.common import write_file

def main(args_options):
    search_engines = args_options.engines
    output = args_options.output
    urls_queue = multiprocessing.Manager().list()  # url队列

    supported_engines = {
        'baidu':baidu.Baidu_enum,
        'google': google.Google_enum,
        'yahoo': yahoo.Yahoo_enum,
        'ecosia':ecosia.Ecosia_enum,
        'teoma': teoma.Teoma_enum,
        '360':qihu.Qihu360_enum,
        'hotbot':hotbot.Hotbot_enum,
    }
    chosen_enums = []
    if search_engines is None:
        chosen_enums = [
            baidu.Baidu_enum,
            google.Google_enum,
            yahoo.Yahoo_enum,
            ecosia.Ecosia_enum,
            teoma.Teoma_enum,
            qihu.Qihu360_enum,
            hotbot.Hotbot_enum
        ]
    else:
        engines = search_engines.split(',')
        for engine in engines:
            if engine.lower() in supported_engines:
                chosen_enums.append(supported_engines[engine.lower()])  # 选择搜索引擎

    enums = [enum(args_options, q=urls_queue) for enum in chosen_enums]  # 列表生成式生成搜索引擎类的实例
    for enum in enums:
        enum.start()  # 启动搜索引擎爬取url
    for enum in enums:
        enum.join()

    urls = set(urls_queue)  # set对url去重
    write_file(output,urls)

if __name__ == '__main__':
    args = my_parser.parse_args()
    main(args)