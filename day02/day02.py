# Python 下載CSV檔案與解析
# 了解 csv 檔案格式與內容
# 能夠利用套件存取 csv 格式的檔案
# 作業目標
# 比較一下範例檔案中的「File I/O」與「CSV Reader」讀出來的內容有什麼差異

# 根據範例檔案的結果：

# 取出班次一的每一個時間
# 將班次一的每一個時間用一種資料型態保存
# 將班次一到五與其所有時間用一種資料型態個別保存
# 比較一下範例檔案中的「File I/O」與「CSV Reader」讀出來的內容有什麼差異


# import urllib.request

# res = "http://opendata.hccg.gov.tw/dataset/432257df-491f-4875-8b56-dd814aee5d7b/resource/de014c8b-9b75-4152-9fc6-f0d499cefbe4/download/20150305140446074.csv"
# urllib.request.urlretrieve(res, './data/example.csv')


""" File i/o """

# fh = open("C:/Users/admin/Desktop/push_to_github/reptile_marathon/day02/example.csv","r",encoding='utf-8')
# f = fh.read()
# fh.close()

# print(f)
""" CSV """
#     delimiter=','
# import csv
# # 開啟 CSV 檔案
# with open('./day02/example.csv', newline='', encoding="utf-8") as csvfile:
#     # 讀取 CSV 檔案內容
#     rows = csv.reader(csvfile)
#     # 以迴圈輸出每一列
#     for row in rows:
#         print(row)

#Ans: File I/O為一連串的字串所組成，CSV Reader 是串列的集合，每個串列為一行，每個串列裡都用逗號來區分開元素。


# 1.取出班次一的每一個時間

# import csv
# # 開啟 CSV 檔案
# with open('./day02/example.csv', newline='', encoding="utf-8") as csvfile:
#     # 讀取 CSV 檔案內容
#     rows = csv.reader(csvfile)
#     # 以迴圈輸出每一列
#     for row in rows:
#         print(row[5])


# 2.將班次一的每一個時間用一種資料型態保存

# import csv
# # 開啟 CSV 檔案
# times = []
# with open('./day02/example.csv', newline='', encoding="utf-8") as csvfile:
#     # 讀取 CSV 檔案內容
#     rows = csv.reader(csvfile)
#     # 以迴圈輸出每一列
#     for row in rows:
#         times.append(row[5])
# print(times)

# 3.將班次一到五與其所有時間用一種資料型態個別保存

import csv
# 開啟 CSV 檔案
times1 = []
times2 = []
times3 = []
times4 = []
times5 = []
with open('./day02/example.csv', newline='', encoding="utf-8") as csvfile:
    # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
    # 以迴圈輸出每一列
    for row in rows:
        times1.append(row[5])
        times2.append(row[6])
        times3.append(row[7])
        times4.append(row[8])
        times5.append(row[9])
print(times1,"\n",times2,"\n",times3,"\n",times4,"\n",times5)

