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
import villian


class Game:
    """A class that allows the game to be ran taking user inputs to move your
    character"""
    def __init__(self):
        """Sets variables for the starting map and starting position"""
        self.map = Maps()
        self.change_map(self.map.large)
        self.player = Player.default()
        self.pending_message = ""

    def change_map(self, new_map):
        "Sets what the current map and position is"
        self.current_map = new_map["locations"]
        self.item_map = new_map["items"]
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

        # Prevents user from going out of the map.
        if (self.pos[0] < 0 or self.pos[0] >= len(self.current_map)
                or self.pos[1] < 0
                or self.pos[1] >= len(self.current_map[self.pos[0]])):
            self.pos = old_pos

        # Checks if the postion of the player is where the cave is, if it
        # is then it will change the current map to the cave map.
        if self.current_map == self.map.large["locations"] and self.pos[
                0] == 1 and self.pos[1] == 3:
            self.change_map(self.map.cave)

        # Allows the player to go back into large map if they are in the cave.
        if self.current_map == self.map.cave["locations"] and self.pos[
                0] == 0 and self.pos[1] == 0:
            self.change_map(self.map.large)

        # Checks if the postion of the player is where the plane is, if it
        # is then it will change the current map to the plane map.
        if self.current_map == self.map.large["locations"] and self.pos[
                0] == 6 and self.pos[1] == 2:
            self.change_map(self.map.plane)

        # Allows the player to go back into large map if they are in the plane.
        if self.current_map == self.map.plane["locations"] and self.pos[
                0] == 5 and self.pos[1] == 1:
            self.change_map(self.map.large)

        # Allows the user to quit the game if the go to the end.
        if self.current_map == self.map.large["locations"] and self.pos[
                0] == 0 and self.pos[1] == 0:
                quit()

        # Adds items to character if they come accross it in the map.
        y, x = self.pos
        item = self.item_map[y][x]
        if item != None:
            if isinstance(item, Item):
                self.item_map[y][x] = None
                self.player.inventory.append(item)
                self.pending_message = self.player.print_inventory()


# Calls the start function from the menu module.
menu.start()
init()
game = Game()
# Runs the game in a loop.
while True:
    game.mainmenu()