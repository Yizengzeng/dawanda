# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 15:08:26 2018

@author: lenovo
"""

#字典
msg={"地址":"绵阳三台",
 "手机号码":"123456",
 "寄信人":"是我"}
print(msg["地址"])
print(msg["手机号码"])
print(msg["寄信人"])

mas={"姓名":"外卖",
     "身高":"180",
     "性别":"男",
     "年龄":"19"}
print(mas["姓名"])
print(mas["身高"])
print(mas["性别"])
print(mas["年龄"])

xue={"name":"天苍苍",
     "songs":["野茫茫","莫说话"],
     'saa':["a","b","c"]}
songs=xue['songs']
print(songs)
print("歌曲总数："+str(len(songs)))
print(max(xue['saa']))

ao={'未来五天天气':['晴天','雨','小雨','多云','阵雨'],
        '未来五天气温':[10,12,15,6,22],
        '星期':['1','2','3','4','5','6','7']}
print(max(ao['未来五天气温']))
print(ao['未来五天天气'])

city_pinyin=input("请输入城市拼音：")
print(city_pinyin)

address='http://api.openweathermap.org/data/2.5/weather?q=meishan&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996 '
print(address.format(city_pinyin))


menno=input("请输入菜单：")

if menno=='1':
    print("1.查看当前城市天气")
if menno=="2":
    print("2.查看其它城市天气")
if menno=='3':
    print("3.保存当前城市")    
        
   #联网 
import urllib.request as r
city_pinyin=input("请输入城市拼音：")
address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996 '
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignor')
#print(info)

#json(dict)格式
import json
data=json.loads(info)
data['main']['temp']

q={'weather':data['weather'][0]['description'],
   'temp_max':data['main']['temp_max'],
   'pressure':data['main']['pressure']}
print(q)


import urllib.request as a
url='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'







