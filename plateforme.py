#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:42:53 2018

@author: CharlotteMorin
"""


#import csv
#
#with open('synthese-test.csv', newline='') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=',')
#    for row in spamreader:
#        print(row)


chemin = "synthese-test.csv"

file = open(chemin, 'r', encoding='utf-8') 
data = file.read()

rows = data.split('\n')
#print(type(rows))


count=0

final_data = []
for row in rows :
    split_list = row.split(';')
    final_data.append(split_list)
    count +=1

final_data = final_data[1:count]
#print(final_data)
