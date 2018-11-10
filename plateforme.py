#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:42:53 2018

@author: CharlotteMorin
"""

import csv
import matplotlib

chemin = 'synthese-test.csv'

f = open(chemin, 'r')

## avec la fonction readline() et la boucle while on affiche chaque ligne du fichier csv
#line = f.readline()
#while line:
#    print(line)
#    line = f.readline()


try :
    fichier_csv = csv.reader(f)
    for row in fichier_csv :
        print(row[0])
finally :
    f.close()
