import requests
from bs4 import BeautifulSoup

product_element = """<div class="swatch-size__item swatch-size-unavailable">
<input type="radio" name="single-name-option" id="size-GREY / 5" value="40366341521505" class="swatch-size__control">
<label for="size-GREY / 5" class="swatch-size__label">5</label>
</div>"""

# Get start tag
tag = []
soup = BeautifulSoup(product_element, 'html.parser')
for item in soup:
    tag.append(item.name)

if len(tag) > 1:
    # Raise error
    pass

# Create variable for product tag
prod_tag = tag[0]

# url = "https://www.aimeleondore.com/products/ald-nb-p550-basketball-oxfords-5"
# req = requests.get(url)
# soup = BeautifulSoup(req.content, 'html.parser')
# print(soup.prettify())
#
# all_p = soup.find_all('div', attrs={"class": "swatch-size__item swatch-size-unavailable"})
# for item in all_p:
#     print(str(item))
#
# for item in all_p:
#     if item.has_attr('swatch-size__control'):
#         print(item.text)

