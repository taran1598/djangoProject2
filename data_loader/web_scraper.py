import bs4
import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

url = 'https://www.foodnetwork.com/recipes/food-network-kitchen/baked-eggs-with-salsa-verde-recipe-2009020#/'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

page_html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
# uClient = urlopen(req)  # open url
# page_html = uClient.read()  # get html (raw html)
# uClient.close()  # close the connection

# html parsing
page_soup = soup(page_html, "lxml")

section = page_soup.find_all('p', class_='o-Ingredients')
print(section[0].find_all('p', class_='o-Ingredients__a-Ingredient')[0])
# print(page_soup)
