import random
import string
import data.functions
import data
import copy

def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine the character sets
    all_characters = letters + digits + symbols

    # Generate the password
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

# Generate a password with a length of 12 characters
# password = generate_password(12)
# print(password)


email = data.user_data.email
# mm = data.user_data.mm
print(email)
# print(mm)


