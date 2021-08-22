from random import randint
import os

# Regle
g_regle_item = [
    "Total 1",
    "Total 2",
    "Total 3",
    "Total 4",
    "Total 5",
    "Total 6",
    "Brelan",
    "Carré",
    "Full 15",
    "Triple paire 25",
    "Double brelan 25",
    "Carré/Paire 25",
    "Petite suite 20",
    "Suite ordonée 30",
    "Suite moyenne 40",
    "Grande suite 60",
    "Yathzee 50",
    "Strike 100",
    "Chance",
]

# Utilitaire
def cls_ecran():
    """ CLS l'écran """
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")


# Des
def lance_des_initial():
    """ créé un lancé de 6 dés """
    return [randint(1, 6) for val in list(range(6))]


def lance_des(des):
    """ lance tous les dés """
    for de in des:
        de = randint(1, 6)
    return des


def lance_des_inter(des):
    """ selection des dés à lancer """
    lst_des = des.copy()
    for index in list(range(6)):
        rep = input("De [" + str(index + 1) + "]:")
        if rep in ["o", "O", "ok", "OK"]:
            lance_de(lst_des, index)
    return lst_des


def lance_de(des, numero_de):
    """ lance le dé numéro numero_de """
    # le dé numéro 1 est à l'indice 0
    des[numero_de] = randint(1, 6)


def affiche_de(valeur):
    """ affiche la valeur du de """
    print(" [{}]".format(valeur), end="")


def affiche_des(des):
    """ affiche tous les dés """
    for de in des:
        print("  . ", end="")
    print()
    for de in des:
        affiche_de(de)
    print()
    for de in des:
        print(" '-'", end="")
    print("")


def affiche_lance_des(des, des_nouv):
    """affiche le lancé : des
    et le lancé : des_nouv
    """
    affiche_des(des)
    for step in des:
        print("  v ", end="")
    print("")
    affiche_des(des_nouv)


# Joueurs
def cree_joueur(pseudo):
    """ créé un joueur """
    return {"nom": pseudo, "points": 0}


def maj_point(joueur, point):
    """ Mise à jour des points du joueur """
    joueur["points"] += point


def affiche_joueur(joueur):
    """ affiche un joueur """
    nom = joueur["nom"]
    points = joueur["points"]

    print("{} à {} pts".format(nom, points))


# Points
def affiche_regle():
    """ affiche toutes les sélections possibles """
    index = 1
    for regle in g_regle_item:
        print("|{:2}|{:<21}|".format(index, regle))
        index += 1


def verifie_selection_regle(selection):
    """ Vérifie si selection est bien une valeur permise """
    if selection == None:
        return False

    if selection.isnumeric():
        return (int(selection) > 0) and (int(selection) <= len(g_regle_item))

    return False


def calcule_point(selection, des):
    """calcule les points d'une sélection dans
    la table des sélections, soit la régle
    """
    # Total des 1 (ou 2, ou 3, ...)
    if selection in list(range(1, 7)):
        pts = selection * des.count(selection)
    elif selection == 9:
        pts = 15
    elif selection in [10, 11, 12]:
        pts = 25
    elif selection == 13:
        pts = 20
    elif selection == 14:
        pts = 30
    elif selection == 15:
        pts = 40
    elif selection == 16:
        pts = 60
    elif selection == 17:
        pts = 50
    elif selection == 18:
        pts = 100
    elif selection == 19:
        pts = randint(0, 100)
    else:
        pts = 10  # points par défaut...

    print("{:<3}|pts {:<3}|{}".format(selection, pts, g_regle_item[selection - 1]))

    return pts


# Jeu
def quitter_erreur(msg):
    """ quitte sur une erreur et affiche le message msg """
    if msg != "":
        print(msg)
    exit(1)


def quitter(rep):
    """ quitter le jeu """
    if rep in ["o", "O", "oui", "OUI", "OK", "ok"]:
        print("A bientôt !!")
        exit(0)


def determine_gagnant(lst_joueur):
    """ renvoie une liste triée par ordre des points décroissants """
    return sorted(lst_joueur, key=lambda joueur: joueur["points"], reverse=True)


def affiche_podium(lst_gagnants):
    """ affiche tous les joueurs par ordre décroissant des points """
    position = 1
    for joueur in lst_gagnants:
        print(
            "- {:<2} | {:<20} | pts : {}".format(
                position, joueur["nom"], joueur["points"]
            )
        )
        position += 1


def moteur_jeu(nb_tours, lst_joueur):
    """ bouble principale du jeu """
    # Boucle sur les tours
    for tour in list(range(nb_tours)):

        # Boucle sur les joueurs
        for joueur in lst_joueur:
            cls_ecran()
            print("~~~~~~~~~~~~~~~~~")
            print("Tour {}".format(tour + 1))

            print("~~~~~~~~~~~~~~~~~")
            print("{} à toi de jouer !!\n".format(joueur["nom"]))

            print("~~~~~~~~~~~~~~~~~")
            affiche_regle()

            print("~~~~~~~~~~~~~~~~~")
            print("Lancé des dés")
            des = lance_des_initial()  # création des dés
            affiche_des(des)

            print("~~~~~~~~~~~~~~~~~")
            print("Relance des dés ? [o/n]")
            des_rel = lance_des_inter(des)
            affiche_lance_des(des, des_rel)

            print("~~~~~~~~~~~~~~~~~")
            print("Rappel des points")
            affiche_joueur(joueur)

            print("~~~~~~~~~~~~~~~~~")
            rep = input("Sélection de la combinaison:")
            rep_parsee = verifie_selection_regle(rep)

            if rep_parsee:
                pts = calcule_point(int(rep), des_rel)
                maj_point(joueur, pts)
            else:
                print("Sélection inconnue... aucun point en plus !!!")

            affiche_joueur(joueur)

            print("~~~~~~~~~~~~~~~~~")
            rep = input("Quitter le jeu ? [o/n]:")
            quitter(rep)

    # fin de boucle
    lst_gagnants = determine_gagnant(lst_joueur)
    cls_ecran()
    print("~~~~~~~~~~~~~~~~~")
    print("Podium !!")
    print("")
    affiche_podium(lst_gagnants)


def jouer():
    """ configure les principales variables pour la boucle de jeu """
    # Nombre de joueurs
    str_nb_joueur = input("Nombre de joueurs:")

    if not str_nb_joueur.isnumeric():
        quitter_erreur("Format de la saisie incorrect")

    nb_joueur = int(str_nb_joueur)

    if nb_joueur <= 0:
        quitter_erreur("Nombre de joueurs est insuffisant")

    # Création liste des joueurs
    lst_joueur = []
    for joueur in list(range(nb_joueur)):
        pseudo = input("Pseudo:")
        lst_joueur.append(cree_joueur(pseudo))

    print("")

    # Nombre de tours
    nb_tours = int(input("Nombre de tours:"))

    # Boucle du jeu
    moteur_jeu(nb_tours, lst_joueur)


if __name__ == "__main__":
    print("----------------------")
    print("Bienvenue au Strike !!")
    print("----------------------")

    print("")

    jouer()

    print("A bientôt pour une autre partie !!")
