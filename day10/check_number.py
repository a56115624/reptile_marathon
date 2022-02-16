# 測試是否為電話號碼的程式
# 麻煩版
# def isPhoneNumber(text):
#      if len(text) != 12:
#          return False
#      for i in range(0,2):
#          if not text[i].isdecimal():
#              return False
#      if text[2] != '-':
#          return False
#      for i in range(4,7):
#          if not text[i].isdecimal():
#              return False
#      if text[7] != '-':
#          return False
#      for i in range(8,11):
#          if not text[i].isdecimal():
#              return False
#      return True 
  
# print('this is a number: 02-1234-5555')
# print(isPhoneNumber('02-1234-5555'))
# print('this is a number: oh no! regular expression')
# print(isPhoneNumber('oh no! regular expression'))


# Data = 'Please call David at 02-8888-1688 by today. 02-9888-9898 is his office number.'
# for i in range(len(Data)):
#     number = Data [i:i+12]
#     if isPhoneNumber(number):
#         print('Phone Number: ' + number)
# print('Please call him/her as soon as possible.')



#用正規表示式取代
import re
# phoneNumRegex = re.compile(r'\d\d-\d\d\d\d-\d\d\d\d')
# result = phoneNumRegex.findall('Please call David at 02-8888-1688 by today. 02-9888-9898 is his office number.')
# number = ', '.join(result)
# print('Phone Number: ' + number)
# print('Please call him/her as soon as possible.')


phoneNumRegex = re.compile(r'\d\d-\d\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Call me at 02-8888-1688 by today.')
print(mo.group())

