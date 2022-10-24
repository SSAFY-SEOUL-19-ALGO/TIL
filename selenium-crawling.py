from selenium import webdriver
import requests
from bs4 import BeautifulSoup

driver = webdriver.Safari()

til = {
    "sanwon": "https://github.com/nowgnas/TIL",
    "yejin": "https://github.com/yejin013/TIL",
    "junmo": "https://github.com/devjunmo/TIL",
    "sooji": "https://github.com/KangSuzy/TIL",
    "jino": "https://github.com/wlsgh7608/TIL",

}

driver.get(til["sanwon"])

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
datas = soup.select(
    '#repo-content-pjax-container > div > div > div.Layout > div.Layout-main > div.Box > div.Box-header> div > div.flex-1 > div.d-flex > a.ml-2 > relative-time'
)
for title in datas:
    print(title.get('title')[:13])
