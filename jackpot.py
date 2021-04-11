from random import randint

CAPITAL=100

def jouer(dico_joueur):
    print(f"Joueur {dico_joueur['nom']} va jouer !!")
    print(f"Vous avez {dico_joueur['point']} euros")

    try:
        m=input("Mise:")
        m=int(m)
    except:
        print("Entrez un nombre")
        return
 
    dico_joueur["point"] -= m

    a=randint(1,7)
    b=randint(1,7)
    c=randint(1,7)

    print(a,b,c)

    if a==b and a!=c and a!=7 or a==c and a!=b and a!=7 or b==c and b!=a and b!=7:
        dico_joueur["point"]=dico_joueur["point"]+m
    
    if a==b and b==c and a!=7:
        dico_joueur["point"]=dico_joueur["point"]+m*10
    
    if a==b and a!=c and a==7 or a==c and a!=b and a==7 or b==c and b!=a and b==7:
        dico_joueur["point"]=dico_joueur["point"]+m*9
    
    if a==b and b==c and a==7:
        dico_joueur["point"]=dico_joueur["point"]+m*99
    
    if a==7 or b==7 or c==7:
        dico_joueur["point"]=dico_joueur["point"]+m

    print(f'Il vous reste {dico_joueur["point"]} euros')




# Main function
liste_joueur = [
    {"nom": "jacques", "point": CAPITAL},
    {"nom": "xavier", "point": CAPITAL}
]

print(liste_joueur)

def jouer_jack():
    t=""
    while t!="n":
        for joueur_courant in liste_joueur:
            jouer(joueur_courant)
        try:
            t=input("Continuer (o/n)")
        except:
            print("Entrez [o/n]")

#jouer_jack()
    
# =================================

def jackpot(mise):
    a=randint(1,7)
    b=randint(1,7)
    c=randint(1,7)

    print(a,b,c)

    point = 0

    if a==b and a!=c and a!=7 or a==c and a!=b and a!=7 or b==c and b!=a and b!=7:
        point = mise
    
    if a==b and b==c and a!=7:
        point = mise * 10
    
    if a==b and a!=c and a==7 or a==c and a!=b and a==7 or b==c and b!=a and b==7:
        point = mise * 9
    
    if a==b and b==c and a==7:
        point = mise * 99

    if a==7 or b==7 or c==7:
        point += mise

    return point


class Joueur:
    def __init__(self, nom, point, jeu):
        self.nom = nom
        self.point = point
        self.jeu = jeu
    
    def jouer(self, mise):
        print(f"{self.nom} a joué {mise} euro(s)")
        self.point = self.point - mise + self.jeu(mise)

    def jouer_a(self, jeu):
        self.jeu = jeu

    def __str__(self):
        return f"{self.nom} a {self.point} euro(s)"

jacques = Joueur("jacques", CAPITAL, jackpot)
print(jacques)
jacques.jouer(50)
print(jacques)