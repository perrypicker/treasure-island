print('''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/[TomekK]
    *******************************************************************************
''')

print("Welcome to Treasure Island. Your mission is to find the treasure.\n")

right_or_left = input("Where do you want to go? Right or left? ").lower()


if right_or_left == "left" :
    river = input("You found a river. What do you want to do? Swim or wait? ").lower()
    
    if river == "wait" :
        doors = input("You are looking three doors. Red, blue and yellow. Which do you choose? ").lower()

        if doors == "red" :
            print("Burned by ffire. Game Over.")

        elif doors == "blue" :
            print("Eaten by beast. Game Over.")

        elif doors == "yellow" :
            print("You win!")

        else :
            print("You are dead because you do not know how to follow instructions. Game Over.")
    
    else :
        print("You have been attacked by a trout. Game Over.")

else :
    print("You fall into a hole. Game Over.")