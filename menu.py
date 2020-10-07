# Course: CS 30
# Period: 1
# Date created: 2020-09-30
# Date last modified: 2020-10-07
# Name: Aarsh Shah
# Description: Creates a series of menus that are used to navigate
# the game/ different options such as movement and inventory.


def quit():
    """A function used within menu's so that the user can end the game
    """
    print("\nEnd Game")
    exit()


def start():
    """A function that creates a starting menu to get info from the player.
    """
    print("At anytime input 'quit' to end the game")
    while True:
        # Asks the user if they would like to start & responds accordingly.
        start1 = input("Would you like to Start, Yes or No??\n").lower()
        if start1 == "yes":
            # Creates variables and takes user inputs for their names.
            name = input("What is your full name?\n")
            print(f"Hi, {name}")
            username = input("What would you like your username to be?\n")
            print(f"Welcome {username} to SURVIVAL INSTINCT!\n")
            break
        elif start1 in ["no", "quit"]:
            quit()
        else:
            print("Please Try Again")
            continue


def move():
    """A function that creates a menu for the movement of the character.
    """
    # Stores the info for the menu's in these variables
    movements = ["Forward", "Backward", "Right", "Left"]
    while True:
        print("\nWhich way would you like to move:")
        for movement in movements:
            print(movement)
        # Takes the users input on where they want to move
        # and compares it, to print a statement.
        move = input().lower()
        if move == "forward":
            print("\nYou moved 500m forward")
            print("You've come across Immortal Man")
            inventory()
        elif move == "backward":
            print("\nYou moved 500m backward")
            print("You've found extra flashlight batteries")
            continue
        elif move == "right":
            print("\nYou moved 500m to the right")
            print("You've found Adrenaline Pills")
            continue
        elif move == "left":
            print("\nYou moved 500m to the left")
            print("You found nothing")
            continue
        elif move == "quit":
            quit()
        else:
            print("\nYou can't go that way")
            continue


def inventory():
    """Creates a function for the inventory of the character.
    """
    # Creates a dictionary storing both tool and heal items.
    invent = {
        "Tools": ["Knife", "Flashlight", "Flaregun", "Metal Shard"],
        "Heals": ["Medkit", "Bandages", "Painkiler"],
    }
    # A loop that allows the user to input what item they want use
    # And prints what the item does.
    while True:
        print("\nWhat would you like to use?")
        # Gets user input on what type of item they want to use.
        type1 = input("Tools or Heals?\n").lower()
        if type1 == "tools":
            # Gets input on what tool and prints a statement.
            print("\nWhat tool would you like to use")
            for tool in invent["Tools"]:
                print(tool)
            tool = input().lower()
            if tool == "knife":
                print("\nKnife does 25 damage")
                move()
            elif tool == "flashlight":
                print("\nFlashlight allows you to see around you")
                move()
            elif tool == "flaregun":
                print("\nThis allows you to signal for help")
                move()
            elif tool == "metal shard":
                print("\nThis allows you to delfect damage")
                move()
            elif tool == "quit":
                quit()
            else:
                print("\nInvalid type")
                continue
        elif type1 == "heals":
            # Gets input on what healable and prints a statement.
            print("\nWhat healable would you like to use")
            for tool in invent["Heals"]:
                print(tool)
            heal = input().lower()
            if heal == "medkit":
                print("\nRestores 50 Health")
                move()
            elif heal == "Bandages":
                print("\nRestores 25 Health")
                move()
            elif heal == "painkiler":
                print("\nAllows you do more damage")
                move()
            elif heal == "quit":
                quit()
            else:
                print("\nInvalid type")
                continue
        elif type1 == "quit":
                quit()
        else:
            print("Invalid type")


start()
move()
inventory()
