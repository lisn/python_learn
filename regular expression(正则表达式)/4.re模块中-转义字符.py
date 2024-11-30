
import re

print('的匹配',re.match(r'\d',r'\d'))
print('的匹配',re.match('\\d',r'\d'))
print('的匹配',re.match(r'\\\d',r'\d'))
print('的匹配',re.match('\\\\d',r'\d'))


print('的匹配',re.match('\n','\n'))

print(re.match(r'\d','212132'))