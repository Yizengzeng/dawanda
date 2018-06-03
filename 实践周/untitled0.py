# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 11:28:49 2018

快捷键，字体放大：Ctrl和+
新建文件：Ctrl new

保存

@author: lenovo
"""
a=3
#一次申明多个变量
xuan,guibin,xixi=80,90,88
xj='xiaojiao'
yanzhi=5.0

b=str(yanzhi)
b
print(xj+b)
c='3.9'
d=float(c)
print(xj+'\t'+b)
#字符串中出现{}大括号，表示占位符
print('今天温度是{}天气是{}今天星期{}'.format(10,'小雨','六'))
#列表list
usemoney=10,20,30,40,50
usemoney[1]
usemoney2=[10,20,30,40,50]
print(usemoney2[0])

a=['星期一','星期二','星期三','星期四','星期五','星期六','星期天']
b=[]
print(a)
if a[5]=='星期六':
    print('今天是{}'.format('星期六')) 
    print(a[0]);print(a[1]);print(a[2]);print(a[3]);print(a[4]);print(a[6])
    del a[-2]
    print(a)








