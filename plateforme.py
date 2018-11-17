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

count = 0
final_data = []
for row in rows :
    split_list = row.split(';')
    final_data.append(split_list)
    count += 1

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
    i += 1

lib_unite = lib_unite[1:count]
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


compte_unite = {}.fromkeys(set(lib_unite),0)
for valeur in lib_unite:
    compte_unite[valeur] += 1
#print(compte_unite)



#### Avec le module Counter ####

from collections import Counter

c = Counter(lib_unite)

#for cle in c.keys():
#    print(cle)
#
#for valeur in c.values():
#    print(valeur)
    
    
    
# Ecrire les resultats dans un fichier json
#{"unite",valeur, "frequence":val,"annee",val,"semaine",}



# =============================================================================
# Générer les résultats sous forme graphique
# =============================================================================

# importer la librairie graphique
import matplotlib.pyplot as plt

# importer la librairie PDF 
from fpdf import FPDF

# définir les axes x et y avec les clés et valeurs 
data_unite = c
x_axe = data_unite.keys()
y_axe = data_unite.values()

# générer les résultats en graphiques barres
plt.bar(x_axe, y_axe, width=0.5, align='center', color='orange')

# renommes axes x et y et donner un titre au graphique
plt.xlabel('Unité')
plt.ylabel('Nombre de faits')
plt.title('Faits par unité')


# =============================================================================
# Génrer résultats en image et export PDF 
# =============================================================================

# enregistrer dans un fichier. L'image graphique.jpg va être créé
plt.savefig("graphique.jpg")
plt.show()
plt.close()

# générer le PDF
pdf = FPDF()

# ajoute une page
pdf.add_page()

# choix de la typo
pdf.set_font("Arial", size=12)

# titre du PDF
pdf.cell(200, 10, txt="Gendarmerie nationale", ln=1, align="C")

# fonction pour ajouter les images
def add_image(image_path):
    # position de l'image
    pdf.image(image_path, x=0, y=50, w=100)
    pdf.ln(95)  # move 85 down
    pdf.cell(200, 10, txt="".format(image_path), ln=1)
  
if __name__ == '__main__':
    add_image('graphique.jpg')

pdf.output("charlotte-solene.pdf")
