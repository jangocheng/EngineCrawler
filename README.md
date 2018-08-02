# EngineCrawler:
EngineCrawler 主要用于抓取国内外一些主流搜索引擎搜索返回的url内容，目前支持以下的搜索引擎： baidu，google，yahoo，ecosia，teoma，360，hotbot，脚本支持直接使用百度或者谷歌的高级搜索语法来进行搜索，谷歌搜索引擎不需要翻墙，抓取的是国内镜像站的数据。
# Dependencies
`pip -r install requirements.txt`
# Usage:
`usage: EngineCrawler.py [-h] -r RULE -p PAGE [-e ENGINES] [-o OUTPUT]

OPTIONS:
  -h, --help            show this help message and exit
  -r RULE, --rule RULE  Engine advanced search rules
  -p PAGE, --page PAGE  The number of pages returned by the search engine
  -e ENGINES, --engines ENGINES
                        Specify a comma-separated list of search engines
  -o OUTPUT, --output OUTPUT
                        Save the results to text file

Example: python EngineCrawler.py -e baidu,yahoo -r 'inurl:php?id=1' -p 10 -o
urls.txt
`
# Screenshot:
![avatar](https://github.com/heroanswer/EngineCrawler/blob/master/screenshot.png)
