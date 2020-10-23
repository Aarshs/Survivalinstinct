# Course: CS 30
# Period: 1
# Date created: 2020-09-30
# Date last modified: 2020-10-19
# Name: Aarsh Shah
# Description: Creates the starting menu that is used to start the game.

def quit():
    """A function used within menu's so that the user can end the game
    """
    print("\nEnd Game")
    exit()


def start():
        """Creates a starting menu to get info from the player.
        """
        print("""\
Welcome to Survival Instinct. You play as a character to who was going on a
trip to Brazil. Unfortunately your planes engine fails and you crash into the
amazon rain forest. You are the sole survivor. You must survive the dangers of
this jungle and escape by finding the radio so that you can alert
people for help.\
""")
        print("\nAt anytime input 'quit' to end the game")
        while True:
            # Asks the user if they would like to start & responds accordingly.
            start1 = input("Would you like to Start, Yes or No??\n>").lower()
            if start1 == "yes":
                # Creates variables and takes user inputs for their name.
                name = input("What is your full name?\n>")
                if name != "quit":
                    print(f"Hi, {name} \nWelcome to SURVIVAL INSTINCT!\n")
                else:
                    quit()
                # Stores input to see if the user would like to start.
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
