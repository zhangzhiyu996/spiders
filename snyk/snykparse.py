from selenium import webdriver
import math, random, time, hashlib, requests, re
from lxml import etree

from scrapy import Spider

def gethref(a):
    return a.get('href')

class Crawl():
    def __init__(self):
        self.url = "https://security.snyk.io/"

    def spider(self):
        txt = {}
        #b = webdriver.Chrome()
        with open("snyklst.txt", "r", encoding="utf-8") as f:
            f.read()
        vul = "vuln/SNYK-PYTHON-ESQREPY-3351843"
        vul = "vuln/SNYK-UNMANAGED-ENZO1982MP4V2-3363255"
        # b.get(self.url + vul)
        # button = b.find_element_by_class('vue--button vue--button--link see-all')
        # button.click()
        # content = b.page_source
        # print(content)
        res = requests.get(self.url + vul)
        html = etree.HTML(res.text)
        txt['id'] = vul[5:]
        txt['vulnerability'] = html.xpath('string(//h1[@class="vue--heading title"]/text())').strip()
        tmp = html.xpath('//a[@class="vue--anchor"]/text()')
        txt['cve'] = "CVE not available"
        txt['affects'] = "Unmanaged(C/C++)"
        txt['cwe'] = "CWE unknown"
        for t in tmp:
            if 'CVE' in t:
                txt['cve'] = t
            elif 'CWE' in t:
                txt['cwe'] = t
            else:
                txt['affects'] = t
        try:
            if txt['affects'] == 'Unmanaged(C/C++)':
                txt['affects'] += "::" + html.xpath('//span[@class="vue--anchor"]/text()')[0]
        except:
            print(vul)
        txt['versions'] = map(str.strip, html.xpath('//strong[@data-snyk-test="vuln versions"]/text()'))
        txt['vulscore'] = [i.get("data-snyk-test-score") for i in html.xpath('//div[@data-snyk-test="severity widget score"]')]
        try:
            txt['vullevel'] = html.xpath('//span[@class="vue--badge__text"]/text()')[0].strip()
        except:
            txt['vullevel'] = 'unknown'
        blocks = html.xpath('//div[@class="vue--markdown-to-html markdown-description"]')
        try:
            txt['howtofix'] = blocks[0].xpath('string(p)')
        except:
            txt['howtofix'] = 'unknown'
        try:
            txt['overview'] = blocks[1].xpath('string(p)')
        except:
            txt['overview'] = 'unknown'
        try:
            txt['references'] = blocks[2].xpath('ul/li/a/@href')
            txt['refdescription'] = blocks[2].xpath('ul/li/a/text()')
        except:
            txt['references'] = ['unknown']
            txt['refdescription'] = ['unknown']
        txt['exploitmaturity'] = html.xpath('string(//div[@data-snyk-test="CvssDetailsItem: Exploit Maturity"]/span/strong/text())').strip()
        txt['attackcomplexity'] = html.xpath('string(//div[@data-snyk-test="CvssDetailsItem: Attack Complexity"]/span/strong/text())').strip()
        #txt['attackvector'] = map(str.strip, html.xpath('//div[@data-snyk-test="CvssDetailsItem: Attack Vector"]/span/strong/text()'))
        txt['snykid'] = html.xpath('string(//li[@label="snyk-id"]/strong/text())')
        txt['published'] = html.xpath('string(//li[@label="published"]/strong/text())')
        txt['disclosed'] = html.xpath('string(//li[@label="disclosed"]/strong/text())')
        txt['credit'] = html.xpath('string(//li[@label="credit"]/strong/text())')
        print(txt)
            # with open("snyklst" + v + ".txt", 'w') as f:
            #     f.write(str(ids))

s = Crawl()
params = s.spider()