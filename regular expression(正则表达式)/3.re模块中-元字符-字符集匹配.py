import re


print('[a-d]的匹配',re.match('[abcd]','ab'))
print('[a-d]的匹配',re.match('[abcd]','ab'))
print('[a-d]的匹配',re.match('[a-d]','zb'))
print('[a-d]的匹配',re.match('[a-d]','zb'))
print('[0-9]的匹配',re.match('[0-9]','232'))
print('[A-Z]的匹配',re.match('[A-Z]','Zb'))
print('[^a-z]的匹配',re.match('[^a-z]','zb'))
print('[0-9a-zA-Z]的匹配',re.match('[0-9 a-z A-Z]','Zb'))
#不在0-9a-zA-Z之内
print('[^0-9a-zA-Z]的匹配',re.match('[^0-9 a-z A-Z]','Zb'))
#下面这种表达是在^0-9 a-z A-Z之内的字符
print('[(^0-9)a-zA-Z]的匹配',re.match('[(^0-9) a-z A-Z]','Zb'))
print('[(^0-9)a-zA-Z]的匹配',re.match('[(^0-9) a-z A-Z]','6Zb'))
print('[(^0-9)a-zA-Z]的匹配',re.match('[(^0-9) a-z A-Z]','^6Zb'))
print('[(^0-9)a-zA-Z]的匹配',re.match('[(^0-9) a-z A-Z]','+6Zb'))


# 任意的字符表示
print('[\w\W]的匹配',re.match('[\w\W]','我+6Zb'))