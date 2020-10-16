# Course: CS 30
# Period: 1
# Date created: 2020-09-15
# Date last modified: 2020-10-15
# Name: Aarsh Shah
# Description: Creates a class for the charcateristics of the player.

import items
import main


class Player:
    """Player class with inventory"""
    def __init__(self):
        # The items that the player starts with
        self.inventory = [items.Knife(), items.Flaregun(), items.Bandages()]
        self.health = 200
        self.victory = False

    def alive(self):
        """The game continues as long as the player has more 0 health"""
        return self.health > 0

    def print_inventory(self):
            """Prints the inventory of items"""
            print("Your Inventory:")
            for item in self.inventory:
                print("- " + str(item))

    def pickup_items(self):
        """Adds items to the player's inventory when they are found"""
        # define the position in the ship
        position = 1
        # Adds the found item to the player's inventory
        current_inventory = self.inventory
        position.add_inventory(current_inventory)
