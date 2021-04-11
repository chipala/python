print ()
print ("421")
print ()

from random import randint

nt=int(input("Nombre de tours:"))

to=0
j=0
o=0
jt=0
ot=0

while to<nt:

    to=to+1

    

    print

    print("tour ",to) # ou bien print("tour",to)

    print

    print ("A l'ordinateur:")

    print


    t=0

    a=randint(1,6)
    b=randint(1,6)
    c=randint(1,6)


    while t<2:

        t=t+1

        print
        
        print (a,b,c)

        print

        
       

        if a+b==2 and (c<5 and c>1 and t==1 or c<4 and c>1 and t==2):
            c=randint(1,6)
                
        if a+c==2 and (b<5 and b>1 and t==1 or b<4 and b>1 and t==2):
            b=randint(1,6)
        
        if c+b==2 and (a<5 and a>1 and t==1 or a<4 and a>1 and t==2):
            a=randint(1,6)
        
        if a==b and a>2 and c!=b:
            c=randint(1,6)

        if a==c and a>2 and b!=a:
            b=randint(1,6)

        if c==b and c>2 and a!=c:
            a=randint(1,6)

        if a+b==3 and c>1 and c!=4 and t==1:
            c=randint(1,6)

        if a+c==3 and b>1 and b!=4 and t==1:
            b=randint(1,6)

        if c+b==3 and a>1 and a!=4 and t==1:
            a=randint(1,6)

        if a+b==3 and c>1 and c!=4 and c!=2 and t==2:
            c=randint(1,6)

        if a+c==3 and b>1 and b!=4 and b!=2 and t==2:
            b=randint(1,6)

        if c+b==3 and a>1 and a!=4 and a!=2 and t==2:
            a=randint(1,6)

        if a==4 and b==2 and (c==6 or c==5 or c==2):
            c=randint(1,6)

        if a==4 and c==2 and (b==6 or b==5 or b==2):
            b=randint(1,6)        

        if b==4 and b==2 and (a==6 or a==5 or a==2):
            a=randint(1,6)        

    if a+b+c==3:
        o=o+7

    if a==b and b==c and a>1:
        o=o+a

    if a+b+c==7 and a!=b and b!=c and c!=a:
        o=o+8

    if a+b==2 and c>1:
        o=o+c

    if a+c==2 and b>1:
        o=o+b

    if b+c==2 and a>1:
        o=o+a

    if a==c+1 and b==a+1 or a==b+1 and b==c+1 or a==b-1 and b==c-1 or a==c+1 and c==b+1 or a==c-1 and c==b-1 or a==b+1 and c==a+1 or b==c-1 and a==c+1:
        o=o+2

    if a+b+c==5 and a!=3 and b!=3 and c!=3:
        o=o+4

    print
        
    print (a,b,c)

    print

    print ("L'ordinateur a",o,"points")

        
  










    print

    print ("Au joueur:")

    print

    t=0

    a=randint(1,6)
    b=randint(1,6)
    c=randint(1,6)


    while t<2:

        t=t+1

        print
        
        print (a,b,c)

        print

        rd1=input("Relancer de 1 (o/n)")

        if rd1=="o":
            a=randint(1,6)
    

        rd1=input("Relancer de 2 (o/n)")

        if rd1=="o":
            b=randint(1,6)
   

        rd1=input("Relancer de 3 (o/n)")

        if rd1=="o":
            c=randint(1,6)

    print (a,b,c)

    print

    if a+b+c==3:
        
        j=j+7

    if a==b and b==c and a>1:
        j=j+a

    if a+b+c==7 and a!=b and b!=c and c!=a:
        j=j+8

    if a+b==2 and c>1:
        j=j+c

    if a+c==2 and b>1:
        j=j+b

    if b+c==2 and a>1:
        j=j+a

    if a==c+1 and b==a+1 or a==b+1 and b==c+1 or a==b-1 and b==c-1 or a==c+1 and c==b+1 or a==c-1 and c==b-1 or a==b+1 and c==a+1 or b==c-1 and a==c+1:
        j=j+2

    if a+b+c==5 and a!=3 and b!=3 and c!=3:
        j=j+4


    print ("Vous avez",j,"points")

    print
        
    jt=jt+j    
    
   

           

            

        



