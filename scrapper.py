# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 12:52:32 2021

@author: rubyasar
"""

from bs4 import BeautifulSoup
import urllib.request 
import re

#Change the below url as per your need
url='https://analytics.usa.gov'

data=urllib.request.urlopen(url).read()
bs=BeautifulSoup(data,'lxml')

#to check out the entire source code of website use below command
#print(bs.prettify())

#to check out the entire text(including js) of website use below command
#print(bs.get_text())

#Change the below path as per your need
address="C:/Users/rubya/Desktop/Web Scraping/"

""" Get All Headings """
with open(address+'headings-kpi.txt','wt') as file:
    for link in bs.find_all(['h1','h2','h3']):
        if link.string not in (None,'...'):    
            file.write(link.string+'\n')  

""" Get All Web-Links """
with open(address+'links.txt','wt') as file:
    for link in bs.find_all('a',attrs={'href':re.compile('^https')}):
        file.write(link.get('href')+'\n')                   

""" Get All Agency Names """
with open(address+'agences.txt','wt') as file:
    file.write(bs.find('select' , attrs={'id':'agency-selector'}).get_text().strip())

""" Get All Json Data-Sources """
with open(address+'datasources.txt','wt') as file:
    for link in bs.find_all('figure',attrs={'data-source':re.compile('^https://.*.json')}):
        file.write(link['data-source']+'\n')
        
""" Get API Info"""
with open(address+'api.txt','wt') as file:
    for link in bs.find_all(string=re.compile('API project')):   
        file.write(link.parent.get('href'))  

