# Course: CS 30
# Period: 1
# Date created: 2020-09-15
# Date last modified: 2020-10-15
# Name: Aarsh Shah
# Description: Creates a class for the charcateristics of the player.

import items


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

