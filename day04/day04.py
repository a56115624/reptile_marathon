# 請利用 API: https://www.dcard.tw/_api/forums/pet/posts?popular=true 回答下列問題：



# 1. 這個 API 一次會回傳幾筆資料？每一筆資料包含哪些欄位？
# import requests
# import json
# r1 = requests.get("https://www.dcard.tw/_api/forums/pet/posts?popular=true")
# r2 = json.loads(r1.text)
# number = len(r2)
# clum = r2[0].keys()
# print(number,"\n",clum)



# 2. 取出每一筆資料的「標題」、「貼文時間」、「留言人數」、「按讚人數」
# import requests
# import json
# r1 = requests.get("https://www.dcard.tw/_api/forums/pet/posts?popular=true")
# r2 = json.loads(r1.text)
# # print(r2)
# for i in r2:
#     print(i["title"],'\n',"貼文時間",i["createdAt"],"留言人數",i['commentCount'],"按讚人數",i['likeCount'])



# 3. 計算熱門/非熱門文章的「平均留言人數」與「平均按讚人數」
# popular
import json
import requests
r1 = requests.get("https://www.dcard.tw/_api/forums/pet/posts?popular=true")
r2 = json.loads(r1.text)


commentCount_ans = 0
likeCount_ans = 0
for i in r2:
    commentCount_ans = commentCount_ans + i['commentCount']
    likeCount_ans = likeCount_ans + i['likeCount']
# print(commentCount_ans)
print("熱門文章","\n","平均留言人數",commentCount_ans/len(i),"平均按讚人數",likeCount_ans/len(i))

# unpopular
r3= requests.get('https://www.dcard.tw/_api/forums/pet/posts?popular=false')
fresponse = r3.text
fdata = json.loads(fresponse)

fcommentCount = 0
flikeCount = 0
for i in fdata:
    fcommentCount = fcommentCount + i["commentCount"]
    flikeCount = flikeCount+ i["likeCount"]
# print(flikeCount)
print("非熱門文章","\n","平均留言人數",fcommentCount/len(i),"平均按讚人數",flikeCount/len(i))



