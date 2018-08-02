#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

def parse_args():

    '''命令行解释器'''

    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -e baidu,yahoo -r 'inurl:php?id=1' -p 10 -o urls.txt")
    parser._optionals.title = "OPTIONS"
    parser.error = parser_error
    parser.add_argument('-r', '--rule', help="Engine advanced search rules", required=True)
    parser.add_argument('-p', '--page', help="The number of pages returned by the search engine", required=True,type=int)
    parser.add_argument('-e', '--engines', help='Specify a comma-separated list of search engines')
    parser.add_argument('-o', '--output', help='Save the results to text file')
    return parser.parse_args()

def banner():
    print """
 _____             _             ____                    _           
| ____|_ __   __ _(_)_ __   ___ / ___|_ __ __ ___      _| | ___ _ __ 
|  _| | '_ \ / _` | | '_ \ / _ \ |   | '__/ _` \ \ /\ / / |/ _ \ '__|
| |___| | | | (_| | | | | |  __/ |___| | | (_| |\ V  V /| |  __/ |   
|_____|_| |_|\__, |_|_| |_|\___|\____|_|  \__,_| \_/\_/ |_|\___|_|   
             |___/   
                # Coded By Farmsec - @answer
    """

def parser_error(errmsg):
    banner()
    print "Usage: python " + sys.argv[0] + " [Options] use -h for help"
    print "Error: " + errmsg
    sys.exit()