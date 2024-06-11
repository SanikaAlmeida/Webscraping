#Steps:
# 1. send http request to the url-> receives the html 
# 2. parse the content
# 3. extract the exact data

import pandas as pd
import requests
from bs4 import BeautifulSoup

ProductName=[]
Prices=[]
Description=[]
Reviews=[]

url='https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")
boxes=soup.find_all('div',class_="_75nlfW")

for box in boxes:
    names=box.find('div',class_="KzDlHZ")
    ProductName.append(names.text)

    prices=box.find('div',class_="Nx9bqj _4b5DiR")
    Prices.append(prices.text)

    descs=box.find('ul',class_="G4BRas")
    Description.append(descs.text)

    reviews=box.find('div',class_="XQDdHH")
    Reviews.append(reviews.text)
   
# print(ProductName)
# print(Prices)
# print(Description)
# print(Reviews)

df=pd.DataFrame({"Name":ProductName,"Prices":Prices,"Description":Description,"Reviews":Reviews})
print(df)