# Course: CS 30
# Period: 1
# Date created: 2020-09-15
# Date last modified: 2020-10-16
# Name: Aarsh Shah
# Description: Creates a class for the charcateristics of the player.

import items

inventoryad = [items.knife, items.flaregun, items.bandages]

class Player:
    """Player class with inventory"""
    def __init__(self, inventory, health, victory):
        self.inventory = inventory
        self.health = health
        self.victory = victory

    def attributes(self):
        # The items that the player starts with and their starting health.
        self.inventory = [items.knife(), items.flaregun(), items.bandages()]
        self.health = 200
        self.victory = False

    def alive(self):
        """The game continues as long as the player has more 0 health"""
        return self.health > 0

    def pickup_items(self):
        """Adds items to the player's inventory when they are found"""
        # Adds the found item to the player's inventory
        self.inventory.append()

def print_inventory():
        """Prints the inventory of items"""
        print("Your Inventory:")
        for item in inventoryad:
            print("- " + str(item))