from bs4 import BeautifulSoup
import requests

url = 'https://www.blocket.se/goteborg?ca=15'
response = requests.get(url)
content = BeautifulSoup(response.content, "html.parser")

# to print a single 'price'
# prices = content.find('p', attrs={'class': 'list_price font-large'})

# print(prices)

for prices in content.findAll('p', attrs={'class': 'list_price font-large'}):
  print(prices.text.encode('utf-8'))