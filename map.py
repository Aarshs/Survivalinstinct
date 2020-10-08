# Course: CS 30
# Period: 1
# Date created: 2020-10-07
# Date last modified: 2020-10-07
# Name: Aarsh Shah
# Description: Uses tabulate and colorama libraries to create
# different maps for the different locations of the game.

from tabulate import tabulate
from colorama import Fore, Back, Style


def large_map():
    jungles = (Fore.GREEN + "Jungle" + Style.RESET_ALL)
    cave = (Fore.BLUE + "Cave" + Style.RESET_ALL)
    print(" " * 15 + "Wilderness Map")
    table1 = [[jungles, jungles, jungles, jungles, jungles],
              [jungles, jungles, jungles, cave, jungles],
              [jungles, jungles, jungles, jungles, jungles],
              [jungles, jungles, jungles, jungles, jungles],
              [jungles, jungles, jungles, jungles, jungles],
              [jungles, jungles, "Start", jungles, jungles],
              [jungles, jungles, "Plane", jungles, jungles],
              [jungles, jungles, jungles, jungles, jungles],
              [jungles, jungles, jungles, jungles, jungles]]

    print(tabulate(table1, tablefmt="fancy_grid"))


def cave_map():
    boulder = (Fore.GREEN + "Boulder" + Style.RESET_ALL)
    cave = (Fore.BLUE + "Cave" + Style.RESET_ALL)

    table2 = [[boulder, boulder, boulder], [boulder, "You", boulder],
              [boulder, boulder, boulder]]

    print(tabulate(table2, tablefmt="fancy_grid"))


def plane_map():
    print()


large_map()
cave_map()
