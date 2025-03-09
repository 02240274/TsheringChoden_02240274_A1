import random

# Function to play the number guessing game
def guess_number_game():
    """A simple number guessing game where the user can set the number."""
    number_to_guess = 8  # Preset number to guess
    
    print("Number has been set. Now it's time for the guessing!")
    
    while True:
        user_guess = input("Guess the number (or type 'exit' to quit): ")
        
        if user_guess.lower() == "exit":
            print("Game exited. Goodbye!")
            return
        
        try:
            guess = int(user_guess)
            if guess < number_to_guess:
                print("Higher! Try again.")
            elif guess > number_to_guess:
                print("Lower! Try again.")
            else:
                print("Congratulations! You've guessed the number.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Function to play Rock-Paper-Scissors
def rock_paper_scissors():
    """A simple Rock-Paper-Scissors game against the computer."""
    choices = ["rock", "paper", "scissors"]
    
    while True:
        user_choice = input("Enter rock, paper, or scissors (or type 'exit' to quit): ").lower()
        
        if user_choice == "exit":
            print("Game exited. Goodbye!")
            return
        
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

# Main menu
def main():
    while True:
        print("\nSelect a function (1-3):")
        print("1. Guess Number Game")
        print("2. Rock Paper Scissors Game")
        print("3. Exit Program")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            guess_number_game()
        elif choice == "2":
            rock_paper_scissors()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the main menu if the script is executed directly
if __name__ == "__main__":
    main()
