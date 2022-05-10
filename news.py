import requests
from bs4 import BeautifulSoup



header ={                                                               
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
url = "https://www.bbc.com/turkce"
page = requests.get(url,headers=header)                                 
htmlPage = BeautifulSoup(page.content,'html.parser')                      


news_Titles = htmlPage.find_all("h3", attrs={"class":"bbc-t81ytv e1tfxkuo2"})  

for new_Title in news_Titles :
        print("")
        print(new_Title.getText())
        print("")
        
      
        

