# Course: CS 30
# Period: 1
# Date created: 2020-10-08
# Date last modified: 2020-10-25
# Name: Aarsh Shah
# Description: Imports modules/ classes and creates a map with different game
# tiles with user inputted movement, attacking, healing and more.

import random
from copy import deepcopy
from os import system

from colorama import init
from tabulate import tabulate

import menu
from items import *
from map import Maps
from player import Player
from villian import Villian


class Game:
    """A class that allows the game to be run taking user inputs to move your
    character, pick up items, attack enemies and run away.
    """
    def __init__(self):
        """Sets variables up for the game, including the map,
        pending messages, the default settings.
        """
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
        """Sets what the current visual, item and enemy map and position is."""
        self.current_map = new_map["locations"]
        self.item_map = new_map["items"]
        self.enemy_map = new_map["enemies"]
        self.pos = deepcopy(new_map["default_pos"])
        self.pending_message = new_map["description"]

    def mainmenu(self):
        """Allows for user inputs as the map is printed and reacts according to
        the users inputs.
        """
        map_copy = deepcopy(self.current_map)
        # Sets the marker to indicate the player as "You".
        map_copy[self.pos[0]][self.pos[1]] = "You"

        system('cls')
        # Prints the map array in a fancy format using the tabulate library.
        print(tabulate(map_copy, tablefmt="fancy_grid"))
        if self.pending_message != "":
            print(self.pending_message)
            self.pending_message = ""
        # Variable that stores the user input on where they want to move.
        selector = input("""\
Choose a direction (Use WASD):
Left, Right, Up, or Down?
> \
""").lower()
        # Checks to see where the user wants to move and reacts accordingly.
        self.old_pos = self.pos[:]
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

        # Calls game methods to allow the aspects of the game to function.
        self.move_map()
        self.boundaries()
        self.add_items()
        self.attacking()

    def boundaries(self):
        """Method to prevent the user from going outside of the map."""
        if (self.pos[0] < 0 or self.pos[0] >= len(self.current_map)
                or self.pos[1] < 0
                or self.pos[1] >= len(self.current_map[self.pos[0]])):
            # Moves the user back into the map if they go past the boundaries.
            self.pos = self.old_pos

    def move_map(self):
        """Allows the user to move between the different maps of the game."""
        for hotspot in self.map_hotspots:
            if self.current_map == hotspot["map"][
                    "locations"] and self.pos == hotspot["pos"]:
                self.change_map(hotspot["new_map"])

    def positioning(self):
        """Method to store what enemy is at your current location."""
        # Sets the positon to x and y coordinates.
        self.y, self.x = self.pos
        # Variable to store what enemy is in battle.
        self.enemy = self.enemy_map[self.y][self.x]

    def add_items(self):
        """Adds items to character if they come accross it in the map."""
        # Sets the positon to x and y coordinates.
        y, x = self.pos
        # Variable to store what item is being picked up in respect to the map.
        item = self.item_map[y][x]
        # Checks if there is an item in the position of the player.
        if item != None and isinstance(item, Item):
            self.item_map[y][x] = None
            # Adds the new item to the inventory.
            self.player.inventory.append(item)
            # Prints out the new inventory.
            self.pending_message = f"""{item} was found!\n
{self.player.inventory_info()}"""

    def attacking(self):
        """Reacts when the player encounters an enemy."""
        self.positioning()
        # Checks if there is an enemy in the position of the player.
        if self.enemy != None and isinstance(self.enemy, Villian):
            self.item_map[self.y][self.x] = None
            # Calls the menu methood which allows the user to react.
            self.pending_message = self.menu1()

    def menu1(self):
        """Creates the menu that is presented when the player encounters
        an enemy.
        """
        self.positioning()
        while 1:
            # Variable that stores the input of the players next action
            option = input(f"""\
You have encountered a {self.enemy}. He is a {self.enemy.description}.
What do you want to do?
1. Run
2. Equip
> \
""").lower()
            if option in ("run", "1"):
                print("You are attempting to run")
                # Variable then chooses a random choice from the random list.
                option = random.choice(self.player.random)
                if option == "Escaped":
                    return "You got away"
                elif option == "Failed":
                    print("You couldn't get away")
                    return self.equip()
            elif option in ("equip", "2"):
                return self.equip()
            elif option == "quit":
                quit()
            else:
                print("Please Try again")

    def equip(self):
        """Method to allow the player to equip either a healable or weapon
        item.
        """
        self.positioning()
        # A while loop that runs as long as the enemy is alive.
        while self.enemy.alive():
            # Checks to see if the items in the inventory still have uses.
            self.player.inventory = list(
                filter(item_usable, self.player.inventory))
            # Asks the user what they want to equip from their inventory.
            print("What do you want equip?\n")
            print(self.player.inventory_info())
            # Variable stores the user input for what item they want to equip.
            option = input("\n>").lower()
            if option in [item.name for item in self.player.inventory]:
                # Stores the chosen item to be equipped.
                self.equipped_item = next(item
                                          for item in self.player.inventory
                                          if item.name == option)
                print(f"You equipped {str(self.equipped_item)}")
                # Checks to see if the chosen item is a weapon.
                if isinstance(self.equipped_item, Weapon):
                    self.attack()
                # Checks to see if the chosen item is a healable.
                elif isinstance(self.equipped_item, Heal):
                    self.heal()
                # Checks to see if the player has more than 0 health.
                if not self.player.alive():
                    print("You Died!")
                    quit()
                # Removes the enemy off the map once they've been killed.
                if not self.enemy.alive():
                    self.enemy_map[self.y][self.x] = None
            elif option == "quit":
                quit()
            else:
                print("You don't have that item")
        # Prints a statment saying that you've won if you killed the main boss.
        if self.enemy.name == "Immortal Man":
            print("""\
You killed the Immortal Man!
He was stashing the radio in his house.
YOU HAVE ESCPAED, CONGRATS""")
            quit()
        # Returns a statement if you are successful in killing the enemy.
        else:
            return ("You killed the enemy!")

    def heal(self):
        """Allows the player to recover health and use a healable."""
        self.player.health += self.equipped_item.add_health
        self.equipped_item.uses -= 1
        print(f"You now have {self.player.health} health")

    def attack(self):
        """Allows the player to attack using their equipped weapon."""
        self.positioning()
        # Variable to store the amount of damage the equipped weapon deals.
        damage = self.equipped_item.damage
        # Remove a use off the weapon everytime its used.
        self.equipped_item.uses -= 1
        # Deals the damage to the enemies health.
        self.enemy.health -= damage
        # Subtracts your health from the amount of damage the enemy dealt.
        self.player.health -= self.enemy.damage()
        # Prints what weapon the player attacked with
        # and the players' and enemies current health
        print(f"""You attacked with a {self.equipped_item}
The enemy has {self.enemy.health} health
You now have {self.player.health} health\n""")


# Calls the start function from the menu module.
menu.start()
init()
game = Game()
# Runs the game in a loop.
while True:
    game.mainmenu()
