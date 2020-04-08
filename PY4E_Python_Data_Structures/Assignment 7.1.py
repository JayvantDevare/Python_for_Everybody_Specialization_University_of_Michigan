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

# Assignment 7.1
# Write a program that prompts for a file name, then opens that file and reads through the file,
# and print the contents of the file in upper case. Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt
# Use words.txt as the file name

#save words.txt file in same directory where your .py file is stored

fname = input("Enter file name: ")   #enter file name as words.txt
fh = open(fname)
for i in fh:
    i = i.rstrip().upper()
    print (i)