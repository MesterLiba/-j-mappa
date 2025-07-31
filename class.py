class Warriors():
    def __init__(self, type, health, speed, damage):
        self.type = type
        self.health = health
        self.speed = speed
        self.damage = damage
    
    def warrior_print(self):
        print(f'{self.type} warrior has {self.health} health and its speed is {self.speed} and it can damage {self.damage}')


class Spear_warrior(Warriors):
    def __init__(self):
        super().__init__('Spear', 100, 50, 120)

class Sword_warrior(Warriors):
    def __init__(self):
        super().__init__('Sword', 120, 40, 110)

class Sigma_warrior(Warriors):
    def __init__(self):
        super().__init__('Sigma', 999, 999, 999)

spear_warrior = Spear_warrior()
sword_warrior = Sword_warrior()
sigma_warrior = Sigma_warrior()


warriors =  [spear_warrior, sword_warrior, sigma_warrior]

for warriors in warriors:
    warriors.warrior_print()