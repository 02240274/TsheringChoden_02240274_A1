import random

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to calculate the sum of prime numbers within a given range
def prime_number_sum(start, end):
    return sum(num for num in range(start, end + 1) if is_prime(num))

# Function to convert between meters and feet
def length_unit_converter(value, direction):
    if direction.upper() == 'M':  # Convert meters to feet
        return round(value * 3.28084, 2)
    elif direction.upper() == 'F':  # Convert feet to meters
        return round(value / 3.28084, 2)
    else:
        raise ValueError("Invalid direction. Use 'M' for meters to feet or 'F' for feet to meters.")

# Function to count consonants in a string
def consonant_counter(text):
    return sum(1 for char in text if char.isalpha() and char.lower() not in 'aeiou')

# Function to find the smallest and largest numbers in a list
def min_max_finder(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest

# Function to check if a string is a palindrome
def palindrome_checker(text):
    cleaned_text = ''.join(text.split()).lower()
    return cleaned_text == cleaned_text[::-1]

# Function to count occurrences of specific words in a text file
def word_counter(file_path, words_to_count):
    word_count = {word: 0 for word in words_to_count}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.lower().split()
                for word in words_to_count:
                    word_count[word] += words.count(word)
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    return word_count

# Main function with menu
def main():
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
                numbers.append(float(input(f"Enter number {i+1}: ")))
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
        if cont.lower() != 'y':
            break

if __name__ == "__main__":
    main()
