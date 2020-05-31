import requests
from bs4 import BeautifulSoup
url = r'https://www.flipkart.com/acer-nitro-5-core-i7-9th-gen-8-gb-1-tb-hdd-256-gb-ssd-windows-10-home-4-graphics-nvidia-geforce-gtx-1650-an515-54-742f-an515-54-76nb-gaming-laptop/p/itm89c6770573582?pid=COMFHNY8BHYY9JKK&marketplace=FLIPKART'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
price = soup.find('div',attrs={'class':'_1HmYoV _35HD7C col-8-12'})
print(price.tag)