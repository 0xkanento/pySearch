import requests 
from bs4 import BeautifulSoup

#Author : Kanento
#Update Software : V.1
#Description : Faites des recherche directement avec python


print("""
██▓███ ▓██   ██▓  ██████ ▓█████ ▄▄▄       ██▀███   ▄████▄   ██░ ██ 
▓██░  ██▒▒██  ██▒▒██    ▒ ▓█   ▀▒████▄    ▓██ ▒ ██▒▒██▀ ▀█  ▓██░ ██▒
▓██░ ██▓▒ ▒██ ██░░ ▓██▄   ▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒▒▓█    ▄ ▒██▀▀██░
▒██▄█▓▒ ▒ ░ ▐██▓░  ▒   ██▒▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄  ▒▓▓▄ ▄██▒░▓█ ░██ 
▒██▒ ░  ░ ░ ██▒▓░▒██████▒▒░▒████▒▓█   ▓██▒░██▓ ▒██▒▒ ▓███▀ ░░▓█▒░██▓
▒▓▒░ ░  ░  ██▒▒▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ░▒ ▒  ░ ▒ ░░▒░▒
░▒ ░     ▓██ ░▒░ ░ ░▒  ░ ░ ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░  ░  ▒    ▒ ░▒░ ░
░░       ▒ ▒ ░░  ░  ░  ░     ░    ░   ▒     ░░   ░ ░         ░  ░░ ░
         ░ ░           ░     ░  ░     ░  ░   ░     ░ ░       ░  ░  ░
         ░ ░                                       ░                
""")


def Google():
  
 
 url = "https://www.google.com/search?q="
 search = input("Enter your search : ")
 r = requests.get(f"{url}{search}")
 soup = BeautifulSoup(r.content, "html.parser")
 for link in soup.find_all("a"):
   print(link.get("href"))

if __name__ == "__main__":
  Google()
 
  

 
  











