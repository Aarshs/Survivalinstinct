# Course: CS 30
# Period: 1
# Date created: 2020-09-28
# Date last modified: 2020-10-25
# Name: Aarsh Shah
# Description: Creates classes and sub-classes for the different
# types of items.


def item_usable(item):
    """Checks to see if an item is still usable."""
    if isinstance(item, (Heal, Weapon)):
        return item.uses != 0
    else:
        return True


class Item():
    """A parent class for the characteristic of inventory items."""
    def __init__(self, name, description, uses):
        """Sets variables up for item name, description and uses."""
        self.name = name
        self.description = description
        self.uses = uses

    def __str__(self):
        """Returns the name of each item."""
        return self.name

    def __eq__(self, other):
        """Called when comparing two items, returns if the items have the same
        name.
        """
        return other and self.name == other.name


class Weapon(Item):
    """Class for the weapon type of item used to deal damage."""
    def __init__(self, name, description, uses, damage):
        super().__init__(name, description, uses)
        self.damage = damage

    @staticmethod
    def Knife():
        """Method for the knife weapon with the name, description, uses, and
        the amount of damage it does.
        """
        return Weapon(
            name="knife",
            description="Small Weapon that does 25 damage, it never breaks",
            damage=25,
            uses=1000000
        )

    @staticmethod
    def Chainsaw():
        """Method for the chainsaw weapon with the name, description, uses, and
        the amount of damage it does.
        """
        return Weapon(
            name="chainsaw",
            description="High Damage Weapon doing 125 damage",
            damage=125,
            uses=2
        )

    @staticmethod
    def Axe():
        """Method for the axe weapon with the name, description, uses, and
        the amount of damage it does.
        """
        return Weapon(
            name="axe",
            description="Simple but effective Weapon, doing 90 damage",
            damage=90,
            uses=2
        )

    @staticmethod
    def Sword():
        """Method for the sword weapon with the name, description, uses, and
        the amount of damage it does.
        """
        return Weapon(
            name="sword",
            description="Large Weapon that does 75 damage",
            damage=75,
            uses=8
        )


class Heal(Item):
    """Class for the characteristics of a healable item."""
    def __init__(self, name, description, uses, add_health):
        super().__init__(name, description, uses)
        self.add_health = add_health

    @staticmethod
    def Medkit():
        """Method for the medkit item with name, description, uses, and the
        amount of health that will be added when used.
        """
        return Heal(
            name="medkit",
            description="Large healable item, restoring 100 health",
            uses=1,
            add_health=100
        )

    @staticmethod
    def Bandages():
        """Method for a bandage item with name, description, uses, and the
        amount of health that will be added when used.
        """
        return Heal(
            name="bandages",
            description="Small healable item, restoring 50 health",
            uses=2,
            add_health=50
        )
