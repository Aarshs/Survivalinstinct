# Course: CS 30
# Period: 1
# Date created: 2020-10-15
# Date last modified: 2020-10-15
# Name: Aarsh Shah
# Description: Creates a parent class and sub class for the creation of
# the different locations.


class Locations():
    """Parent class for different locations"""
    def __init__(self, place, place_description):
        self.place = place
        self.place_description = place_description

    def location_info(self):
        """Creates a print statement which tell info about a location"""
        print(f"The {self.place} is the {self.place_description}")


class Plane(Locations):
    """Stores information about the plane location"""
    def __init__(self):
        self.plane = "Crashed Commerical Plane"
        self.place_description = "Starting area of the game"


class Cave(Locations):
    """Stores information about the Cave location"""
    def __init__(self):
        self.plane = "The Cave"
        self.place_description = "Home of Immortal Man"


class Jungle(Locations):
    """Stores information about the jungle location"""
    def __init__(self):
        self.plane = "The Jungle"
        self.place_description = "General area to explore to find items"
