import random
import string

def improved_generator(first_name: str, last_name: str, length: int):
    # Use string constants for symbols and digits
    symbol_chars = "!@#$%^&*()"
    digit_chars = "1234567890"

    # Include uppercase and lowercase letters in the password base
    password_base = list(first_name.lower() + last_name.lower() + symbol_chars + digit_chars +
                         string.ascii_letters)

    # Shuffle the password base once instead of twice
    random.shuffle(password_base)

    # Use random.choices for more concise code
    password = random.choices(password_base, k=length)

    return f"Password: {''.join(password)}"

# Example usage
print(improved_generator(first_name=input("Enter Your FirstName: ", last_name="Enter Your LastName: ", length=20))
