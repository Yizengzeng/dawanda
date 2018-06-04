# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:50:01 2018

@author: lenovo
"""

import urllib.request as a
city_pinyin=input("欢迎使用全球城市气候查询系统\n请输入城市：")
url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996'
info=a.urlopen(url.format(city_pinyin)).read().decode('utf-8','ignor')
#print(info)
import json
data=json.loads(info)

menno=input("查看当前城市请按1，其它数值查看其它城市：")
if menno=='1':
    print("七天天气情况")
    a=range(1,6)
    for i in a:
        a=7*i-6
        q={"日期：":data['list'][a]['dt_txt'],
           "天气：":data['list'][a]['weather'][0]['description'],
           "最低温度：":data['list'][a]['main']['temp_min'],
           "最高温度：":data['list'][a]['main']['temp_max'],
           "气压：":data['list'][a]['main']['pressure']}
        print("{}\n天气:{}\n最低温度：{}\n最高温度：{}\n气压：{}".format(q["日期："],q["天气："],q["最低温度："],q["最高温度："],q["气压："]))
else:
    print("\n查看其它城市天气")
    city_pinyin=input("请输入城市：")
    a=range(1,6)
    for i in a:
        a=7*i-6
        q={"日期：":data['list'][a]['dt_txt'],
           "天气：":data['list'][a]['weather'][0]['description'],
           "最低温度：":data['list'][a]['main']['temp_min'],
           "最高温度：":data['list'][a]['main']['temp_max'],
           "气压：":data['list'][a]['main']['pressure']}
        print("{}\n天气:{}\n最低温度：{}\n最高温度：{}\n气压：{}".format(q["日期："],q["天气："],q["最低温度："],q["最高温度："],q["气压："]))
        
