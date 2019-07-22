from bs4 import BeautifulSoup
import requests

url = 'https://www.blocket.se/goteborg?ca=15'
response = requests.get(url)
content = BeautifulSoup(response.content, "html.parser")

advertismentList = content.find_all('article', attrs={'class': 'media item_row ptm pbm nmt'})

print(advertismentList)