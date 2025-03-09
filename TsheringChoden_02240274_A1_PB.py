import random

# Function to play the number guessing game
def guess_number_game():
    """A simple number guessing game where the user can set the number."""
    
    # The number to guess (preset for now, but can be user-defined)
    number_to_guess = 8  
    
    # Loop to allow the user to set the number (currently disabled with a preset value)
    while number_to_guess is None:
        user_input = input("Set a number between 1 and 100 for others to guess (or type 'exit' to quit): ")
        
        # Allow the user to exit the game
        if user_input.lower() == "exit":
            print("Game exited. Goodbye!")
            return
        
        try:
            user_set_number = int(user_input)  # Convert input to integer
            if 1 <= user_set_number <= 100:  # Ensure number is within valid range
                number_to_guess = user_set_number
            else:
                print("Please enter a number within the range of 1 to 100.")
        except ValueError:
            print("Please enter a valid number.")
    
    print("Number has been set. Now it's time for the guessing!")
    
    # Loop for the guessing process
    while True:
        user_guess = input("Guess the number (or type 'exit' to quit): ")
        
        # Allow the user to exit the game at any time
        if user_guess.lower() == "exit":
            print("Game exited. Goodbye!")
            return
        
        try:
            guess = int(user_guess)  # Convert guess to integer
            
            if guess < number_to_guess:
                print("Higher! Try again.")
            elif guess > number_to_guess:
                print("Lower! Try again.")
            else:
                print("Congratulations! You've guessed the number.")
                break  # Exit loop when the correct number is guessed
        except ValueError:
            print("Please enter a valid number.")

# Run the game if the script is executed directly
if __name__ == "__main__":
    guess_number_game()
