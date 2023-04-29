import math, random, time, hashlib, requests, re
from lxml import etree

from scrapy import Spider

class Crawl():
    def __init__(self):
        self.url = "https://osv.dev/list?"
        self.ivtrurl = "https://www.yetimall.fun/public/home/WxStore/getGoodsInfo?id=3502&userId=0"
        self.cookies = {
            '_ga': 'GA1.1.1349455576.1677737212',
            '_ga_ZXG9G6HTBR': 'GS1.1.1678722653.7.1.1678722664.0.0.0',
        }
        self.headers = {
            'authority': 'osv.dev',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ja;q=0.5',
            'cache-control': 'max-age=0',
            # 'cookie': '_ga=GA1.1.1349455576.1677737212; _ga_ZXG9G6HTBR=GS1.1.1678722653.7.1.1678722664.0.0.0',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
            'sec-ch-ua-arch': '"x86"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-full-version-list': '"Chromium";v="110.0.5481.192", "Not A(Brand";v="24.0.0.0", "Microsoft Edge";v="110.0.1587.69"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-ch-ua-wow64': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69',
        }

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
        i = 1
        while i < 250:
            if i % 40 == 0:
                print(i)
            params = {
                'page': i,
            }
            try:
                res = requests.get(self.url, params=params, headers=headers)
                html = etree.HTML(res.text)
            # ids = html.xpath('//span[@role="cell"]/a')
            # for id in ids:
            #     print(id.xpath('./text()'))
                ids += html.xpath('//span[@role="cell"]/a/text()')
                ls = html.xpath('//span[@role="cell"]/a/text()')
                if len(str(ls)) == 2:
                    print(res.text)
                    print(i)
            # print(html.xpath('//span[@role="cell"]/a/text()'))
                else:
                    with open("osvlst-all0.txt", 'a') as f:
                        f.write(str(html.xpath('//span[@role="cell"]/a/text()')))
                        f.write("\n")
                    i += 1
            except:
                print(i)

s = Crawl()
params = s.spider()