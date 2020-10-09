# Course: CS 30
# Period: 1
# Date created: 2020-10-08
# Date last modified: 2020-10-08
# Name: Aarsh Shah
# Description: Imports modules/ functions from different game files 
# and prints them out.


from main import large_map, cave_map
from info import character1, inventory1, location1
from menu import inventory2, move, start, quit


def print_all():
    print(large_map, cave_map)
    print(character1, inventory1, location1)
    print(inventory2, move, start, quit)


print_all()
