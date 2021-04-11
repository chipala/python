#!/usr/bin/env python3

from random import randint

LISTE_COULEURS = ['pique', 'coeur', 'carreau', 'trefle']
JEU_32 = []

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __str__(self):
        tete_val = self.value
        if self.value == "11":
            tete_val = "valet"
        elif self.value == "12":
            tete_val = "dame"
        elif self.value == "13":
            tete_val = "roi"

        return '{:6} : {}'.format(tete_val, self.color)


def cree_jeu():
    for couleur in LISTE_COULEURS:
        for valeur in range(1, 14):
            JEU_32.append(Card(str(valeur), couleur))

def affiche_jeu():
    for carte in JEU_32:
        print(carte)


# Main 
card_1 = Card("1", "coeur")
print(card_1)

cree_jeu()
affiche_jeu()
