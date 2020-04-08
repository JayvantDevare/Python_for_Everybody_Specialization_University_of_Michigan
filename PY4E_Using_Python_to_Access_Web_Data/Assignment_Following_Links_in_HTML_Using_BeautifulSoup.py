#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jayvant
#
# Created:     25/03/2020
# Copyright:   (c) jayvant 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

#url = 'http://py4e-data.dr-chuck.net/known_by_Ailidh.html'
#possition - 18
#times - 7
url = input('Enter URL:')

position = int(input('Enter position:'))-1
count = int(input('Enter count:'))
html = urlopen(url).read()

soup = BeautifulSoup(html,"html.parser")
href = soup('a')
#print href

for i in range(count):
    link = href[position].get('href', None)
    print (href[position].contents[0])
    html = urlopen(link).read()
    soup = BeautifulSoup(html,"html.parser")
    href = soup('a')