import math, random, time, hashlib, requests, re, json, sys
from lxml import etree

from scrapy import Spider

class Crawl():
    def __init__(self):
        self.url = "https://api.osv.dev/v1/vulns/"
    def spider(self):
        headers = {
            'authority': 'osv.dev',
            'accept': 'text/html, application/xhtml+xml',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ja;q=0.5',
            'referer': 'https://osv.dev/list?',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'turbo-frame': 'vulnerability-table-page2',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
        }
        ids = []
        # for i in range(2792, 3200):
        #     if i % 40 == 0:
        #         print(i)
        with open("osvlst-all5.txt", 'r') as rf:
            for line in rf.readlines():
                for id in line.split(','):
                    sid = id.strip()
                    sid = sid.lstrip('[')
                    sid = sid.rstrip(']')
                    sid = sid.strip("'")
                    try:
                        res = requests.get(self.url + sid, headers=headers)
                    except:
                        print(id)
                        print(1)
                    if '{"code":' in res.text:
                        print(id)
                        print(res.text)
        #html = etree.HTML(res.text)
            # ids = html.xpath('//span[@role="cell"]/a')
            # for id in ids:
            #     print(id.xpath('./text()'))
            #ids += html.xpath('//span[@role="cell"]/a/text()')
            # print(html.xpath('//span[@role="cell"]/a/text()'))
            
                    with open("osvdata-all5.txt", 'a') as f:
                        #text = res.text.replace('\\n', '\n')
                        try:
                            f.write(res.text)
                            pass
                        except:
                            print(id)
                            print(2)
                        f.write("\n")

reload(sys)
sys.setdefaultencoding('utf-8')
s = Crawl()
params = s.spider()