# Course: CS 30
# Period: 1
# Date created: 2020-10-15
# Date last modified: 2020-10-19
# Name: Aarsh Shah
# Description: Creates a parent class and sub class for the creation of
# the villian.

import random


class Villian():
    """A parent-class for the characteristics of the enemies including their 
    name, description, health and the amount of damage they can deal"""
    def __init__(self, name, description, health, amount):
        self.name = name
        self.name = description
        self.health = health
        self.amount = amount

    def __str__(self):
        """Returns the name of the villian."""
        return self.name

    def alive(self):
        """The enemies will stay alive as
        long as they have more than 0 health"""
        return self.health > 0


class Immortalman(Villian):
    """A class for the main enemy of the game"""
    def __init__(self):
        self.name = "Immortal Man"
        self.description = "Horrifying beast who resides in the cave"
        self.health = 500
        self.amount = [10, 35, 50]

    def damage(self):
        """Randomly chooses the amount of damage that Immortal Man
        will deal from a list"""
        return random.choice(self.amount)


class Knight(Villian):
    """A class for the enemies of the game"""
    def __init__(self):
        self.name = "Knight"
        self.description = "Men on horses who deal damage"
        self.health = 100
        self.amount = [10, 15, 25]

    def damage(self):
        """Randomly chooses the amount of damage that the enemy
        will deal from a list"""
        return random.choice(self.amount)