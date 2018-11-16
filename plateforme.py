#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:42:53 2018

@author: CharlotteMorin
"""


#import csv
#
#f = open("synthese-test.csv", 'r', encoding='utf-8')
#file = list(csv.reader(f))



chemin = "synthese-test.csv"

file = open(chemin, 'r', encoding='utf-8') 
data = file.read()

rows = data.split('\n')
#print(type(rows))


# =============================================================================
# Afficher toutes les datas
# =============================================================================

count = 1
final_data = []
for row in rows :
    split_list = row.split(';')
    final_data.append(split_list)
    count +=1

final_data = final_data[1:count]
#print(final_data)


# =============================================================================
# Afficher la deuxième colonne (Libellé unité)
# =============================================================================

i = 0
lib_unite = []
for libelle_unite in rows :
    split_lib_unite = libelle_unite.split(';')
    lib_unite.append(split_lib_unite[1])
    i +=1

libelle_unite = libelle_unite[1:count]
#print(lib_unite)


# =============================================================================
# Compter le nombre d'occurences d'une unité
# =============================================================================

#def nb_lib_unite(unite):
#    count = 0
#    for row in lib_unite:
#        if row == unite:
#            count +=1
#    return (count)
#
#bta_brignoles = nb_lib_unite("BTA BRIGNOLES")
#print(bta_brignoles)
#
#cob_st_maximim = nb_lib_unite("COB ST MAXIMIN LA STE BAUME")
#print(cob_st_maximim)


#compte_unite = {}.fromkeys(set(lib_unite),0)
#for valeur in lib_unite:
#    compte_unite[valeur] += 1
#print(compte_unite)



#### Avec le module Counter ####

#from collections import Counter
#
#c = Counter(lib_unite)
#
#for cle in c.keys():
#    print(cle)
#
#for valeur in c.values():
#    print(valeur)
