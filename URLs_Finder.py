from bs4 import BeautifulSoup
import urllib.request
import re
from termcolor import colored as c
print(c("""
------- Just run und get all links in the entered url :) -------
  _____ _           _     _     _ _           _           
 |  __ (_)         | |   | |   | (_)         | |          
 | |__) | _ __ __ _| |_  | |__ | |_ _ __   __| | ___ _ __ 
 |  ___/ | '__/ _` | __| | '_ \| | | '_ \ / _` |/ _ \ '__|
 | |   | | | | (_| | |_  | |_) | | | | | | (_| |  __/ |   
 |_|   |_|_|  \__,_|\__| |_.__/|_|_|_| |_|\__,_|\___|_|  s
                     ______                               
                    |______|                              
""","cyan"))
target = str(input("Target website (with http/https) : "))
while target == "":
    target = str(input("Enter Target Website!!!! "))
target_domain = str(input("Target website domain ONLY (example.com) : "))

openurl = urllib.request.urlopen(target)
urlcontent = openurl.read()
soup = BeautifulSoup(urlcontent, "html.parser")

# Just edit the value in findAll Method if your are looking for something else like images,scripts, etc...
a = soup.findAll("a")
for i in a:
    # Enter a certain attribute of your searched HTML element
    i = i.get("href")
    print(i)

if target_domain != "":
    print(c("\n\n\nIn url find more url related to traget website\n\n\n", "yellow"))
    ina = soup.find_all(href=re.compile(target_domain))
    for ini in ina:
        print(ini.get("href"))

print("\nProgramm Finished")



