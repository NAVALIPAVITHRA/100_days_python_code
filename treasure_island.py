print("___________________________________________welcome to treasure island_________________________________________________________________________________________________")
direction = input("you're at a crossroad. Where do you want to go? Type 'left' or 'right': ")

if direction == "left":
    print("You came to a lake. There is an island in the middle.")
    option = input("Type 'wait' to wait for the boat or 'swim' to cross by swimming: ")

    if option == "wait":
        print("The boat is here, and you arrived at the island unharmed.")

        color = input("There are 3 doors: red, yellow, and blue. Which one do you choose? ")
        if color == "red":
            print("Hey! It's fire. Game over!")
        elif color == "yellow":
            print("Congratulations! You found the golden treasure!")
        else:
            print("Oops! You lost the treasure. Game over!")

    else:
        print("Game over! You chose to swim.")

else:
    print("Game over! You didn't choose the left path.")

