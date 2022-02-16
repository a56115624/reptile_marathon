# # 剪刀石頭布
import random 


me = int(input("[0] 剪刀 [1] 石頭 [2] 布"))
com = random.randint(0,2)
tans = ["剪刀","石頭","布"]
# print(com)
print("妳出的拳",tans[me])
print("電腦出的拳", tans[com])
if me ==com:
    print("平手")
elif me == (com+1)%3:
    print("妳贏了")
else:
    print("妳輸了")