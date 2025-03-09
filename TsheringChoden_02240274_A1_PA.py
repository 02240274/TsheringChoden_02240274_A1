def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_number_sum(start, end):
    """Calculate the sum of prime numbers within a given range."""
    return sum(num for num in range(start, end + 1) if is_prime(num))

def length_unit_converter(value, direction):
    """Convert between meters and feet."""
    if direction.upper() == 'M':
        return round(value * 3.28084, 2)  # Meters to feet
    elif direction.upper() == 'F':
        return round(value / 3.28084, 2)  # Feet to meters
    else:
        raise ValueError("Invalid direction. Use 'M' for meters to feet or 'F' for feet to meters.")

def consonant_counter(text):
    """Count the number of consonants in a string."""
    return sum(1 for char in text if char.isalpha() and char.lower() not in 'aeiou')

def min_max_finder(numbers):
    """Find the smallest and largest numbers in a list."""
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest

def palindrome_checker(text):
    """Check if a string is a palindrome, ignoring spaces and case."""
    cleaned_text = ''.join(text.split()).lower()
    return cleaned_text == cleaned_text[::-1]

def main():
    while True:
        print("\nSelect a function (1-5):")
        print("1. Calculate the sum of prime numbers")
        print("2. Convert length units")
        print("3. Count consonants in string")
        print("4. Find min and max numbers")
        print("5. Check for palindrome")
        print("0. Exit program")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            start = int(input("Enter the starting range: "))
            end = int(input("Enter the ending range: "))
            print("Sum of prime numbers:", prime_number_sum(start, end))
        
        elif choice == '2':
            value = float(input("Enter the numeric value: "))
            direction = input("Enter the direction (M for meters to feet, F for feet to meters): ")
            try:
                print("Converted length:", length_unit_converter(value, direction))
            except ValueError as e:
                print(e)

        elif choice == '3':
            text = input("Enter a string: ")
            print("Number of consonants:", consonant_counter(text))

        elif choice == '4':
            num_count = int(input("How many numbers do you want to enter? "))
            numbers = []
            for i in range(num_count):
                numbers.append(float(input(f"Enter number {i+1}: ")))
            smallest, largest = min_max_finder(numbers)
            print(f"Smallest: {smallest}, Largest: {largest}")

        elif choice == '5':
            text = input("Enter a string: ")
            print("Is palindrome:", palindrome_checker(text))

        elif choice == '0':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select between 0 and 5.")

        cont = input("Would you like to try another function? (y/n): ")
        if cont.lower() != 'y':
            break

if __name__ == "__main__":
    main()