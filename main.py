import art
print(art.art)

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" '
                    'to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow "
                        "and one blue. Which colour do you choose? \n").lower()
        if choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "red":
            print("Burned by fire. Game Over.")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("You made a mistake while choosing, please start again.")
    elif choice2 == "swim":
        print("Attacked by trout. Game Over.")
    else:
        print("You made a mistake while choosing, please start again.")
elif choice1 == "right":
    print("Fall into a hole. Game Over.")
else:
    print("You made a mistake while choosing, please start again.")