def get_pages():
                    
    with open ("pages.txt", "a", encoding="utf-8") as file:
                            
        for i in range(1, 102, 1):
            page_number = i
            pages = "https://coinmarketcap.com/?page=" + str(page_number)
                            
            file.write(pages + "\n")
            
    return file

pages = get_pages()
print(pages)            
                 
