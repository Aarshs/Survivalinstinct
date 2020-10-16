# Course: CS 30
# Period: 1
# Date created: 2020-09-28
# Date last modified: 2020-10-15
# Name: Aarsh Shah
# Description: Creates classes and sub-classes for the different
# types of items.


class Item():
    def __init__(self, name, description, uses):
        self.name = name
        self.description = description
        self.uses = uses

    def __str__(self):
        return self.name


class Ammo(Item):
    def __init__(self):
        self.name = "Flare Ammo"
        self.description = "Ammo needed to use the Flaregun"
        self.uses = 1


class Flaregun(Item):
    def __init__(self):
        self.name = "Flaregun"
        self.name = "Used to signal for help"
        self.uses = 0


class Weapon(Item):
    def __init__(self, damage):
        self.damage = damage


class Knife(Weapon):
    def __init__(self):
        self.name = "Knife"
        self.description = "Small Weapon"
        self.damage = 25
        self.uses = 15


class Chainsaw(Weapon):
    def __init__(self):
        self.name = "Chainsaw"
        self.description = "High Damage Weapon"
        self.damage = 125
        self.uses = 2


class Axe(Weapon):
    def __init__(self):
        self.name = "Axe"
        self.description = "Medium Weapon"
        self.damage = 125
        self.uses = 2


class Sword(Weapon):
    def __init__(self):
        self.name = "Sword"
        self.description = "Large Weapon"
        self.damage = 75
        self.uses = 10


class Heal(Item):
    def __init__(self, add_health):
        self.add_health = add_health


class Medkit(Heal):
    def __init__(self):
        self.name = "Medkit"
        self.description = "Large healable item that can be found"
        self.uses = 1
        self.add_health = 100


class Bandages(Heal):
    def __init__(self):
        self.name = "Bandages"
        self.description = "Small healable item that can be found"
        self.uses = 1
        self.add_health = 50
