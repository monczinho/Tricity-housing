# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 12:37:53 2024

@author: Kamil
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
# import re


file_path = r"C:\Users\Kamil\OneDrive\Inżynieria danych i Data Science\Tricity-housing\data\flat-sell.csv"

# included filter in link in order to get only offers with known prices
url_site = "https://www.morizon.pl/mieszkania/gdansk/?ps%5Blocation%5D%5Bmap%5D=1&ps%5Blocation%5D%5Bmap_bounds%5D=54.4472188%2C18.9512795%3A54.2749559%2C18.4287748&ps%5Bwith_price%5D=1&page="
flats = pd.DataFrame()

def get_flat_info(flat_url):
    response_flat = requests.get(flat_url)
    soup_flat = BeautifulSoup(response_flat.text, features='html.parser')
    
    # if not soup_flat.find("h3", attrs={"class": "offer-title big-text ezl3qpx2 ooa-ebtemw er34gjf0"}):
    #     return pd.DataFrame()
    
    price = soup_flat.find("span", attrs={"class": "hUo19C"}).text
    title = soup_flat.find("h1", attrs={"class": "reQkSH"}).text
    # attribute_table = soup_flat.find('div', attrs={"class": "ooa-1gtr7l5 e18eslyg2"})
    
    flat_dict = {}
    flat_dict['Nazwa'] = title
    flat_dict['Cena'] = price
    
    for section in soup_flat.find_all('div', attrs={"class": "kG1Tuz"}):
        for attribute in section.find_all('div', attrs={"class": "oH0nKI"}):
            attribute_name = attribute.find('div', attrs={"class": "OlSncH cBsAOs"}).text
            attribute_value = attribute.find('div', attrs={"class": "OlSncH i1S7Na"}).text
            
            flat_dict[attribute_name] = attribute_value
            flat = pd.DataFrame(flat_dict, index=[0])
    return flat

data = pd.DataFrame()
response = requests.get(url_site + '1')
soup = BeautifulSoup(response.text, features='html.parser')
    
pages = int(soup.find_all("div", attrs={"class": "I03LY0"})[-2].text)
    

for i in range(1, pages+1):
    url = url_site + str(i)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='html.parser')
    
    flat_list = soup.find_all('div', attrs={"class": "card__outer"})
    
    for flat in flat_list:
        link = flat.find('a').get("href")
        name = flat.find('span', attrs={"class": "_9Y9BTQ"}).text
        link = "https://www.morizon.pl" + link
        flat_info = get_flat_info(link)
        flats = pd.concat([flats, flat_info]) 
    print(i)

flats.to_csv(file_path, index=False, sep='|')
print('File created')
    
