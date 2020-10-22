# Course: CS 30
# Period: 1
# Date created: 2020-09-28
# Date last modified: 2020-10-19
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
    
    def __eq__(self, other):
        return other and self.name == other.name
    
    @staticmethod
    def Radio():
        return Item(
            name="radio",
            description="Used to signal for help",
            uses=1
        )


class Weapon(Item):
    """Class for the weapon type of item used to deal damage"""
    def __init__(self, name, description, uses, damage):
        super().__init__(name, description, uses)
        self.damage = damage
    
    @staticmethod
    def Knife():
        return Weapon(
            name="knife",
            description="Small Weapon",
            damage=25,
            uses=15
        )
    
    @staticmethod
    def Chainsaw():
        return Weapon(
            name="chainsaw",
            description="High Damage Weapon",
            damage=125,
            uses=2
        )
    
    @staticmethod
    def Axe():
        return Weapon(
            name="axe",
            description="Medium Weapon",
            damage=125,
            uses=2
        )
    
    @staticmethod
    def Sword():
        return Weapon(
            name="sword",
            description="Large Weapon",
            damage=75,
            uses=10
        )


class Heal(Item):
    """Class for the characteristics of a healable item"""
    def __init__(self, name, description, uses, add_health):
        super().__init__(name, description, uses)
        self.add_health = add_health
    
    @staticmethod
    def Medkit():
        return Heal(
            name="medkit",
            description="Large healable item that can be found",
            uses=1,
            add_health=100
        )
    
    @staticmethod
    def Bandages():
        """Method for a bandage item with name, description, uses, and the 
        amount of health that will be added when used
        """
        return Heal(
            name="bandages",
            description="Small healable item that can be found",
            uses=1,
            add_health=50
        )
