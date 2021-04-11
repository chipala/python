print('--------------------------------------------------------------------------------')
print("Formula one")
print('--------------------------------------------------------------------------------')

# --------------------------------------------------------------------------------
# Utiliser un DICTIONNAIRE
# --------------------------------------------------------------------------------
dict_pilote = {
	"Mercedes": ["Hamilton", "Bottas"],
	"Ferrari": [{"nom": "Vettel", "points": 10}, {"nom": "Leclerc", "points": 1}]
}

def afficher_pilote_mercedes():
	print("Afficher les pilotes mercedes")
	print(dict_pilote.get("Mercedes"))


# On peut faire mieux :-)
def afficher_pilote(ecurie):
	if ecurie in ["Mercedes", "Ferrari"]:
		print("Les pilotes de",ecurie,"sont :")
		print(dict_pilote[ecurie])
	else:
		print("Tu tapes n'importe quoi :-P")


print()
afficher_pilote("Mercedes")

print()
afficher_pilote("Mercedes")
afficher_pilote("Titi")

print()
afficher_pilote("Mercedes")
afficher_pilote("Ferrari")

ecurie = input("Entrez un nom d'ecurie:")
afficher_pilote(ecurie)
