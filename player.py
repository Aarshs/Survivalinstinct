# Course: CS 30
# Period: 1
# Date created: 2020-09-15
# Date last modified: 2020-10-19
# Name: Aarsh Shah
# Description: Creates a class for the charcateristics of the player.

import items


class Player:
    """Player class with inventory"""
    def __init__(self, inventory, health):
        self.inventory = inventory
        self.health = health
        self.victory = False

    @staticmethod
    def default():
        """The items that the player starts with and their starting health."""
        return Player([items.Knife(), items.Flaregun(), items.Bandages()], 200)
        # return Player({
        #     "Weapons": [items.Knife(), items.Flaregun()],
        #     "Heals": [items.Bandages()]},
        #     200
        # )

    def alive(self):
        """The game continues as long as the player has more 0 health"""
        return self.health > 0

    def print_inventory(self):
        """Prints the inventory of items"""
        message = ""
        message = "Your Inventory:\n"
        for item in self.inventory:
            message += "- " + str(item) + "\n"
        return message
