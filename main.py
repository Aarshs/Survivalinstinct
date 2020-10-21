# Course: CS 30
# Period: 1
# Date created: 2020-10-08
# Date last modified: 2020-10-19
# Name: Aarsh Shah
# Description: Imports modules/ classes and creates a map with different game
# tiles with user inputted movement.

from colorama import init
from tabulate import tabulate
from copy import deepcopy
from items import Item
from map import Maps
from os import system
from player import Player
import menu
import random
from villian import Villian


class Game:
    """A class that allows the game to be ran taking user inputs to move your
    character"""
    def __init__(self):
        """Sets variables for the starting map and starting position"""
        self.map = Maps()
        self.change_map(self.map.large)
        self.player = Player.default()
        self.pending_message = ""
        self.map_hotspots = [{
            "map": self.map.large,
            "new_map": self.map.cave,
            "pos": [1, 3],
        }, {
            "map": self.map.cave,
            "new_map": self.map.large,
            "pos": [0, 0],
        }, {
            "map": self.map.large,
            "new_map": self.map.plane,
            "pos": [6, 2],
        }, {
            "map": self.map.plane,
            "new_map": self.map.large,
            "pos": [5, 1],
        }]

    def change_map(self, new_map):
        "Sets what the current map and position is"
        self.current_map = new_map["locations"]
        self.item_map = new_map["items"]
        self.current_enemy = new_map["enemies"]
        self.pos = deepcopy(new_map["default_pos"])

    def mainmenu(self):
        """Allows for user inputs as the map is printed and reacts according to
        the users inputs"""
        map_copy = deepcopy(self.current_map)
        # Sets the marker to indicate the player as "You"
        map_copy[self.pos[0]][self.pos[1]] = "You"

        system('cls')
        # Prints the map array in a fancy format using the tabulate library.
        print(tabulate(map_copy, tablefmt="fancy_grid"))
        if self.pending_message != "":
            print(self.pending_message)
            self.pending_message = ""
        # Takes user input on where they want to move
        selector = input("""\
Choose a direction (Use WASD):
Left, Right, Up, or Down?
> \
""").lower()
        # Checks to see where the user wants to move.
        old_pos = self.pos[:]
        if selector == "a":
            self.pos[1] += -1
        elif selector == "d":
            self.pos[1] += 1
        elif selector == "w":
            self.pos[0] += -1
        elif selector == "s":
            self.pos[0] += 1
        elif selector == "quit":
            quit()
        else:
            print("Please Try Again")

        self.move_map()
        self.add_items()
        self.attacking()

        # Prevents user from going out of the map.
        if (self.pos[0] < 0 or self.pos[0] >= len(self.current_map)
                or self.pos[1] < 0
                or self.pos[1] >= len(self.current_map[self.pos[0]])):
            self.pos = old_pos

        # Allows the user to quit the game if the go to the end.
        if self.current_map == self.map.large["locations"] and self.pos[
                0] == 0 and self.pos[1] == 0:
            quit()

    def move_map(self):
        for hotspot in self.map_hotspots:
            if self.current_map == hotspot["map"][
                    "locations"] and self.pos == hotspot["pos"]:
                self.change_map(hotspot["new_map"])

    def add_items(self):
        """Adds items to character if they come accross it in the map."""
        y, x = self.pos
        item = self.item_map[y][x]
        if item != None and isinstance(item, Item):
            self.item_map[y][x] = None
            self.player.inventory.append(item)
            self.pending_message = self.player.inventory_info()

    def attacking(self):
        """Allows the players to attack the enemy ."""
        y, x = self.pos
        enemy = self.current_enemy[y][x]
        if enemy != None and isinstance(enemy, Villian):
            self.item_map[y][x] = None
            self.pending_message = self.menu1()

    def menu1(self):
        option = input("""\
What do you want to do?
1. Run
2. Equip
> \
""").lower()
        if option in ("run", "1"):
            print("You are attempting to run")
            random.choice(self.player.random)
            if self.player.random == "Escaped":
                y, x = self.pos
                self.current_enemy[y][x] = None
                return "You got away"
                # Add code to make the enemy die/ disappear
            elif self.player.random == "Failed":
                option = "equip"
        if option in ("equip", "2"):
            self.equip()
        elif option == "quit":
            quit()
        else:
            print("Please Try again")

    def equip(self):
        print("What do you want equip?\n")
        print(self.player.inventory_info())
        self.equipped_item = input("\n>").lower()
        if self.equipped_item in self.player.inventory:
            print()

# Calls the start function from the menu module.
menu.start()
init()
game = Game()
# Runs the game in a loop.
while True:
    game.mainmenu()