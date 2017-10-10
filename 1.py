#-*-coding:utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

import builtwith
def get_method_from_html(url):
    ji_shu = builtwith.parse(url)
    print url + "所用到的网络技术是:", ji_shu


if __name__ == '__main__':
    url = raw_input("输入网址:  ")
    get_method_from_html(url)