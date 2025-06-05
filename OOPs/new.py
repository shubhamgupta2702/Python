class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_enemy(self):
        print(f"{self.name} attacks with power {self.attack}")


warrior = Character("Thor", 100, 70)
mage = Character("Gandalf", 80, 70)
MCU = Character("Iron Man", 100, 70)

warrior.attack_enemy()
mage.attack_enemy()
MCU.attack_enemy()


'''
1 - classes and objects
2 - inheritence
3 - encapsulation
4 - abstraction
5 - polymorphism
'''