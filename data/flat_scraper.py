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
url_site = "https://www.morizon.pl/mieszkania/gdansk/?ps%5Blocation%5D%5Bmap%5D=1&ps%5Blocation%5D%5Bmap_bounds%5D=54.4472188%2C18.9512795%3A54.2749559%2C18.4287748&ps%5Bwith_price%5D=1&page="


data = pd.DataFrame()
response = requests.get(url_site + '1')
soup = BeautifulSoup(response.text, features='html.parser')
    
pages = int(soup.find_all("div", attrs={"class": "I03LY0"})[-2].text)
    

for i in range(1, pages+1):
    url = url_site + str(i)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='html.parser')
    
    flat_list = soup.find('div', attrs={"class": "ooa-r53y0q ezh3mkl11"})