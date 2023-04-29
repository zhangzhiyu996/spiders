import math, random, time, hashlib, requests, re
from lxml import etree

from scrapy import Spider

def gethref(a):
    return a.get('href')

class Crawl():
    def __init__(self):
        self.url = "https://security.snyk.io/vuln/"

    def spider(self):
        ids = []
        for i in range(1, 31):
            if i % 10 == 0:
                print(i)
            res = requests.get(self.url+str(i))
            html = etree.HTML(res.text)
            # ids = html.xpath('//span[@role="cell"]/a')
            # for id in ids:
            #     print(id.xpath('./text()'))
            ids += map(gethref, html.xpath('//a[@data-snyk-test="vuln table title"]'))
            # print(html.xpath('//span[@role="cell"]/a/text()'))
        with open("snyklst.txt", 'w') as f:
            f.write(str(ids))

s = Crawl()
params = s.spider()