## 作業目標

# * 請利用 API: https://www.dcard.tw/_api/forums/pet/posts?popular=true 回答下列問題：

# 1. 這個 API 一次會回傳幾筆資料？每一筆資料包含哪些欄位？
# 2. 取出每一筆資料的「標題」、「貼文時間」、「留言人數」、「按讚人數」
# 3. 計算熱門/非熱門文章的「平均留言人數」與「平均按讚人數」


import requests
r = requests.get('https://www.zhihu.com/api/v4/questions/55493026/answers',headers={"user-agent":"my-app/0.0.1"})
response = r.text
print(response)

# 網站已被修改目前無法使用(作答失敗)