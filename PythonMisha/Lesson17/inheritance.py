class Character:
    def __init__(self, name, hp, stamina):
        self.name = name
        self.hp = hp
        self.stamina = stamina

    def voice(self):
        print("HAAA")

class Enemy (Character):
    def __init__(self, name, hp, stamina):
        super().__init__(name, hp, stamina)

class NPC (Character):
    def __init__(self, name, age, hp, stamina):
        super().__init__(name, hp, stamina)
        self.age = age

class Player (Character):
    def __init__(self, name, age, hp, stamina):
        super().__init__(name, hp, stamina)
        self.age = age

    def voice(self):
        print("I am player")

player = Player("Alex", 12, 12, 12)
player.voice()

enemy = Enemy("ghoul", 100, 100)
enemy.voice()

class Stats:
    def __init__(self, name, hp, stamina):
        self.name = name
        self.hp = hp
        self.stamina = stamina

class Player:
    def __init__(self, age, stats):
        self.age = age
        self.stats = stats