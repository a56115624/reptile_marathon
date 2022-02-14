# ## 作業目標

# 利用 Request + BeatifulSoup 爬取下列兩個網站內容並解析：

# 1. Dcared 網址： https://www.dcard.tw/f
# 2. 知乎： https://www.zhihu.com/explore

# 並且回答下面問題：

# 1. Request 取回之後該怎麼取出資料，資料型態是什麼？

import requests
from bs4 import BeautifulSoup

print('Request 取回之後該怎麼取出資料，資料型態是什麼？ =>')

r1 = requests.get("https://www.dcard.tw/f")
r1.encoding = 'utf-8'
r2 = r1.text


print("資料的型態",type(r2))
print("Type of r.text is", type(r1.text))


# 2. 為什麼要使用 BeatifulSoup 處理？處理後的型態是什麼？

import encodings
import requests
from bs4 import BeautifulSoup


r1 = requests.get("https://www.dcard.tw/f")
r1.encoding = 'utf-8'
r2 = r1.text
soup = BeautifulSoup(r2,"html.parser")
# print(soup)
print(type(soup))

#處理後的型態為 class


# 3. 觀察一下知乎回來的資料好像有點怪怪的，該怎麼解決？
# 加入headers

r1 = requests.get("https://www.zhihu.com/explore",
headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"})

soup = BeautifulSoup(r1.text,"html.parser")
print(soup)

