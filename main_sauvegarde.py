#!/usr/bin/python

import random

print("Hello jack !!")

def dire_bonjour(nom):
    print(nom)

de = input("Taper un nombre:")
print("Vous avez tape le nombre suivant ",de)

continuer = input("Voulez continuer ?")

if continuer == "oui":
    print("ok")
else:
    print("A une prochaine fois")


liste_exemple = range(int(de))

for i in liste_exemple:
	print("'la valeur de i est :", i)

liste_prenom = ["papa", "jacques", "xavier", "yolene"]
liste_age = [77, 44, 38, 36]
liste_nimporte_quoi = [1, "chaine", 't', liste_prenom]

def affiche(liste):
	for i in liste:
		print(i)

print("==============================================")

affiche(liste_prenom)

print("==============================================")

affiche(liste_age)

print("==============================================")

affiche(liste_nimporte_quoi)

print("==============================================")

def lancer_de():
	return random.randint(1, 6)

de = lancer_de()
print("La valeur est :", de)
