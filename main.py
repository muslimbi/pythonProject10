import requests
from bs4 import BeautifulSoup as soup

page = requests.get("https://boston.craigslist.org/d/automotive-services/search/aos")

url = "./pageData.txt"
bsobj = soup(open(url, encoding="utf8").read(), 'html.parser')
links = []
price = []
location = []
heading = []

for link in bsobj.find_all('li', {'class': 'result-row'}):
    links.append(link.a['href'])
    price.append(link.find('span', {'class': 'result-price'}))
    location.append(link.find("span", {"class": "result-hood"}))

print(links)
print(price)
print(location)

title = []
for link in links:
    page = requests.get(link)
    bsobj = soup(page.content, 'html.parser')
    print(bsobj.findAll('h2')[0].text.strip())
    title.append(bsobj.findAll('h2')[0].text.strip())
    for i in bsobj.findAll('section', {'id': 'postingbody'}):
        print(i.text.strip())
