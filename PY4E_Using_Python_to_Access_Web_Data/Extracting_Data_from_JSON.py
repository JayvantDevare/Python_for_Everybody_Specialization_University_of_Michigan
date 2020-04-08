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
import json
import urllib
from urllib.request import urlopen
count = 0

url = input("Enter location: ")  #actual url -http://py4e-data.dr-chuck.net/comments_378595.json
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_378595.json"
print ("retrieving URL. Stand by.")
uh = urlopen(url)
data= uh.read()

info = json.loads(data)
for item in info["comments"]:
	#print item["count"]
	number = int(item["count"])
	count = count + number
print (count)
