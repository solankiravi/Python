import requests
from bs4 import BeautifulSoup
url =r'http://dataquestio.github.io/web-scraping-pages/simple.html'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
content = soup.prettify()
"""
children attributes returns generator
# [<class 'bs4.element.Doctype'>, <class 'bs4.element.NavigableString'>, <class 'bs4.element.Tag'>]
# print([type(item) for item in list(soup.children)])

"""
html = list(soup.children)[2]
# body = list(html.children)[3]
body = soup.find('body')
print(body)