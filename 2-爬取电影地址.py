# 技术点 resp.encoding = 'gb2312'


import requests
import re

domain="https://www.dytt8.net/index.htm"
domain2="https://www.dytt8.net/"
resp=requests.get(domain)
resp.encoding = 'gb2312'
# print(resp.text)

# 定位到最新影片推荐
obj1=re.compile(r"最新影片推荐.*?<ul>(?P<ul>.*?)</ul>",re.S)
# 提取子页面
obj2=re.compile(r"<a href='(?P<herf>.*?)'",re.S)
#
obj3=re.compile(r'◎片　　名　(?P<movie>.*?)<br />.*?<a.*? href="(?P<download>.*?)">',re.S)
#
obj4=re.compile(r'◎片　　名　(?P<movie>.*?)</div>.*?<div><a href="(?P<download>.*?)">',re.S)


result1= obj1.finditer(resp.text)
child_herf_list = []
for it in result1:
    ul=it.group('ul')
    result2 = obj2.finditer(ul)
    for itt in result2:
        # 拼接页面url链接 域名+子页面链接
        child_herf=domain2+itt.group('herf').strip("/")
        child_herf_list.append(child_herf)

# 获取子页面内容
for href in child_herf_list:
    child_resp= requests.get(href)
    child_resp.encoding ='gb2312'
    # print(child_resp.text)
    try:
        result3 = obj3.search(child_resp.text)
        print(result3.group("movie"))
        print(result3.group("download"))
    except Exception as e:
        result4=obj4.search(child_resp.text)
        print(result4.group("movie"))
        print(result4.group("download"))


