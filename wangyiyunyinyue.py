import re
import time

from selenium import webdriver
from author import author


def get_id(url):
    web = webdriver.Firefox()
    web.get(url)
    web.switch_to.frame(web.find_element_by_tag_name("iframe"))
    html = ''
    last_id = []
    midder = ['suiyi']
    id_list = []
    while midder != id_list:
        midder = id_list
        html = web.page_source
        time.sleep(2)
        web.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        last_page = web.find_element_by_link_text('下一页')
        id = re.findall('home\?id=\d+"', html)
        print(set(id))
        id_list = id
        for i in list(set(id)):
            url1 = 'http://music.163.com/#/user/' + i[:-1]
            web2 = webdriver.Firefox()
            web2.get(url1)
            web2.switch_to.frame(web2.find_element_by_tag_name("iframe"))
            html = web2.page_source
            love_id = re.findall('href="(.*?)喜欢的音乐', html)
            if love_id == []:
                continue
            love_id = re.findall('\d+', love_id[0])
            print(love_id)
            web2.close()
            last_id.append(love_id[0])
        try:
            last_page.click()
        except:
            break
    web.close()
    return last_id


a = author()
a.dizhi = 'http://music.163.com/#/playlist?id=133998351'  #被推荐人网易云音乐主页地址
a.love_music()
print(a.love)
str = 'http://music.163.com/#/playlist?id='
l1 = get_id('http://music.163.com/#/user/follows?id=109538358')  #被推荐人关注的人页面的地址
l1.append(get_id('xxxxxxxxxxxxxx'))    #关注的人页面地址，我一般只用我关注的人的地址
# l1 = ['622800043']
l = []
for i in l1:
    if i not in l:
        l.append(i)
s = []
for i in l:
    b = author()
    b.dizhi = str + i
    print(b.dizhi)
    b.love_music()
    b.suanquan(a.love)
    print(b.quan)
    for j in b.love:
        if j not in a.love:
            b.rellove.append([j, b.quan])
    print(b.name, b.love)
    s.append(b)
t = []
z = []
for i in s:
    for j in i.rellove:
        if j[0] not in t:
            t.append(j[0])
            z.append(j)
        else:
            z[t.index(j[0])][1] += j[1]

L = sorted(z,key=lambda x:x[1])[-20:]
for i in L:
    print(i[0])
