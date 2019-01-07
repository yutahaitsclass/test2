import urllib.request
import requests
url = urllib.request.urlopen('https://newspicks.com/')
from bs4 import BeautifulSoup
soup = BeautifulSoup(url, "html.parser")
for div in soup.find_all('div', class_="title _ellipsis"):
    print(div.text)
    