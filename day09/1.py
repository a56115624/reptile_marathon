# requests + BeautifulSoup

import requests
from  bs4 import  BeautifulSoup

r1 = requests.get("https://www.cupoy.com/home")
soup= BeautifulSoup(r1.text,"html.parser")
print(type(soup),soup.find('title').text)



# from  grab import Grab
# from  pyquery import PyQuery as pq

# g = Grab()
# grp = g.go("http://www.cupoy.com/home")
# # print(grp.body)
# p = pq(grp.body)
# print(type(p('title')) , p('title').text())