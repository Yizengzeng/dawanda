# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:50:01 2018

@author: lenovo
"""

import urllib.request as a
city_pinyin=input("请输入城市：")
url='http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
info=a.urlopen(url.format(city_pinyin)).read().decode('utf-8','ignor')
#print(info)
import json
data=json.loads(info)
print("七天天气情况")
a=[1,2,3,4,5,6,7]
for i in a:
    q={"日期：":data['list'][i]['dt_txt'],
       "天气：":data['list'][i]['weather'][0]['description'],
       "最低温度：":data['list'][i]['main']['temp_min'],
       "最高温度：":data['list'][i]['main']['temp_max'],
       "气压：":data['list'][i]['main']['pressure']}
    print("{}\n天气:{}\n最低温度：{}\n最高温度：{}\n气压：{}".format(q["日期："],q["天气："],q["最低温度："],q["最高温度："],q["气压："]))

