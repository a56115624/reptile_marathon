#比較一下範例檔案中的「r.text」與「json.loads(r.text)」讀出來的內容有什麼差異

# r.text為一維字串型態
# json.loads(r.text)為整理過的串列包覆dict的型態。




# 自行尋找一個合適的 API 接口做練習，並且查看其回傳內容
# https://cat-fact.herokuapp.com/facts (來源：https://alexwohlbruck.github.io/cat-facts/)
# http://odata.wra.gov.tw/v4/RealtimeWaterLevel (來源：https://data.gov.tw/dataset/25768)
import requests
import json
r1 = requests.get("https://cat-fact.herokuapp.com/facts")
# print(r1)
r2 = json.loads(r1.text)
print(r2)