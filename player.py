# Course: CS 30
# Period: 1
# Date created: 2020-09-15
# Date last modified: 2020-10-25
# Name: Aarsh Shah
# Description: Creates a class for the charcateristics of the player.

from items import *


class Player:
    """Player class with inventory, health, and equipped item."""
    def __init__(self, inventory, health, item):
        self.inventory = inventory
        self.health = health
        self.equipped_item = item
        self.random = ["Escaped", "Failed"]

    @staticmethod
    def default():
        """The items that the player starts with and their starting health."""
        return Player([Weapon.Knife(), Heal.Bandages()], 200, Weapon.Knife())

    def alive(self):
        """The game continues as long as the player has more 0 health."""
        return self.health > 0

    def inventory_info(self):
        """Prints the inventory of items and their descriptions."""
        message = ""
        message = "Your Inventory:\n"
        for self.item in self.inventory:
            message += "- " + str(self.item).title(
            ) + f""":\n - {self.item.description}
 - Uses: {self.item.uses}\n"""
        return message
