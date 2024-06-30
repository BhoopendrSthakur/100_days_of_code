import random

def get_computer_choice():
    return random.choice([1, 2, 3])

def get_user_choice():
    print("Enter your choice:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Your choice (1, 2, or 3): ")
    while choice not in ["1", "2", "3"]:
        choice = input("Invalid choice. Enter 1, 2, or 3: ")
    return int(choice)

def display_choice(choice):
    if choice == 1:
        return """
        Rock:
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """
    elif choice == 2:
        return """
        Paper:
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """
    elif choice == 3:
        return """
        Scissors:
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print("Your choice:")
    print(display_choice(user_choice))
    
    print("Computer's choice:")
    print(display_choice(computer_choice))

    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()