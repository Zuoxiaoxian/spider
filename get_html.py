#-*-coding:utf-8 -*-
import sys
import urllib2
from fake_useragent import UserAgent
reload(sys)
sys.setdefaultencoding("utf-8")

def get_first_html(url, num_trings=2):
    '''
    :param url: 首页url
    :param num_trings:如果是500-600服务器错误,就尝试几次
    :return:
    '''
    ua = UserAgent()
    headers = {
        "User-Agent": ua.random,
    }
    handler = urllib2.HTTPHandler()
    opener = urllib2.build_opener(handler)
    request = urllib2.Request(url, headers=headers)
    try:
        response = opener.open(request)
        html = response.read()
    except urllib2.URLError as e:
        print '网址错误!',e
        if hasattr(e, 'code') and 500 <= e.code <= 600:
            return get_first_html(url, num_trings-1)
        html = None
    print html
    return html

if __name__ == '__main__':
    url = "http://www.baidu.com"
    get_first_html(url)