#import libraries
import os
import requests
import re
from bs4 import BeautifulSoup

#clear system
clear = lambda: os.system('cls')


while True:
    #input brand name
    brand = input("Input brand: ")
    
    URL = "https://desktop.bg/displays-all"
    page = requests.get(URL)

    #parse HTML document
    soup = BeautifulSoup(page.content, 'html.parser')

    #get all values starting with the inputted brand name
    monitors = soup.find_all(string=re.compile("^{}".format(brand)))

    #get all values with "span" tag with class "price" in the body
    prices = soup.body.find_all("span", class_="price")

    price = 0

    for monitor in monitors:
        if len(monitor) > 8:
            print(monitor.text.strip() + " -", prices[price].text.strip())
            price+=1

    #if "ENTER" is press clear the system and start searching again
    if input("Press ENTER to search again.  ") == "":
        clear()
    else:
        break
