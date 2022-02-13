from urllib.request import urlretrieve
import os

#第一題
# url = urlretrieve("https://www.w3.org/TR/PNG/iso_8859-1.txt","Homework.txt")



# 第二題
# 要檢查的檔案路徑
# filepath = "C:/Users/admin/Desktop/push_to_github/reptile_marathon/Data/Homework.txt"

# # 檢查檔案是否存在
# if os.path.isfile(filepath):
#   print("檔案存在。")
# else:
#   print("檔案不存在。")

#第三題
# test = open("Homework.txt","w")
# test.write("Hello World")
# test.close()

# 第四題
# file = open("Homework.txt","r") 
# for i in file:  
#     if len('Hello World') == len(i):
#         print('[O] 檢查 Homework.txt 檔案字數是否符合 Hello World 字數')
#     else:
#         print('[X] 檢查 Homework.txt 檔案字數是否符合 Hello World 字數')