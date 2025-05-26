import requests
from bs4 import BeautifulSoup
import re

origin_url = "https://www.bible.com/bible/111/GEN.1.NIV"

headers = {
   
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

# 发送GET请求
res = requests.get(origin_url, headers=headers)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

print(soup.contents)