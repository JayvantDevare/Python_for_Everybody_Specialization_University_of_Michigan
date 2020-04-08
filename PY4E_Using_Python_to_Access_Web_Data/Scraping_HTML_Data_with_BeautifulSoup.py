#-------------------------------------------------------------------------------
# Name:        module2
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
import ssl

url = input('Enter -  ')   #enter url - http://py4e-data.dr-chuck.net/comments_378592.html

html = urlopen(url).read()
soup = BeautifulSoup(html)
tag = soup("span")
count=0
sum=0
for i in tag:
	x=int(i.text)
	count+=1
	sum = sum + x
print (count)
print (sum)