import random

def guess_number_game():
    """A simple number guessing game where the user can set the number."""
    # Allow the user to set the number to guess
    number_to_guess = 8
    while number_to_guess is None:
        user_input = input("Set a number between 1 and 100 for others to guess (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Game exited. Goodbye!")
            return
        try:
            user_set_number = int(user_input)
            if 1 <= user_set_number <= 100:
                number_to_guess = user_set_number
            else:
                print("Please enter a number within the range of 1 to 100.")
        except ValueError:
            print("Please enter a valid number.")

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

if __name__ == "__main__":
    guess_number_game()
