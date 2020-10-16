# Course: CS 30
# Period: 1
# Date created: 2020-10-07
# Date last modified: 2020-10-08
# Name: Aarsh Shah
# Description: Uses tabulate and colorama libraries to create
# different maps for the different locations of the game.

from colorama import Fore, Style

# Creates Creates variables for all of the various locations
# with colour formatting.
jungles = (Fore.GREEN + "Jungle" + Style.RESET_ALL)
cave = (Fore.BLUE + "Cave" + Style.RESET_ALL)
boulder = (Fore.RED + "Boulder" + Style.RESET_ALL)
structure = (Fore.BLUE + "Structure" + Style.RESET_ALL)
seats = (Fore.GREEN + "Seats" + Style.RESET_ALL)
cockpit = (Fore.BLUE + "Cockpit" + Style.RESET_ALL)
storage = (Fore.BLUE + "Storage" + Style.RESET_ALL)
door = (Fore.WHITE + "Door" + Style.RESET_ALL)
exit = (Fore.RED + "Exit" + Style.RESET_ALL)
beach = (Fore.YELLOW + "Beach" + Style.RESET_ALL)

class Maps:
    """
    Creates a class that creates mulptiple arrays for the maps of the game"""
    def __init__(self):
        # The large map where the player starts
        self.large = [["End", jungles, jungles, jungles, jungles],
                      [beach, jungles, jungles, cave, jungles],
                      [beach, jungles, jungles, jungles, jungles],
                      [beach, jungles, jungles, jungles, jungles],
                      [beach, jungles, jungles, jungles, jungles],
                      [beach, jungles, "Start", jungles, jungles],
                      [beach, jungles, "Plane", jungles, jungles],
                      [beach, jungles, jungles, jungles, jungles],
                      [beach, jungles, jungles, jungles, jungles]]
        # The cave map where the immortal mans house is.
        self.cave = [[boulder, boulder, boulder, structure],
                     [boulder, boulder, boulder, boulder],
                     [boulder, boulder, boulder, boulder],
                     [boulder, boulder, boulder, boulder]]
        # The plane map where items can be salvaged
        self.plane = [[cockpit, cockpit, cockpit], [seats, seats, seats],
                      [seats, seats, seats], [door, seats, seats],
                      [storage, storage, storage], ["", exit, ""]]
