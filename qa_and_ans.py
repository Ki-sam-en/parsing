import json
import urllib3
from bs4 import BeautifulSoup
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
filtered_links=[]
URL = 'https://sudact.ru/qa/questions/scope:all/sort:activity-desc/page:'
data=[]

r=requests.get(URL + str(1), verify=False).text
max_pages = [div['title'][9:] for div in BeautifulSoup(r, "html.parser").find_all('a', title=True) \
            if "страница " in div['title']][-1]

print(max_pages)


for p in range(int(max_pages)):
    cur_url = URL + str(p + 1)
    print(f"Скрапинг страницы №: {(p + 1)}")
    html_text = requests.get(cur_url, verify=False).text
    soup = BeautifulSoup(html_text, "html.parser")
    for a in soup.find_all('a'):
        s = a.get('href')
        if s is not None and ("question" in s and ":" not in s and s.count('/')==5):
            filtered_links.append(s)

for t in filtered_links:
    print(f"Обрабатывается {t} ссылка")
    url = 'https://sudact.ru'+t
    html_text = requests.get(url, verify=False).text
    soup = BeautifulSoup(html_text, "html.parser")
    txt = [t.text for t in soup.find_all('div', class_='post-body', attrs={'text'})]
    data.append([txt[0], txt[1:]])

with open('file.json', "w", encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)

