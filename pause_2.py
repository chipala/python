#!/usr/bin/python

import time

print("Une pause de 5 secondes va etre faite")
# Pause de 5 secondes
time.sleep(5)

# Avec une saisie
duree = input("Entrez la duree (sec):")
print("Debut de la pause de ", str(duree), " (sec)")
time.sleep(int(duree))
print("Fin")
