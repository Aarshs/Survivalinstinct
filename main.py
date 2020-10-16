# Course: CS 30
# Period: 1
# Date created: 2020-10-08
# Date last modified: 2020-10-16
# Name: Aarsh Shah
# Description: Imports modules/ classes and creates a map with different game
# tiles with user inputted movement.

from colorama import init
from tabulate import tabulate
from copy import deepcopy
from map import Maps
from os import system
from player import Player
import items
import menu


class Game:
    """A class that allows the game to be ran taking user inputs to move your
    character"""
    def __init__(self):
        """Sets variables for the starting map and starting position"""
        self.map = Maps()
        self.currentmap = self.map.large
        self.pos = [5, 2]

    def mainmenu(self):
        """Allows for user inputs as the map is printed and reacts according to
        the users inputs"""
        map_copy = deepcopy(self.currentmap)

        map_copy[self.pos[0]][self.pos[1]] = "You"

        system('cls')
        # Prints the map array in a fancy format using the tabulate library.
        print(tabulate(map_copy, tablefmt="fancy_grid"))
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
        if (self.pos[0] < 0 or self.pos[0] >= len(self.currentmap)
                or self.pos[1] < 0
                or self.pos[1] >= len(self.currentmap[self.pos[0]])):
            self.pos = old_pos

        # Checks if the postion of the player is where the cave is, if it
        # is then it will change the current map to the cave map.
        if self.currentmap == self.map.large and self.pos[0] == 1 and self.pos[
                1] == 3:
            self.currentmap = self.map.cave
            self.pos = [0, 1]

        # Allows the player to go back into large map if they are in the cave.
        if self.currentmap == self.map.cave and self.pos[0] == 0 and self.pos[
                1] == 0:
            self.currentmap = self.map.large
            self.pos = [2, 3]

        # Checks if the postion of the player is where the plane is, if it
        # is then it will change the current map to the plane map.
        if self.currentmap == self.map.large and self.pos[0] == 6 and self.pos[
                1] == 2:
            self.currentmap = self.map.plane
            self.pos = [3, 0]

        # Allows the player to go back into large map if they are in the plane.
        if self.currentmap == self.map.plane and self.pos[0] == 5 and self.pos[
                1] == 1:
            self.currentmap = self.map.large
            self.pos = [5, 2]

        # Adds items to character if they come accross it in the map.
        if self.currentmap == self.map.large and self.pos[0] == 2 and self.pos[
                1] == 2:
            # medkit = items.medkit
            # player.inventoryad.append(medkit)
            # player.print_inventory()

# print(player.inventoryad)
menu.start()
init()
game = Game()
while True:
    game.mainmenu()
