#!/usr/bin/env python
# Supprimer la ligne ci-dessus si le programme ne se lance pas

from random import randint

class Joueur:
    def __init__(self, pseudo):
        self._pseudo = pseudo
        self._point = 0
    
    def __str__(self):
        return f"{self._pseudo:<10}: {self._point:>4}"

class De:
    def __init__(self, nb_face=6):
        self._nb_face = nb_face
        self._valeur = De.lance_de(self._nb_face)

    def lance_de(face):
        return randint(1, face)

    def lance(self):
        self._valeur = lance_de(self._nb_face)

    def valeur(self):
        return self._valeur

    def __str__(self):
        return f"{self._valeur}"

class Jeu:
    def __init__(self, nb_tour=2, nb_joueur=2):
        self._nb_tour = nb_tour
        self._nb_joueur = nb_joueur

    def moteur(self):
        pass

if __name__ == "__main__":
    j_1 = Joueur("joueur 1")
    print(j_1)
    de_1 = De()
    print(de_1)
    pass
