import requests
from bs4 import BeautifulSoup

url = "https://www.aimeleondore.com/products/ald-nb-p550-basketball-oxfords-6"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
# print(soup.prettify())

# all_p = soup.find_all('div', {"class": "swatch-size__item swatch-size-unavailable"})
# for item in all_p:
#     print(item)
#     soup.find_all('input', {"id": "size-GREY / 6.5"})

all_p = soup.find_all('div', attrs={"class": "swatch-size__item swatch-size-unavailable"})
for item in all_p:
    print(item)



