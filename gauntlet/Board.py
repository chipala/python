import random
import Character as character

class Board:
    def __init__(self, raw, col):
        self.raw = raw
        self.col = col
        self.elements = []


    def addElement(self, x=0, y=0, element=None):
        self.elements.append({'x': x, 'y': y, 'elmt': element})


    def draw(self):
        symbol = "."
        raws = list(range(self.raw))
        cols = list(range(self.col))
        for y in raws:
            for x in cols:
                exist = False
                for element in self.elements:
                    exist = element['x'] == x and element['y'] == y
                    if exist:
                        if element['elmt'] == None:
                            element['elmt'] = character.Character('titi' + str(x + y))
                        print(f"{element['elmt'].name:10}", end='')
                        break
                if not exist:
                    print(f"{symbol:10}", end='')
            print()
