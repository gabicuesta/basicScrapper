# import libraries
import urllib2
from bs4 import BeautifulSoup

import csv
from datetime import datetime

listSongName = []
listBandName = []

# specify the url
quote_page = 'https://www.jpopasia.com/charts/kpop/mnet/'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# get the index price
price_box = soup.find('b', attrs={'class':'a-black'})
for songName in soup.find_all('b', attrs={'class':'a-black'}):
    listSongName.append(songName.text.encode("utf-8"))

for songBand in soup.find_all('div', attrs={'class':'color-concrete margin-bottom-s'}):
    listBandName.append(songBand.text.encode("utf-8"))

rows = zip(listBandName,listSongName)

i = 0

with open("kpop.csv", "w") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
        i += 1
        if i>=20 :
            break
