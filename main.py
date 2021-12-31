import requests
from bs4 import BeautifulSoup as soup

page = requests.get("https://boston.craigslist.org/d/automotive-services/search/aos")
bsobj = soup(page.content,'lxml')
links = []
for link in bsobj.findAll('li',{'class':'result-row'}):
    links.append(link.a['href'])
title = []
for link in links:
    page = requests.get(link)
    bsobj = soup(page.content,'lxml')
    print(bsobj.findAll('h2')[0].text.strip())
    title.append(bsobj.findAll('h2')[0].text.strip())
    for i in bsobj.findAll('section',{'id':'postingbody'}):
        print(i.text.strip())

