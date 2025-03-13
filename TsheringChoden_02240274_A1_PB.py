import random # Importing the random module for generating random choices

# Function to play the number guessing game
def guess_number_game():
    """A simple number guessing game where the user can set the number."""
    number_to_guess = random.randint(1, 50)
    attempts = 0 # The correct number that the user needs to guess

    print("Number has been set. Now it's time for the guessing!")
    
    while True:
         # Asking the user for their guess
        user_guess = input("Guess the number (or type 'exit' to quit): ")

        # Allow the user to exit the game
        if user_guess.lower() == "exit":
            print("Game exited. Goodbye!")
            return # Ends the function and exits the game
        
        try:
            guess = int(user_guess)  # Convert the user's input into an integer
            if guess < number_to_guess:
                print("Lower! Try again.") # Hint to guess a higher number
            elif guess > number_to_guess:
                print("Higher! Try again.") # Hint to guess a lower number
            else:
                print("Congratulations! You've guessed the number.") # User wins
                break # Exit the loop when the number is guessed correctly
        except ValueError:
            print("Please enter a valid number.") # Handle cases where input is not a number

# Function to play Rock-Paper-Scissors
def rock_paper_scissors():
    """A simple Rock-Paper-Scissors game against the computer.The user selects rock, paper, or scissors, and the computer makes a random choice."""
    choices = ["rock", "paper", "scissors"]  # Possible choices for the game
    
    while True:
         # Asking the user for their choice
        user_choice = input("Enter rock, paper, or scissors (or type 'exit' to quit): ").lower()

        # Allow the user to exit the game
        if user_choice == "exit":
            print("Game exited. Goodbye!")
            return  # Ends the function and exits the game
        
        # Validate user input
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue # Restart the loop if input is invalid
        
         # Computer makes a random choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")  # Both choices are the same
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")  # User wins the round
        else:
            print("You lose!") # Computer wins the round

# Main menu
def main():
      # The main menu of the program, allowing users to select different games to play.
    
    while True:
        print("\nSelect a function (1-3):")
        print("1. Guess Number Game")
        print("2. Rock Paper Scissors Game")
        print("3. Exit Program")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            guess_number_game()  # Start the number guessing game
        elif choice == "2":
            rock_paper_scissors()  # Start the Rock-Paper-Scissors game
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break # Exit the program
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")  # Handle incorrect menu choices

# Run the main menu if the script is executed directly
if __name__ == "__main__":
    main()
