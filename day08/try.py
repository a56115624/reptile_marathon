import requests
import os

from bs4 import BeautifulSoup
from PIL import Image
url = "https://www.ptt.cc/bbs/Beauty/M.1574854555.A.E5C.html"
response = requests.get(url,cookies={"over18":"1"})
soup = BeautifulSoup(response.text,"html.parser")
# 決定資料夾
putin ="downloads"
# 如果資料夾不再就創一個
if not os.path.exists(putin):
    os.makedirs(putin)
# 定位所有圖片
image_tags = soup.find(id='main-content').findChildren('a')
for image_tag in image_tags:
    if 'imgur' not in image_tag['href']:
        continue
    img_id = image_tag['href'].split('/')[-1] # 擷取最後一段
    # print(img_id)
    img_url = f'https://i.imgur.com/{img_id}'
    # print(img_url)
    with requests.get(img_url,stream=True) as r:
        r.raise_for_status()
        # 檢查圖片副檔名
        img = Image.open(r.raw)
        img_savename = '{put_in}/{img_id}.{img_ext}'.format(
            put_in = putin ,img_id = img_id, img_ext = img.format.lower())
        img.save(img_savename)
        print('Save image {}'.format(img_savename))