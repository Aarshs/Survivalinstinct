# Course: CS 30
# Period: 1
# Date created: 2020-09-30
# Date last modified: 2020-10-19
# Name: Aarsh Shah
# Description: Creates the starting menu that is used to start the game.

from player import *

def quit():
    """A function used within menu's so that the user can end the game
    """
    print("\nEnd Game")
    exit()


def start():
        """Creates a starting menu to get info from the player.
        """
        print("\nAt anytime input 'quit' to end the game")
        while True:
            # Asks the user if they would like to start & responds accordingly.
            start1 = input("Would you like to Start, Yes or No??\n>").lower()
            if start1 == "yes":
                # Creates variables and takes user inputs for their names.
                name = input("What is your full name?\n>")
                if name != "quit":
                    print(f"Hi, {name}")
                else:
                    quit()
                username = input("What would you like your username to be?\n")
                if username != "quit":
                    print(f"Welcome {username} to SURVIVAL INSTINCT!\n")
                else:
                    quit()
                begin = input("Press 'w' to begin\n>").lower()
                if begin == "w":
                    break
                elif begin == "quit":
                    quit()
                else:
                    print("Please Try Again")
            elif start1 in ["no", "quit"]:
                quit()
            else:
                print("Please Try Again")
                continue

item = Player.default()


def run():
    print("You are running")


def equip():
    print("What do you want equip?\n")
    print(item.print_inventory())



equip()


def menu():
    option = input("""\
What do you want to do?
1. Run
2. Equip
> \
""").lower()
    if option in ("run", "1"):
            equip()
    elif option == "quit":
        quit()
    else:
        print("Please Try again")

    if option in ("equip", "2"):
        print()
    elif option == "quit":
        quit()
    else:
        print("Please Try again")
