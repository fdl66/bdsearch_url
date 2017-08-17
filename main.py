#!/usr/bin/env python
# coding=utf-8

from pyquery import PyQuery as Pq
import requests
import random
import re
import urllib2


resource_file="blacklist.txt"
search_list = []
search_result = {}

#读取文件，得到搜索列表
def get_search_list():
    f = open(resource_file,'rb')
    for item in f.read().split('\n'):
        if item != '\r':
            search_list.append(item.strip('\r'))

#百度搜索类
class BaiduSearchSpider(object):
    def __init__(self, searchText):
        self.url = "http://www.baidu.com/baidu?wd=%s&tn=monline_4_dg" % searchText
        self.header=['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0', \
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0', \
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ (KHTML, like Gecko) Element Browser 5.0', \
            'IBM WebExplorer /v0.94', 'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)', \
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)', \
            'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14', \
            'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25', \
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36', \
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)']
        self.header_cnt=random.randint(0,8)
        self.headers = {
            "User-Agent": self.header[self.header_cnt]}
        self._page = None
    @property
    def page(self):
        if not self._page:
            r = requests.get(self.url, headers=self.headers)
            r.encoding = 'utf-8'
            self._page = Pq(r.text)
        return self._page

    @property
    def baiduURLs(self):
        return [(site.attr('href'), site.text().encode('utf-8')) for site in
                self.page('div.result.c-container  h3.t  a').items()]

    @property
    def originalURLs(self):
        tmpURLs = self.baiduURLs
        print tmpURLs
        originalURLs = []
        for tmpurl in tmpURLs:
            tmpPage = requests.get(tmpurl[0])
            # tmpPage.encoding = 'utf-8' #这样不好使，print的时候python报错
            tmptext = tmpPage.text.encode('utf-8')
            urlMatch = re.search(r'URL=\'(.*?)\'', tmptext, re.S)
            if not urlMatch == None:
                print urlMatch.group(1), "   ", tmpurl[1]
                originalURLs.append(tmpurl)
            else:
                print "---------------"
                print "No Original URL found!!"
                print tmpurl[0]
                print tmpurl[1]

        return originalURLs


#未完成，得到真实url
def get_true_url(target_url):
    response = urllib2.urlopen(target_url)
    realurl = response.geturl()
    return realurl
    print(realurl)

#开始搜索
def start_search():
    for item in search_list:
        bdsearch=BaiduSearchSpider(item)
        search_result[item]=bdsearch.baiduURLs


def main():
    get_search_list()
    start_search()
    print search_result

if __name__=="__main__":
    main()