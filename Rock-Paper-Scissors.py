import random

user, computer = 0, 0

while True:
    print("\n1 - Rock\n2 - Paper\n3 - Scissors")
    user_choice =("Your choice: ")
    computer_choice = random.choice(["1", "2", "3"])

    if user_choice == "1":
        if computer_choice == "1":
            print("Computer's choice: Rock\nRock equal to rock. Scoreless!")

        elif computer_choice == "2":
            print("Computer's choice: Paper\nPaper wraps stone. You lose!")
            computer += 100

        elif computer_choice == "3":
            print("Computer's choice: Scissors\nRock breaks scissors. You win!")
            user += 100

    elif user_choice == "2":
        if computer_choice == "1":
            print("Computer's choice: Rock\nPaper wraps stone. You win!")
            user += 100

        elif computer_choice == "2":
            print("Computer's choice: Paper\nPaper equal to paper. Scoreless!")

        elif computer_choice == "3":
            print("Computer's choice: Scissors\nScissors cuts paper. You lose!")
            computer += 100

    elif user_choice == "3":
        if computer_choice == "1":
            print("Computer's choice: Rock\nRock breaks scissors. You lose!")
            computer += 100

        elif computer_choice == "2":
            print("Computer's choice: Paper\nScissors cuts paper. You win!")
            user += 100

        elif computer_choice == "3":
            print("Computer's choice: Scissors\nScissors equal to scissors. Scoreless!")

    else:
        break

print("\nUser's score: {}\nComputer's score: {}".format(user, computer))
