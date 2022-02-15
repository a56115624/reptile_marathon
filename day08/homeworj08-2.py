import requests
import os

from bs4 import BeautifulSoup
from PIL import Image
url = 'https://www.ptt.cc/bbs/Beauty/M.1556291059.A.75A.html'
resp = requests.get(url, cookies={'over18': '1'})
soup = BeautifulSoup(resp.text, "html.parser")
# 確認圖片正確格式
from PIL import Image

resp = requests.get('https://i.imgur.com/Cgb5oo1.jpg', stream=True)
image = Image.open(resp.raw)
print(image.format) # e.g. JPEG

# 決定要儲存的資料夾
output_dir = 'downloads'

# 假如資料夾不存在就新增一個資料夾
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 定位所有圖片的 tag
image_tags = soup.find_all('a', rel="noreferrer noopener nofollow")
for img_tag in image_tags:
    # 取得所有圖片在第三方服務的 id
    if 'imgur' not in img_tag['href']:
        continue
    # 組合圖片而非網站的網址，前面加一個i，後面加附檔名
    img_id = img_tag['href'].split('/')[-1]
    img_url = 'https://i.imgur.com/{}.jpg'.format(img_id)
    print(img_url)
    # 對圖片送出請求
    with requests.get(img_url, stream=True) as r:
        r.raise_for_status()
        # 檢查圖片副檔名
        img = Image.open(r.raw)
        img_savename = '{outdir}/{img_id}.{img_ext}'.format(
            outdir=output_dir, img_id=img_id, img_ext=img.format.lower())
        img.save(img_savename)
        print('Save image {}'.format(img_savename))