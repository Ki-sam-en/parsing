import requests
from bs4 import BeautifulSoup as beautiSoup

import re

import config

def gets_currencies_links():

    with open("pages.txt", "r", encoding="utf-8") as file:
        
        for i in file:
            response = requests.get(url=i, headers=config.HEADERS)

            if response.status_code == 200:
                print("юху")
                
                soup = beautiSoup(response.text, "lxml")
                
                with open ("links_first.txt", "a", encoding="utf-8") as file:
                        
                    for sp in soup.find_all("a", class_="cmc-link", attrs={"href" : re.compile("^/currencies")}):
                        link = config.URL + str(sp.get("href"))
                        
                        file.write(link + "\n")
            
            else:
                print("сломалось чет...")           
                
    return file
  
    
links = gets_currencies_links()
print(links)