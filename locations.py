# Course: CS 30
# Period: 1
# Date created: 2020-10-15
# Date last modified: 2020-10-19
# Name: Aarsh Shah
# Description: Creates a parent class and sub class for the creation of
# the different locations.

from colorama import Fore, Style


class Locations():
    """Parent class for different locations"""
    def __init__(self, place, place_description):
        self.place = place
        self.place_description = place_description

    def location_info(self):
        """Creates a print statement which tell info about a location"""
        print(f"The {self.place} is the {self.place_description}")


class Plane(Locations):
    """Stores information about the Plane location"""
    def __init__(self):
        self.plane = "Crashed Commerical Plane"
        self.place_description = "Starting area of the game"


class Cave(Locations):
    """Stores information about the Cave location"""
    def __init__(self):
        self.plane = "The Cave"
        self.place_description = "Home of Immortal Man"


class Jungle(Locations):
    """Stores information about the Jungle location"""
    def __init__(self):
        self.plane = "The Jungle"
        self.place_description = "General area to explore to find items"


# Creates variables for all of the various locations
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
