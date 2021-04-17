# Description d'une classe en python

# Début de la classe
class Voiture:
    def __init__(self, arg_marque):
        self.marque = arg_marque
    
    def affiche_marque(self):
        print(self.marque)

    def regulateur(self, vitesse):
        self.vitesse = vitesse
        return vitesse 

    def __str__(self):
        return f"{self.marque} roule a {self.vitesse}"       

#fin de la classe

class Gendarme:
    def __init__(self, nom):
        self.nom = nom

    def __str__(self):
        return f"Gendarme: {self.nom}"
    
    def controle(self, voiture, vitesse):
        if (voiture.vitesse <= vitesse + 20 and voiture.vitesse > vitesse):
            print("Points perdus : 2")        
        elif (voiture.vitesse > vitesse + 20):
            print("Retrait de permis")
        else:
            print("Tout va bien :-)")
        print(f"Controle realise par {self.nom} pour la voiture {voiture.marque}")
        
# Exemple
ma_206 = Voiture("peugeot")
ma_206.affiche_marque()
allure = ma_206.regulateur(130)
print(allure)
ma_206.regulateur(150)
print(ma_206)

gg = Gendarme("Georges")
print(gg)
gg.controle(ma_206, 110)

# On peut faire la meme chose avec un dictionnaire
# mais c'est incompréhensible !!!!!!!!
def fonction_rouler(dico, marque, vitesse):
    dico[marque] = vitesse

ma_super_207 = {'peugeot' : 150, "rouler": fonction_rouler}
v_super_207 = ma_super_207['peugeot']
print(v_super_207)
ma_super_207["rouler"](ma_super_207, 'peugeot', 130)
print(ma_super_207['peugeot'])
# Fin du n'importe quoi !!!
