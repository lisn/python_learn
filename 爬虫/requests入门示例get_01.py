
import requests

requeryContent = input("plase input search content:")

url = f"https://www.baidu.com/s?wd={requeryContent}"


headers = {
    "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36 Edg/131.0.0.0"
}

rsp = requests.get(url,headers=headers)

print(f'{type(rsp)} : {rsp}')

print(rsp.text)

rsp.close()