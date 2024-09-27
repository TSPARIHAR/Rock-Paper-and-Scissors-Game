import random

def get_computer_choice():
    choices = ["R", "P", "S"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "R" and computer_choice == "S") or \
         (user_choice == "P" and computer_choice == "R") or \
         (user_choice == "S" and computer_choice == "P"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    while True:
        user_choice = input("Enter your choice Rock(R), Paper(P), or Scissors(S): ").upper()
        if user_choice not in ["R", "P", "S"]:
            print("Invalid choice. Please enter R, P, or S.")
            continue

        computer_choice = get_computer_choice()
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)
        result = determine_winner(user_choice, computer_choice)
        print(result)

        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again not in ["yes","no"]:
                print("Invalid Choice. Please enter yes or no.")
            else:
                break
        
        if play_again != "yes":
            break

play_game()
