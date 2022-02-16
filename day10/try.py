import re
# def RegexMatchingTest (regex,inputtext):
#         parten = re.compile(regex)

# test_string = "My plate number is XYZ-1234."
# regex = 'My plate number is \w\w\w-\d\d\d\d'
# RegexMatchingTest(regex, test_string)


# 用search表達
rex = re.compile(r'\w\w\w-\d\d\d\d')
mo = rex.search("My plate number is XYZ-1234.")
print(mo.group())

# test_string = "My phone number is 0912-345 678."
# regex = 'My phone number is \d\d\d\d-\d\d\d\s\d\d\d'
# RegexMatchingTest(regex, test_string)


#用findall
rex = re.compile(r'\d\d\d\d-\d\d\d\s\d\d\d')
mo = rex.findall("My phone number is 0912-345 678.")
print(mo)

#簡化版
# #利用量詞{n,m}來簡化寫法
# test_string = "My phone number is 0912-345 678."
# regex = 'My phone number is \d{4}-\d{3}\s{1}\d{3}'
# RegexMatchingTest(regex, test_string)
rex = re.compile(r'\d{4}-\d{3}\s\d{3}')
mo = rex.findall('My phone number is 0912-345 678.')
print(mo)

# 最簡單版
# 更偷懶的寫法，用「.」來代表任何字元
# test_string = "My phone number is 0912-345 678."
# regex = 'My phone number is .{4}-.{3}.{1}.{3}'
# RegexMatchingTest(regex, test_string)
rex = re.compile(r'.{4}-.{3}.{1}.{3}')
mo = rex.search("My phone number is 0912-345 678")
print(mo.group())

# 用[]找出裡面有的東西
# test_string = "I love dogs."
# regex = 'I love [acdgnost]'
# RegexMatchingTest(regex, test_string)
rex = re.compile(r'I love [acdgnost]')
mo = rex.search("I love dogs.")
print(mo.group())

# 若要匹配超過一個以上的字元，必須加入量詞(「+」或「*」或「?」)來表達
# test_string = "I love dogs."
# regex = 'I love [acdgnost]+'
# RegexMatchingTest(regex, test_string)

rex = re.compile(r'I love [acdgnost]+')
mo = rex.search("I love dogs.")
print(mo.group())


# 分組及捕捉
# test_string = "I like baseball sport."
# regex = 'I like (hiking|baseball) sport'
# RegexMatchingTest(regex, test_string)

rex = re.compile(r'I like (hiking|baseball) sport')
mo = rex.search("I like baseball sport.")
print(mo.group())

# 用\(來表示括號
# test_string = "Please call number (02)2882-5252."
# regex = 'Please call number \([0-9]{2}\)[0-9]{4}-[0-9]{4}'  #用「\(」來匹配左括號"("，用「\)」來匹配右括號")"
# # RegexMatchingTest(regex, test_string)
rex = re.compile(r'Please call number \([0-9]{2}\)[0-9]{4}-[0-9]{4}')
mo  = rex.search("Please call number (02)2882-5252.")
print(mo.group())

# 比對中文字
# test_string = "Here are 中文字 and English"  #中英夾雜的句子
# regex = '[\u4e00-\u9fa5]+'                  #中文的UNICODE，範圍是0x4E00 ~ 0x9FA5
# RegexMatchingTest(regex, test_string)