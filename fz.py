import re
import urllib.request
from bs4 import BeautifulSoup

html_page = urllib.request.urlopen('https://www.pnp.ru/law/')
print(html_page)

soup = BeautifulSoup(html_page, 'html.parser')

with open('fz.json', 'w', encoding = 'utf-8') as f:
    num_of_page = 221
    for i in range(num_of_page):
        url = 'https://www.pnp.ru/law/' + str(i + 1)
        for links in soup.findAll('a', attrs={'href': re.compile("/download/\d+(?=\/)")}, target = '_blank'):
            print(links.get('href'))
            f.write(links['href'] + '\n')

