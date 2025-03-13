import random #Importing the random module for generating random choices

# Function to check if a number is prime
def is_prime(n):
    # """Returns True if the number is prime, otherwise False."""
    if n < 2:  # A prime number must be greater than or equal to 2
        return False
    for i in range(2, int(n**0.5) + 1):  # Check divisibility up to the square root of the number
        if n % i == 0: # If n is divisible by any number in this range, it's not prime
            return False
    return True  # If no divisors are found, it's a prime number

# Function to calculate the sum of prime numbers within a given range
def prime_number_sum(start, end):
    # """Calculates the sum of all prime numbers in a given range (start to end, inclusive)."""
    return sum(num for num in range(start, end + 1) if is_prime(num))

# Function to convert between meters and feet
def length_unit_converter(value, direction):  
    #  """
    # Converts a given length between meters and feet.
    # direction = 'M' converts meters to feet
    # direction = 'F' converts feet to meters
    # """
    if direction.upper() == 'M':  # Convert meters to feet
        return round(value * 3.28084, 2)
    elif direction.upper() == 'F':  # Convert feet to meters
        return round(value / 3.28084, 2)
    else:
        raise ValueError("Invalid direction. Use 'M' for meters to feet or 'F' for feet to meters.")

# Function to count consonants in a string
def consonant_counter(text):
    # """Counts the number of consonants in a given text."""
    return sum(1 for char in text if char.isalpha() and char.lower() not in 'aeiou')

# Function to find the smallest and largest numbers in a list
def min_max_finder(numbers):
    #  """Finds and returns the smallest and largest numbers in a given list."""
    smallest = min(numbers)  # Find the smallest number
    largest = max(numbers) # Find the largest number
    return smallest, largest

# Function to check if a string is a palindrome
def palindrome_checker(text):
    # """Checks if a given string is a palindrome (reads the same forwards and backwards)."""
    cleaned_text = ''.join(text.split()).lower()  # Remove spaces and convert to lowercase
    return cleaned_text == cleaned_text[::-1]  # Compare original with reversed string

# Function to count occurrences of specific words in a text file
def word_counter(file_path, words_to_count):
    # Reads a file and counts how many times certain words appear in it.
    # words_to_count should be a list of words. 
    word_count = {word: 0 for word in words_to_count} # Initialize count dictionary
    try:
        with open(file_path, 'r', encoding='utf-8') as file: # Open file safely
            for line in file:
                words = line.lower().split() # Convert line to lowercase and split into words
                for word in words_to_count:
                    word_count[word] += words.count(word)  # Count occurrences of each word
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    return word_count  # Return the dictionary with word counts

# Main function with menu
def main():  #Displays a menu allowing users to choose from various utility functions.
    while True:
        print("\nSelect a function (1-6):")
        print("1. Calculate the sum of prime numbers")
        print("2. Convert length units")
        print("3. Count consonants in string")
        print("4. Find min and max numbers")
        print("5. Check for palindrome")
        print("6. Word Counter")
        print("0. Exit program")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':  # Prime number sum
            start = int(input("Enter the starting range: "))
            end = int(input("Enter the ending range: "))
            print("Sum of prime numbers:", prime_number_sum(start, end))
        
        elif choice == '2':  # Length unit conversion
            value = float(input("Enter the numeric value: "))
            direction = input("Enter the direction (M for meters to feet, F for feet to meters): ")
            try:
                print("Converted length:", length_unit_converter(value, direction))
            except ValueError as e:
                print(e)

        elif choice == '3':  # Count consonants in string
            text = input("Enter a string: ")
            print("Number of consonants:", consonant_counter(text))

        elif choice == '4':  # Find min and max numbers
            num_count = int(input("How many numbers do you want to enter? "))
            numbers = []
            for i in range(num_count):
                numbers.append(float(input(f"Enter number {i+1}: ")))  # Collect numbers from the user
            smallest, largest = min_max_finder(numbers)
            print(f"Smallest: {smallest}, Largest: {largest}")

        elif choice == '5':  # Check for palindrome
            text = input("Enter a string: ")
            print("Is palindrome:", palindrome_checker(text))
        
        elif choice == '6':  # Word counter
            file_path = input("Enter the text file path: ")
            words_to_count = ["the", "was", "and"]
            counts = word_counter(file_path, words_to_count)
            print("Word count:", counts)
        
        elif choice == '0':  # Exit program
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select between 0 and 6.")

        cont = input("Would you like to try another function? (y/n): ")
        if cont.lower() != 'y':  # If the user does not want to continue, break the loop
            break

# Run the main menu if the script is executed directly
if __name__ == "__main__":
    main()
