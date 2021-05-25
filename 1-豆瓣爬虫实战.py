# 技术点：csv去空格newline=''


import requests
import re
import csv
# 指定url
url="https://movie.douban.com/top250"
# UA伪装
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
}
# 发送请求
resp=requests.get(url,headers=headers)
page_content=resp.text
# 解析数据
obj =re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span '
                r'class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                r'<span>(?P<num>.*?)人评价</span>', re.S)
# 开始匹配 re.finditer()返回的是一个迭代器，需要对其进行遍历，才能获取数据
result=obj.finditer(page_content)
f = open('../../data.csv', mode="w", newline='')
csvwriter=csv.writer(f)
for it in result:
    # group() 在正则表达式中用于获取分段截获的字符串
    # print(it.group("name"))
    # print(it.group("score"))
    # print(it.group("num"))
    # print(it.group("year").strip())
    dic =it.groupdict()  # 转化为字典格式
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())

f.close()
print('over!')
