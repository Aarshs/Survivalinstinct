# Course: CS 30
# Period: 1
# Date created: 2020-09-28
# Date last modified: 2020-10-16
# Name: Aarsh Shah
# Description: Creates classes and sub-classes for the different
# types of items.


class Item():
    """A parent class for the characteristic of a inventory items"""
    def __init__(self, name, description, uses):
        self.name = name
        self.description = description
        self.uses = uses

    def __str__(self):
        """Returns the name of each item"""
        return self.name


class Ammo(Item):
    """Sub-class for the characteristics of the flaregun ammo"""
    def __init__(self):
        self.name = "Flare Ammo"
        self.description = "Ammo needed to use the Flaregun"
        self.uses = 1


class Flaregun(Item):
    """Class for flaregun item with name, description, and uses"""
    def __init__(self):
        self.name = "Flaregun"
        self.name = "Used to signal for help"
        self.uses = 0


flaregun = Flaregun.name


class Weapon(Item):
    """Sub-Class for the weapon type of item used to deal damage"""
    def __init__(self, damage):
        self.damage = damage


class Knife(Weapon):
    """Class for the knife weapon with name, description, damage, and uses"""
    def __init__(self):
        self.name = "Knife"
        self.description = "Small Weapon"
        self.damage = 25
        self.uses = 15


knife = Knife()


class Chainsaw(Weapon):
    def __init__(self):
        self.name = "Chainsaw"
        self.description = "High Damage Weapon"
        self.damage = 125
        self.uses = 2


chainsaw = Chainsaw()


class Axe(Weapon):
    def __init__(self):
        self.name = "Axe"
        self.description = "Medium Weapon"
        self.damage = 125
        self.uses = 2


axe = Axe()


class Sword(Weapon):
    def __init__(self):
        self.name = "Sword"
        self.description = "Large Weapon"
        self.damage = 75
        self.uses = 10


sword = Sword()


class Heal(Item):
    def __init__(self, add_health):
        self.add_health = add_health


class Medkit(Heal):
    def __init__(self):
        self.name = "Medkit"
        self.description = "Large healable item that can be found"
        self.uses = 1
        self.add_health = 100


medkit = Medkit()


class Bandages(Heal):
    def __init__(self):
        self.name = "Bandages"
        self.description = "Small healable item that can be found"
        self.uses = 1
        self.add_health = 50


bandages = Bandages()
