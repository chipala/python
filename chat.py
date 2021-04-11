
class Chat:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __str__(self):
        return "Je m'appelle {} et j'ai {} an(s)".format(self.nom, str(self.age))

    def fairePipi(self):
        return self.__str__() + " et je fais pipi"

    def faireCaca(self):
        return self.__str__() + " et je fais caca aussi"

    def faireDodo(self):
        return self.__str__() + " et souvent je dors"
    
    def direBonjour(sef):
        print(f"Coucou frère")


# Main 
chat_titi = Chat('titi', 10)
print(chat_titi)
print(chat_titi.fairePipi())

chat_gros_minet = Chat('gros_minet', 15)
print(chat_gros_minet.faireDodo())

chat_gros_minet.direBonjour()
