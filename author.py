from selenium import webdriver
from lxml import etree
import re

class author(object):
    def __init__(self):
        self.name=''
        self.love=[]
        self.quan=0
        self.rellove=[]
        self.dizhi=''

    def love_music(self):
        web = webdriver.Firefox()
        web.get(self.dizhi)
        web.switch_to.frame(web.find_element_by_tag_name("iframe"))
        r = web.page_source
        web.close()
        html = etree.HTML(r)
        self.name=html.xpath('//*[@class="name"]/a/text()')
        self.love=re.findall('song\?id=[0-9]+',r)
    def suanquan(self,p):
        n=0
        m=int(len(p))+int(len(self.love))
        for i in p:
            if i in self.love:
                n+=1
        self.quan=n/m


if __name__ == '__main__':
    author
