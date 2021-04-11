print("--------------------------------------------------------------------------------")
print("Formula one")
print("--------------------------------------------------------------------------------")

# --------------------------------------------------------------------------------
# Utiliser une CLASSE
# --------------------------------------------------------------------------------
class Pilote:
	"""A simple example class"""
	nom = "inconnu"
	point = 0    
	niveau = 0


	def __init__(self, nom, point, niveau):
		self.nom = nom
		self.point = point
		self.niveau = niveau

	def afficher_niveau():
		print(self.niveau)


	def __str__(self):
		return self.nom + '[' + str(self.point) + ']' + '(' + str(self.niveau) + ')'


liste_pilote = [Pilote("Hamilton", 80, 100), Pilote("Bottas", 60, 50)]


for e_pilote in liste_pilote:
	print("Je suis {} et j'ai {} point(s) et mon niveau est {}".format(e_pilote.nom,e_pilote.point,e_pilote.niveau))


pilote_jack = Pilote("Jacques", 100, 1000)
print(pilote_jack.nom)

point_jack = pilote_jack.point
print(point_jack)

print(pilote_jack.niveau)

print(pilote_jack)

for pilote in liste_pilote:
	print(pilote)

