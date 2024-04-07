# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 12:37:53 2024

@author: Kamil
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


file_path = r"C:\Users\Kamil\OneDrive\Inżynieria danych i Data Science\Tricity-housing\data\flat-sell.csv"
url_site = "https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdansk/gdansk/gdansk?ownerTypeSingleSelect=ALL&by=DEFAULT&direction=DESC&viewType=listing&page="


data = pd.DataFrame()
response = requests.get("https://www.morizon.pl/mieszkania/gdansk/")
soup = BeautifulSoup(response.text, features='html.parser')
    
pages = int(soup.find_all("div", attrs={"class": "I03LY0"})[-2].text)
    

for i in range(1, pages+1):
    print(i)