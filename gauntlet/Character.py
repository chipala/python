import Capacity as m_capacity

class Character:
    def __init__(self, name):
        self.name = name
        self.life = 0
        self.capacity = []

    def __str__(self):
        return \
            f"Name:{self.name:20} Life:{self.life}"


    def addCapacity(self, capacity):
        self.capacity.append(capacity)


    def listCapacity(self):
        for capacity in self.capacity:
            print(f"{capacity}")


class Wizard(Character):
    def __init__(self, name):
        super().__init__(name)


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
    

class Elf(Character):
    def __init__(self, name):
        super().__init__(name)
