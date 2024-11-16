import re


#元字符
#.表示任意一个字符，除了\n
print('.的匹配',re.match('.','938'))
print('.的匹配',re.match('.','$938'))
print('.的匹配',re.match('.','&938'))
print('.的匹配',re.match('.','\n')) # None
#None
print('.的匹配',re.match('.','''
'''))


#\d表示0-9之间任意一个数字
#下面是匹配第一个字符是否是数字
print(r'\d的匹配',re.match(r'\d','093883'))

#\D 非数据的任意一字符
#下面是匹配第一个字符是否不是数字
print(r'\D的匹配',re.match(r'\D','ie7723'))

#\s 表示空白字符 \n \t 及空格
print(r'\s的匹配',re.match(r'\s','\n'))
print(r'\s的匹配',re.match(r'\s','\t'))
print(r'\s的匹配',re.match(r'\s','  '))

#\S 表示非空白字符 除\n \t 及空格之外的字符
print(r'\S的匹配',re.match(r'\S','\n'))
print(r'\S的匹配',re.match(r'\S','\t'))
print(r'\S的匹配',re.match(r'\S','\\'))
print(r'\S的匹配',re.match(r'\S','  '))

#w大小写字母，数字，下划线
print(r'\w的匹配',re.match(r'\w','A'))
print(r'\w的匹配',re.match(r'\w','a'))
print(r'\w的匹配',re.match(r'\w','32'))
print(r'\w的匹配',re.match(r'\w','_'))
#W 除大小写字母，数字，下划线之外的字符
print(r'\W的匹配',re.match(r'\W','A'))
print(r'\W的匹配',re.match(r'\W','a'))
print(r'\W的匹配',re.match(r'\W','32'))
print(r'\W的匹配',re.match(r'\W','_'))
print(r'\W的匹配',re.match(r'\W',' '))