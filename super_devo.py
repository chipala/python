#!/usr/bin/env python3

from random import randint

# --------------------------------------------------------------------------------
LISTE_TERRAIN = ['terre', 'eau', 'aire', 'feu']
LISTE_DINO = [
"Tyrannosaurus",
"Vélociraptor",
"Diplodocus",
"Tricératops",
"Allosaure",
"Stégosaure",
"Archéoptéryx",
"Ankylosaure",
"Spinosaure",
"Gallimimus",
]

JEU_52 = []
NB_DYNO = len(LISTE_DINO)
NB_CARTE_MAIN = 5
LISTE_JOUEURS = ["jack", "xav", "papa", "baba", "yo"]
# --------------------------------------------------------------------------------


""" Un  Joueur"""
class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = cree_main(NB_CARTE_MAIN)

    def __str__(self):
        str = "["
        for carte in self.main:
            str += " {" + carte.__str__() + "}"
        str += " ]"

        return "{:10} {}".format(self.nom, str)
    

""" Une Carte """
class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __str__(self):
        tete_val = self.value
        return "{:13} : {:6}".format(tete_val, self.color)


""" Initialise la liste globale correspondant a un jeu de 52 cartes"""
def init_jeu():
    for couleur in range(len(LISTE_TERRAIN)):
        for valeur in range(NB_DYNO):
            JEU_52.append(Card(LISTE_DINO[valeur], LISTE_TERRAIN[couleur]))


""" Affiche toutes les cartes du jeux """
def affiche_jeu():
    for carte in JEU_52:
        print(carte)


""" Creer une main """
def cree_main(nb_carte):
    carte_en_main = 0
    liste_main = []
    nb_total_carte = len(JEU_52)

    while len(liste_main) < nb_carte:
        index = randint(0,(nb_total_carte - 1) - carte_en_main)
        liste_main.append(JEU_52.pop(index))
        carte_en_main = carte_en_main + 1

    return liste_main
        
        
# --------------------------------------------------------------------------------
# DEBUT DU PROGRAMME
# --------------------------------------------------------------------------------
init_jeu()

for joueur in LISTE_JOUEURS:
    print(Joueur(joueur))
