# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 05:18:09 2019

@author: RDxR10
"""

import bs4 as bs
import urllib.request as UR
import pandas as pd

Cities=[]
link='https://karki23.github.io/Weather-Data/assignment.html'
sauce = UR.urlopen(link).read()
soup = bs.BeautifulSoup(sauce, 'lxml')
for _ in soup.find_all('a'):
    href=_.get('href')
    print(href)

scrape_Data_conn = UR.urlopen(link)
content = scrape_Data_conn.read()
scrape_Data_conn.close()
s1 = bs.BeautifulSoup(content,'lxml')
for href in s1.find_all('a'):
    Cities.append('https://karki23.github.io/Weather-Data/'+ href.get('href'))
for city in Cities:
    CD = UR.urlopen(city)
    content1 = CD.read()
    CD.close()
    s2 = bs.BeautifulSoup(content1,'lxml')
    table = s2.find('table')
    '''
    for r in table:
            td=r.find_all('td')
            r_data = [i.text for i in td]
            print(r_data)
            print('\n')
            '''
    rows = table.find_all('tr')
    cols = [__.text.replace('\n','') for __ in rows[0].find_all('th')]
    
    df = pd.DataFrame(columns = cols)

    
    for _ in range(1,len(rows)):
        td = rows[_].find_all('td')
        r_data = [i.text for i in td]
        df = df.append(pd.Series(r_data,index=cols), ignore_index=True)
        '''
        with open('output.csv') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(r_data)
            '''
        
        df.to_csv(''+ r_data[1] + '.csv', index = False)
        
#To check 
print(df.head())

