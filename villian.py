# Course: CS 30
# Period: 1
# Date created: 2020-10-15
# Date last modified: 2020-10-15
# Name: Aarsh Shah
# Description: Creates a parent class and sub class for the creation of
# the villian.

import random


class Villian():
    """A parent-class for the characteristics of the ennemies"""
    def __init__(self, name, description, health, amount):
        self.name = name
        self.name = description
        self.health = health
        self.amount = amount

    def __str__(self):
        return self.name

    def alive(self):
        """The enemies will stay alive as
        long as they have more than 0 health"""
        return self.health > 0


class Immortalman(Villian):
    """A class for the main enemie of the game"""
    def __init__(self):
        self.name = "Immortal Man"
        self.description = "Horrifying beast who resides in the cave"
        self.health = 500
        self.amount = [10, 15, 25]

    def damage(self):
        """Randomly chooses the amount of damage that Immortal Man
        will deal from a list"""
        return random.choice(self.amount)
