from random import randint

def lancer_de():
    l = []
    for de in list(range(6)):
        l.append(randint(1,6))
    return l

def relancer_de(lance):
    for de in list(range(6)):
        r1=input(f"Relancer dé {de+1} (o/n)")    
        if r1=="o":
            lance[de]=randint(1,6)

def affiche_des(lance):
    print()    
    print(lance)
    print()


pts1=0
pts2=0

nt=int(input("Nombre de tours:"))

tour=0

liste1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
liste2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

while tour<nt:

    tour=tour+1

    print()
    print("Joueur 1")
    print()

    print()    
    lance = lancer_de()
    print(lance)
    print()

    t=0

    while t<2:
        t=t+1

        # relancer les dés
        relancer_de(lance)
        
        # afficher les dés
        affiche_des(lance)
        
    if liste1[0]==1:
        print("1:  Total 1")
    if liste1[1]==2:
        print("2:  Total 2")
    if liste1[2]==3:
        print("3:  Total 3")
    if liste1[3]==4:
        print("4:  Total 4")
    if liste1[4]==5:
        print("5:  Total 5")
    if liste1[5]==6:
        print("6:  Total 6")
    if liste1[6]==7:
        print("7:  Brelan")
    if liste1[7]==8:
        print("8:  carré")
    if liste1[8]==9:
        print("9:  Full 15")
    if liste1[9]==10:
        print("10: Triple paire 25")
    if liste1[10]==11:
        print("11: Double brelan 25")
    if liste1[11]==12:
        print("12: Carré/Paire 25")
    if liste1[12]==13:
        print("13: Petite suite 20")
    if liste1[13]==14:
        print("14: Suite ordonée 30")

    if liste1[14]==15:
        print("15: Suite moyenne 40")
    if liste1[15]==16:
        print("16: Grande suite 60")
    if liste1[16]==17:
        print("17: Yathzee 50")
    if liste1[17]==18:
        print("18: Strike 100")
    if liste1[18]==19:
        print("19: Chance")

    ch=0
    while ch==0 or liste1[ch-1]==0:

        ch=input("Votre choix:")
        ch=int(ch)
    
    liste1[ch-1]=0

    

    
    print()
    
    pt=input("Points:")
    
    
    if ch==19:
        pt=a+b+c+d+e+f
    
    if ch==10 or ch==11 or ch==12:
        pt=25

    if ch==13:
        pt=20


    pt=int(pt)

    pts1=pts1+pt

    print("Vous avez ",pts1," points")
    print()
    print("Joueur 1:",pts1," points")
    print("Joueur 2:",pts2," points")

    print()
    print("Joueur 2")
    print()
    
    a=randint(1,6)
    b=randint(1,6)
    c=randint(1,6)
    d=randint(1,6)
    e=randint(1,6)
    f=randint(1,6)

    print()    
    print (a,b,c,d,e,f)
    print()

    t=0

    while t<2:

        t=t+1

        r1=input("Relancer de 1 (o/n)")
        r2=input("Relancer de 2 (o/n)")
        r3=input("Relancer de 3 (o/n)")
        r4=input("Relancer de 4 (o/n)")
        r5=input("Relancer de 5 (o/n)")
        r6=input("Relancer de 6 (o/n)")

        if r1=="o":
            a=randint(1,6)

        if r2=="o":
            b=randint(1,6)

        if r3=="o":
            c=randint(1,6)

        if r4=="o":
            d=randint(1,6)

        if r5=="o":
            e=randint(1,6)

        if r6=="o":
            f=randint(1,6)

        print()    
        print (a,b,c,d,e,f)
        print()

    if liste2[0]==1:
        print("1:  Total 1")
    if liste2[1]==2:
        print("2:  Total 2")
    if liste2[2]==3:
        print("3:  Total 3")
    if liste2[3]==4:
        print("4:  Total 4")
    if liste2[4]==5:
        print("5:  Total 5")
    if liste2[5]==6:
        print("6:  Total 6")
    if liste2[6]==7:
        print("7:  Brelan")
    if liste2[7]==8:
        print("8:  carré")
    if liste2[8]==9:
        print("9:  Full 15")
    if liste2[9]==10:
        print("10: Triple paire 25")
    if liste2[10]==11:
        print("11: Double brelan 25")
    if liste2[11]==12:
        print("12: Carré/Paire 25")
    if liste2[12]==13:
        print("13: Petite suite 20")
    if liste2[13]==14:
        print("14: Suite ordonée 30")

    if liste2[14]==15:
        print("15: Suite moyenne 40")
    if liste2[15]==16:
        print("16: Grande suite 60")
    if liste2[16]==17:
        print("17: Yathzee 50")
    if liste2[17]==18:
        print("18: Strike 100")
    if liste2[18]==19:
        print("19: Chance")


    ch=0
    while ch==0 or liste2[ch-1]==0:

        ch=input("Votre choix:")
        ch=int(ch)
    
    liste2[ch-1]=0

    

    
    print()
    
    pt=input("Points:")
    
   

   

    if ch==19:
        pt=a+b+c+d+e+f


    if ch==10 or ch==11 or ch==12:
        pt=25

    if ch==13:
        pt=20
        
    pt=int(pt)

    pts2=pts2+pt

    print("Vous avez ",pts2," points")
    print()
    print("Joueur 1:",pts1," points")
    print("Joueur 2:",pts2," points")




print()
print("Fin")
