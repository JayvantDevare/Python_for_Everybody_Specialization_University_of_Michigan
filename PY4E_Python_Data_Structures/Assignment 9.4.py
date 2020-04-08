#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jayvant
#
# Created:     08/04/2020
# Copyright:   (c) jayvant 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Assignment 9.4
# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

maxvalue = 0
name = ""
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = {}

l = [i.split()[1] for i in handle.readlines()
            if i.startswith("From") and i.find("@")>0 and len(i.split()) > 2]
for i in l:
    if not dic.has_key(i):
        dic[i] = 1
    else:
        dic[i] +=1
        if maxvalue < dic[i]:
            maxvalue = dic[i]
            name = i

print (name,maxvalue)

