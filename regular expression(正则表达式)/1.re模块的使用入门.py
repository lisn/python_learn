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