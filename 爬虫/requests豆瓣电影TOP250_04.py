
import requests


url = "https://movie.douban.com/top250"


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}


#url + parm 才是真正的 url=https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20

resp = requests.get(url,headers=headers)

print(resp.url)

# print(resp.json())


resp.close()