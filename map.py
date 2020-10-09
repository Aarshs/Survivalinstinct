# Course: CS 30
# Period: 1
# Date created: 2020-10-07
# Date last modified: 2020-10-08
# Name: Aarsh Shah
# Description: Uses tabulate and colorama libraries to create
# different maps for the different locations of the game.

from tabulate import tabulate
from colorama import Fore, Back, Style, init

init()


def large_map():
    """Creates a function that creates a nested array and uses tabulate to
    make a organize table to repersent the main large map for the game.
    """
    # Creates jungle and cave variables with colour formatting.
    jungles = (Fore.GREEN + "Jungle" + Style.RESET_ALL)
    cave = (Fore.BLUE + "Cave" + Style.RESET_ALL)
    # Prints the name of the map above the table.
    print(" " * 15 + "Wilderness Map")
    # Creates a nested list with the different areas as elements in the array.
    large = [[jungles, jungles, jungles, jungles, jungles],
             [jungles, jungles, jungles, cave, jungles],
             [jungles, jungles, jungles, jungles, jungles],
             [jungles, jungles, jungles, jungles, jungles],
             [jungles, jungles, jungles, jungles, jungles],
             [jungles, jungles, "Start", jungles, jungles],
             [jungles, jungles, "Plane", jungles, jungles],
             [jungles, jungles, jungles, jungles, jungles],
             [jungles, jungles, jungles, jungles, jungles]]
    # Prints the nested list in a fancy format using the tabulate library.
    print(tabulate(large, tablefmt="fancy_grid"))


def cave_map():
    """Creates a function that creates a nested array and uses tabulate to
    make a organize table to repersent the cave map where the house
    of the villian is for the game.
    """
    # Creates boulder and structure variables with colour formatting.
    boulder = (Fore.GREEN + "Boulder" + Style.RESET_ALL)
    structure = (Fore.BLUE + "Structure" + Style.RESET_ALL)
    # Prints the name of the map above the table.
    print(" " * 15 + "Cave Map")
    # Creates a nested list with the different areas as elements in the array.
    cave = [[boulder, boulder, boulder, structure],
            [boulder, "You", boulder, boulder],
            [boulder, boulder, boulder, boulder],
            [boulder, boulder, boulder, boulder]]
    # Prints the nested list in a fancy format using the tabulate library.
    print(tabulate(cave, tablefmt="fancy_grid"))


def plane_map():
    """Creates a function that creates a nested array and uses tabulate to
    make a organize table to repersent the plane map for the game.
    """
    # Creates variables for all the different aspects of the plane map
    # with colour formatting.
    seats = (Fore.GREEN + "Seats" + Style.RESET_ALL)
    cockpit = (Fore.BLUE + "Cockpit" + Style.RESET_ALL)
    storage = (Fore.RED + "Storage" + Style.RESET_ALL)
    door = (Fore.BLUE + "Door" + Style.RESET_ALL)
    exit = (Fore.BLUE + "Exit" + Style.RESET_ALL)
    # Prints the name of the map above the table.
    print(" " * 12 + "Plane Map")
    # Creates a nested list with the different areas as elements in the array.
    plane = [[cockpit, cockpit, cockpit], [seats, seats, seats],
             [seats, seats, seats], [door, seats, seats],
             [storage, storage, storage], ["", exit, ""]]
    # Prints the nested list in a fancy format using the tabulate library.
    print(tabulate(plane, tablefmt="fancy_grid"))


large_map()
cave_map()
plane_map()
