import requests
from bs4 import BeautifulSoup
import json
import os
import sys
from datetime import datetime
from selenium import webdriver

now = datetime.now()


updateTime = now.astimezone().strftime('%Y-%m-%d %H:%M:%S')
print(updateTime)
