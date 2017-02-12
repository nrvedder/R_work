# This is some python work I did using Beautiful Soup to scrape data from
# a fantasy football xml table and bring it in as either a pandas dataframe
# or a dictionary of column name and list pairs 

import psycopg2 as psy
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

# Pandas Dataframe table creator function
def tabler(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    ncol = len(soup.find_all('th'))
    nrow = len(soup.find_all('tr'))
    dat = pd.DataFrame(index = range(1,nrow), columns = range(0, ncol))
    for col in range(0,ncol):
        for row in range(1, nrow):
            dat.loc[row, col] = soup.find_all('tr')[row].find_all('td')[col].string.strip()
    colnames = []
    for names in soup.find_all('th'):
        colnames.append(names.string.strip())
    dat.columns = colnames
    return dat

pandas_df = tabler('https://fantasydata.com/nfl-stats/nfl-fantasy-football-stats.aspx')
pandas_df

# Dictionary Creator
def tabler(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    ncol = len(soup.find_all('th'))
    nrow = len(soup.find_all('tr'))
    cols = []
    d = {}
    for col in range(0,ncol):
        l = []
        for row in range(1, nrow):
            l.append(soup.find_all('tr')[row].find_all('td')[col].string.strip())
        cols.append(l)
    colnum = 0
    for names in soup.find_all('th'):
        d[names.string.strip()] = list(cols[colnum])
        if colnum == ncol:
            break
        else:
            colnum += 1
    return d

fb_dict = tabler('https://fantasydata.com/nfl-stats/nfl-fantasy-football-stats.aspx')
fb_dict