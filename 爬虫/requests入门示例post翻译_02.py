import time

import requests


url = "http://fanyi.baidu.com/sug"


headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}

word = input("please input a word:")

data = {
    "kw":word
}

#目前没有办法解决这个问题
resp = requests.post(url,data=data,headers=headers)
print(resp.json()) #{'errno': 1022, 'errmsg': '访问出现异常，请刷新后重试！', 'logid': 1338515610, 'error': 1022, 'errShowMsg': '访问出现异常，请刷新后重试！'}

resp.close()