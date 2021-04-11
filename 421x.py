
#!/usr/bin/env python

import random

# --------------------------------------------------------------------------------
# Declaration des variables globales
# --------------------------------------------------------------------------------
# MAX tour
MAX_TOUR = 5

# Des
liste_de = [1, 2, 3]

# --------------------------------------------------------------------------------
# Declaration des fonctions
# --------------------------------------------------------------------------------
def lance_de(indexDe):
    liste_de[indexDe] = random.randint(1, 6)
    print("Lance le de [{}] => {}".format(indexDe + 1, liste_de[indexDe]))


def affiche_partie():
    print("--------------------------------------------------------------------------------")
    print("{:>40}".format('Jeu du 421'))
    print("--------------------------------------------------------------------------------")


def partie():
    affiche_partie()

    tour = 0
    while tour < MAX_TOUR:
        tour = tour + 1
        print("Tour numero [{}]".format(tour))

        for index in range(3):
            lance_de(index)

        print()

# --------------------------------------------------------------------------------
# Point d'entree du programme :-)
# --------------------------------------------------------------------------------
partie()

