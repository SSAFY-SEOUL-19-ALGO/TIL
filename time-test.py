import requests
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver

now = datetime.now()


updateTime = now.astimezone().strftime('%Y-%m-%d %H:%M:%S')
print(updateTime)
