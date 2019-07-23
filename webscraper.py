from bs4 import BeautifulSoup
import requests

url = 'https://www.blocket.se/goteborg?ca=15'
response = requests.get(url)
content = BeautifulSoup(response.content, "html.parser")

advertArr = []
for advert in content.findAll('article', attrs={"itemtype": "http://schema.org/Offer"}):
  advertObject = {
    "title": advert.find('a', attrs={"class": "item_link"}).text,
    "price": advert.find('p', attrs={"class": "list_price font-large"}).text,
    # "ad_url": advert.find('a', attrs={"itemprop": "url"}),
    # "description": advert.find('a', attrs={"title": }),
    # "photos_url": advert.find('', attrs{})
  }
print(advertObject)