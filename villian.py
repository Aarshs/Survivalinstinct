# Course: CS 30
# Period: 1
# Date created: 2020-10-15
# Date last modified: 2020-10-15
# Name: Aarsh Shah
# Description: Creates a parent class and sub class for the creation of
# the villian.

import random


class Villian():
    def __init__(self, name, description, health, amount):
        self.name = name
        self.name = description
        self.health = health
        self.amount = amount

    def __str__(self):
        return self.name

    def alive(self):
        return self.health > 0


class Immortalman(Villian):
    def __init__(self):
        self.name = "Immortal Man"
        self.description = "Horrifying beast who resides in the cave"
        self.health = 500
        self.amount = [10, 15, 25]

    def damage(self):
        return random.choice(self.amount)
