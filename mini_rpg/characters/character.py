class Character:
    def __init__(self, name, class_type):
        self.name = name
        self.class_type = class_type
        self.health = 100
        self.damage = 10
        self.healing_power = 20
        self.protection = 5
        self.weapon = None
        self.armor = None

    def attack(self, target):
        target.health -= self.damage

    def heal(self):
        self.health += self.healing_power

    def equip_weapon(self, weapon):
        self.weapon = weapon
        self.damage += weapon.damage

    def equip_armor(self, armor):
        self.armor = armor
        self.protection += armor.protection
