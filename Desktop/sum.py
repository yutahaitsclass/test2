import requests
import lxml.html
from bs4 import BeautifulSoup 
import urllib.request

response = requests.get('https://www.flierinc.com/summary/list')
root = lxml.html.fromstring(response.content)
root.make_links_absolute(response.url)  
list = []
for a in root.cssselect('.summary-md a'):
    url = a.get('href')
    list.append(url)
for item in list:
    url_item = urllib.request.urlopen(item)
    soup = BeautifulSoup(url_item, "html.parser")
    for p in soup.find_all('div', class_="summary-body"):
        print(p.text)