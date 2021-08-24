# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 12:52:32 2021

@author: rubyasar
"""

from bs4 import BeautifulSoup
import urllib.request 
import re

data=urllib.request.urlopen('https://analytics.usa.gov').read()
bs=BeautifulSoup(data,'lxml')
print(bs.prettify())

address="C:/Users/rubya/Desktop/Web Scraping/"

""" Get All Web-Links """
with open(address+'links.txt','wt') as file:
    for link in bs.find_all('a',attrs={'href':re.compile('^https')}):
        file.write(link.get('href')+'\n')                   

""" Get All Agency-Names """
with open(address+'agences.txt','wt') as file:
    file.write(bs.find('select' , attrs={'id':'agency-selector'}).get_text().strip())

""" Get All Data-Sources """
with open(address+'datasources.txt','wt') as file:
    for link in bs.find_all('figure',attrs={'data-source':re.compile('^https://.*.json')}):
        file.write(link['data-source']+'\n')

