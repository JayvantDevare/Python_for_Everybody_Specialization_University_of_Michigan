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
import xml.etree.ElementTree as ET

url = input("Enter location: ")  # actual url - http://py4e-data.dr-chuck.net/comments_378594.xml
if len(url) < 1:
    url = "http://python-data.dr-chuck.net/comments_200531.xml"
print ("Retrieving " + url)

xml = urlopen(url).read()
print ("Retrieved: " + str(len(xml)) + " characters")

tree = ET.fromstring(xml)

counts =  tree.findall('.//count')
print( "Count: " + str(len(counts)))

accumulator = 0

for count in counts:
    accumulator += int(count.text)

print(accumulator)