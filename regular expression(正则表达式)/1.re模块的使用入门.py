'''
import re
可以通过dir(re) 可以相应的函数
主要函数match findall的使用
'''

import re
str = 'abcd'
pattern = 'ab'

res = re.match(pattern,str)
print(res)
print(res.group())
print(re.findall(pattern,str))



print('******************************findall*********************************')
#findall 匹配字符串中所有的符合正则的内容  返回一个列表  不常用

lst = re.findall(r'\d+','我的电话是：123456666，我老婆的电话是：24324345354')
print(lst)


print('******************************finditer*********************************')
#finditer 匹配字符串中所有的符合正则的内容  返回一个迭代器  从迭代器中拿到内容需要.group()

it = re.finditer(r'\d+','我的电话是：123456666，我老婆的电话是：24324345354')
print(it)
for i in it:
    print(i.group())

print('******************************search*********************************')
#search 找到一个结果就返回  返回的结果是match对象  拿到内容需要.group()
s = re.search(r'\d+','我的电话是：123456666，我老婆的电话是：24324345354')
print(s.group())


print('******************************match*********************************')
#match 从头开始查找，找到一个结果就返回  返回的结果是match对象  拿到内容需要.group()
s = re.match(r'\d+','我的电话是：123456666，我老婆的电话是：24324345354')
# print(s.group())    #会报错，AttributeError: 'NoneType' object has no attribute 'group'
# print(dir(s))

s = re.match(r'\d+','123456666，我老婆的电话是：24324345354')
print(s.group())
# print(dir(s))


#预加载正则表达式

print('******************************预加载 finditer*********************************')
obj = re.compile(r'\d+')

it = obj.finditer('我的电话是：123456666，我老婆的电话是：24324345354')
for i in it:
    print(i.group())

print('******************************预加载 findall*********************************')
lst = obj.findall('我的电话是：123456666，我老婆的电话是：24324345354')
print(lst)


print('******************************预加载 finditer re.S (?P<命名>正则表达式)分组*********************************')
s='''
<div class='jay'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>宋铁</span></div>
<div class='jolin'><span id='3'>大聪明</span></div>
<div class='sylar'><span id='4'>范思哲</span></div>
<div class='tory'><span id='5'>胡说八道</span></div>
'''
#re.S 让.可以匹配任意一字符，包括换行符
# () 为正则表达式进行分组,并可以给分组进行命名 (?P<命名>正则表达式)
obj = re.compile(r"<div class='.*?'><span id=(?P<id>'\d+')>(?P<name>.*?)</span></div>",re.S)

it = obj.finditer(s)
for i in it:
    print(i.group('id'), '->', i.group('name'))

