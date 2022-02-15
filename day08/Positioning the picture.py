import requests
import os

from bs4 import BeautifulSoup
from PIL import Image
resp = requests.get('https://i.imgur.com/Cgb5oo1.jpg', stream=True)
image = Image.open(resp.raw)
print(image.format) # e.g. JPEG