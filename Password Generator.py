import random
import string

def generate_password(length, min_uppercase, min_lowercase, min_digits, min_special_chars):
    # Define characters to use for generating the password
    uppercase_letters = ''.join(random.choices(string.ascii_uppercase, k=min_uppercase))
    lowercase_letters = ''.join(random.choices(string.ascii_lowercase, k=min_lowercase))
    digits = ''.join(random.choices(string.digits, k=min_digits))
    special_chars = ''.join(random.choices(string.punctuation, k=min_special_chars))

    remaining_length = length - (min_uppercase + min_lowercase + min_digits + min_special_chars)
    characters = string.ascii_letters + string.digits + string.punctuation

    if remaining_length > 0:
        remaining_chars = ''.join(random.choices(characters, k=remaining_length))
    else:
        remaining_chars = ''

    password = uppercase_letters + lowercase_letters + digits + special_chars + remaining_chars
    password = ''.join(random.sample(password, len(password)))  # Shuffle the password characters
    return password

# Main program loop
while True:
    try:
        length = int(input("Enter the desired length of the password: "))
        min_uppercase = int(input("Enter the minimum number of uppercase letters: "))
        min_lowercase = int(input("Enter the minimum number of lowercase letters: "))
        min_digits = int(input("Enter the minimum number of digits: "))
        min_special_chars = int(input("Enter the minimum number of special characters: "))

        if length < (min_uppercase + min_lowercase + min_digits + min_special_chars):
            print("Error: Total minimum characters exceeds the specified length.")
            continue

        while True:
            password = generate_password(length, min_uppercase, min_lowercase, min_digits, min_special_chars)
            print("Generated Password:", password)

            print("\n1. Generate another random password with the same combination")
            print("2. Try another combination")
            print("3. Exit")
            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                continue
            elif choice == '2':
                break
            elif choice == '3':
                print("Thank you for using the password generator. Goodbye!")
                exit()
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        
        if choice == '2':
            continue
        elif choice == '3':
            break
    except ValueError:
        print("Invalid input. Please enter valid integers.")