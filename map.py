# Course: CS 30
# Period: 1
# Date created: 2020-10-07
# Date last modified: 2020-10-19
# Name: Aarsh Shah
# Description: Uses tabulate and colorama libraries to create
# different maps for the different locations of the game.

from villian import Immortalman, Knight
from items import *
from locations import *




class Maps:
    """Creates a class that creates dictionaries and nested lists for the maps
    of the game, as well as setting the starting postion if the player moves
    to a new location"""
    def __init__(self):
        # self.boss = Immortalman.default()
        # self.enemy = Knight.default()
        # The large map where the player starts.
        self.large = {
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
            "default_pos": [5, 2]
        }
        # The cave map where the immortal mans house is.
        self.cave = {
            "locations": [
                [exit, boulder, boulder, structure],
                [boulder, boulder, boulder, boulder],
                [boulder, boulder, boulder, boulder],
                [boulder, boulder, boulder, boulder],
            ],
            "items": [
                [None, None, None, None],
                [None, None, None, None],
                [None, None, None, None],
                [None, None, None, Weapon.Chainsaw()],
            ],
            "enemies": [
                [None, None, None, Immortalman()],
                [None, Knight(), None, None],
                [None, None, None, None],
                [None, None, None, None],
                [None, None, None, None],
            ],
            "default_pos": [0, 1]
        }
        # The plane map where items can be found.
        self.plane = {
            "locations": [
                [cockpit, cockpit, cockpit],
                [seats, seats, seats],
                [seats, seats, seats],
                [door, seats, seats],
                [storage, storage, storage],
                [storage, exit, storage],
            ],
            "items": [
                [None, None, None],
                [None, None, None],
                [None, None, None],
                [None, None, None],
                [None, None, None],
                [None, None, Weapon.Axe()],
            ],
            "enemies": [
                [None, Knight(), None],
                [None, None, None],
                [None, None, None],
                [None, None, Knight()],
                [None, None, None],
                [None, None, None],
            ],
            "default_pos": [3, 0],
        }
