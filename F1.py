from random import randint

print('--------------------------------------------------------------------------------')
print("Formula one")
print('--------------------------------------------------------------------------------')

# --------------------------------------------------------------------------------
# Utiliser une LISTE
# --------------------------------------------------------------------------------
print("p$(1)=\"Hamilton\"")
print("p$(2)=\"Bottas\"")

# Pour faite la meme chose
# Tu peux utiliser une LISTE
# C'est une structure de donnee en python

liste_pilotes = ["Hamilton", "Bottas","Vettel"]
print(liste_pilotes)

print(liste_pilotes[0])
print(liste_pilotes[2])


for un_pilote in liste_pilotes:
	print(un_pilote)
# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------
# Utiliser un DICTIONNAIRE
# --------------------------------------------------------------------------------
dict_pilote = {
	"Mercedes": ["Hamilton", "Bottas"],
	"Ferrari": [{"nom": "Vettel", "points": 10}, {"nom": "Leclerc", "points": 1}]
}

print(dict_pilote)
print(dict_pilote["Mercedes"])
print(dict_pilote["Mercedes"][0])
print(dict_pilote["Mercedes"][1])
print(dict_pilote["Ferrari"])
print(dict_pilote["Ferrari"][0])
print(dict_pilote["Ferrari"][1])
print(dict_pilote["Ferrari"][0]["nom"])

def afficher_pilote_mercedes():
	print("Afficher les pilotes mercedes")
	print(dict_pilote.get("Mercedes"))


afficher_pilote_mercedes()

# On peut faire mieux :-)
def afficher_pilote(ecurie):
	if ecurie in ["Mercedes", "Ferrari"]:
		print("Les pilotes de",ecurie,"sont :")
		print(dict_pilote[ecurie])
	else:
		print("Tu tapes n'importe quoi :-P")


afficher_pilote("Mercedes")
afficher_pilote("Titi")
afficher_pilote("Ferrari")

print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")

p= ["Hamilton", "Bottas","Verstappen","Leclerc","Vettel","Sainz","Gasly","Albon","Ricciardo","Perez","Norris","Raikkonen","Kvyat","Hulkenberg","Stroll","Magnussen","Giovinazzi","Grosjean","Kubica","Russel"]
np=[1.25,1.26,1.27,1.28,1.29,1.3,1.31,1.32,1.33,1.34,1.35,1.36,1.37,1.38,1.39,1.4,1.41,1.42,1.43,1.44]
i=0
t=[]
while i<20:
	
	t=t+[np[i]+randint(1,100)/1000]
	
	i=i+1


pole = [
	(t[0],p[0]),
	(t[1],p[1]),
	(t[2],p[2]),
	(t[3],p[3]),
	(t[4],p[4]),
	(t[5],p[5]),
	(t[6],p[6]),
	(t[7],p[7]),
	(t[8],p[8]),
	(t[9],p[9]),
	(t[10],p[10]),
	(t[11],p[11]),
	(t[12],p[12]),
	(t[13],p[13]),
	(t[14],p[14]),
	(t[15],p[15]),
	(t[16],p[16]),
	(t[17],p[17]),
	(t[18],p[18]),
	(t[19],p[19]),	
]

pp=sorted(pole)


i=0
while i<20:
	
	print(i+1,pp[i])
	i=i+1

nt=1










