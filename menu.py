movements = ["Forward", "Backward", "Right", "Left"]

print("Which way would you like to move:")
for movement in movements:
    print(movement)

while True:
    move = input().lower()
    if move == "forward":
        print("You moved 500m forward")
    elif move == "backward":
        print("You moved 500m backward")
    elif move == "right":
        print("You moved 500m to the right")
    elif move == "left":
        print("You moved 500m to the left")
    else:
        print("You can't go that way")
    break
