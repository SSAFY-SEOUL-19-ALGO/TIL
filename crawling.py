import requests
from bs4 import BeautifulSoup
import json
import os
import sys
from datetime import datetime
from selenium import webdriver

now = datetime.now()


updateTime = now.astimezone().strftime('%Y-%m-%d %H:%M:%S')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 사용자 이름, til url
til = {
    "sanwon": "https://github.com/nowgnas/TIL",
    "yejin": "https://github.com/yejin013/TIL",
    "junmo": "https://github.com/devjunmo/TIL",
    "sooji": "https://github.com/KangSuzy/TIL",
    "jino": "https://github.com/wlsgh7608/JinoWiki",

}
print('github repo crawling')
data = {}
driver = webdriver.Safari()
for name, url in til.items():

    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    datas = soup.select(
        '#repo-content-pjax-container > div > div > div.Layout > div.Layout-main > div.Box > div.Box-header> div > div.flex-1 > div.d-flex > a.ml-2 > relative-time'
    )

    for title in datas:
        print(title.text)
        data[name] = title.get('title')[:13]


with open(os.path.join(BASE_DIR, 'readme.md'), 'w+', encoding='utf-8') as f:
    f.write("# Today I Learn \n")
    f.write(f'TIL list updated at {updateTime}\n')
    f.write('| name | url | updated time |\n')
    f.write('| :--- | -- | -- |\n')

    for name, time in data.items():
        f.write(f'| {name} | {til[name]} | {time} |\n')

print('crawling finish')
