import requests
from bs4 import BeautifulSoup
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
html = res.text
soup = BeautifulSoup( html,'html.parser')
items = soup.find_all(class_='books')
with open('files.txt','w',encoding='utf-8') as f:
    for item in items:
        kind = item.find('h2')
        title = item.find(class_='title')
        brief = item.find(class_='info')
        a=kind.text+'\n'+title.text+'\n'+title['href']+'\n'+brief.text
        f.write(a)
