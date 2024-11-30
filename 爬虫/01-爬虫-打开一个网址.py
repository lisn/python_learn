
from urllib.request import urlopen


url="http://www.baidu.com/"

rsp = urlopen(url)

content = rsp.read().decode("utf-8")

# print(content.decode("utf-8"))

with open("baidu.html","w",encoding="utf-8") as fp:
    fp.write(content)

print("over")