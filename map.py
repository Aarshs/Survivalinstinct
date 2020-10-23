# Course: CS 30
# Period: 1
# Date created: 2020-10-07
# Date last modified: 2020-10-19
# Name: Aarsh Shah
# Description: Uses tabulate and colorama libraries to create
# different maps for the different locations of the game.

from items import *
from locations import *
from villian import Immortalman, Knight


class Maps:
    """Creates a class that creates dictionaries and nested lists for the maps
    of the game, as well as setting the starting postion if the player moves
    to a new location"""
    def __init__(self):
        # Stores the large map where the player starts.
        self.large = {
            # The visual map that the user can see.
            "locations": [
                [beach, jungles, jungles, jungles, jungles],
                [beach, jungles, jungles, cave, jungles],
                [beach, jungles, jungles, jungles, jungles],
                [beach, jungles, jungles, jungles, jungles],
                [beach, jungles, jungles, jungles, jungles],
                [beach, jungles, "Start", jungles, jungles],
                [beach, jungles, "Plane", jungles, jungles],
                [beach, jungles, jungles, jungles, jungles],
                [beach, jungles, jungles, jungles, jungles],
            ],
            # Item map for the postion of where the items can be found.
            "items": [
                [None, None, None, None, None],
                [None, None, Heal.Medkit(), None, None],
                [Weapon.Sword(), None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
            ],
            # Enemy map for the postion of where the enemies can be found.
            "enemies": [
                [None, None, None, None, Knight()],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, Knight(), None, None, None],
                [None, None, None, Knight(), None],
                [None, None, None, None, None],
                [None, None, None, None, None],
            ],
            # Sets the default postion of the map.
            "default_pos": [5, 2]
        }
        # Stores the cave map where the immortal mans can be found.
        self.cave = {
            # The visual map that the user can see.
            "locations": [
                [exit, boulder, boulder, structure, boulder],
                [boulder, boulder, boulder, boulder, "Massive wall"],
                [boulder, boulder, boulder, boulder, "Massive wall"],
                [boulder, boulder, boulder, boulder, "Massive wall"],
            ],
            # Item map for the postion of where the items can be found.
            "items": [
                [None, None, None, None, Item.Radio()],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, Weapon.Chainsaw(), None],
            ],
            # Enemy map for the postion of where the enemies can be found.
            "enemies": [
                [None, None, None, Immortalman(), None],
                [None, Knight(), None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
            ],
            # Sets the default postion of the map.
            "default_pos": [0, 1]
        }
        # Stores the plane map where supplies can be found.
        self.plane = {
            # The visual map that the user can see.
            "locations": [
                [cockpit, cockpit, cockpit],
                [seats, seats, seats],
                [seats, seats, seats],
                [door, seats, seats],
                [storage, storage, storage],
                [storage, exit, storage],
            ],
            # Item map for the postion of where the items can be found.
            "items": [
                [None, None, None],
                [None, None, None],
                [None, None, None],
                [None, None, None],
                [None, None, None],
                [None, None, Weapon.Axe()],
            ],
            # Enemy map for the postion of where the enemies can be found.
            "enemies": [
                [None, Knight(), None],
                [None, None, None],
                [None, None, None],
                [None, None, Knight()],
                [None, None, None],
                [None, None, None],
            ],
            # Sets the default postion of the map.
            "default_pos": [3, 0],
        }
