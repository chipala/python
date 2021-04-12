print ("j'ai reussi !")

mon_message = "Bravo !!" # variable globale !!
print(f"{mon_message}") # f-string, permet d'afficher la valeur d'une variable grace aux {} == exemple ==> {<ma_variable>}

class RappelClass: # nom de la classe, ou symbole, ou type
    def __init__(self, arg1, arg2): # constructeur de la classe, c'est comme cela qu'on créé des objets
                                    # classe == la recette
                                    # object == le gâteau que l'on fait grace à la recette :-)
        self.arg1 = arg1 # self.arg1 est une propriété de la classe, on copie la valeur de arg1
        self.arg2 = arg2
        
    
    def une_method(self, arg1): # on parle de méthode (faut voir ça comme des fonctions mais pour les objets :-)
        print(f"{arg1} est l'argument de la méthode appelée method")
        pass # c'est un mot-clef python pour dire... ne fais rien :-)

    def une_fonction(self, patate):
        print("une_fonction prend en argument patate")
        print(patate)
        print("c'est rigolo")

    variable_de_classe = "C'est rigolo les classes :-)"

# Utilisation de la classe : RappelClass
mon_objet = RappelClass("mon_arg1", "mon_arg2") # création d'un objet identifié par la variable mon_objet
                                                # mon_objet dispose des caractéristiques définies par RappelClass
                                                # RappelClass(...) <= permet de faire appel à __init__(...)
                                                # qui va retourner un objet (construit selon la recette RappelClass)
                                                # le gâteau... construit depuis la recette :-)

print(mon_objet.arg1) # on accède à la propriété arg1 de mon_objet et on l'affiche
print(mon_objet.arg2)

mon_objet.une_method("coucou") # appel à la méthode nommée une_method!!
mon_objet.une_fonction("le lundi, le mardi...") # appel à la méthode une_fonction
