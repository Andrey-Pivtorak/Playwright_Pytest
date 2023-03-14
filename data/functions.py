import random
import string


def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    # Combine the character sets
    all_characters = letters + digits + symbols
    # Generate the password
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password


def generate_random_email():
    # Generate a random username
    username = ''.join(random.choices(
        string.ascii_letters + string.digits, k=10))

    # Generate a random domain name
    domain_name = ''.join(random.choices(string.ascii_lowercase, k=7))

    # Generate a random top-level domain (TLD)
    tlds = ['com', 'net', 'org', 'ua']
    tld = random.choice(tlds)

    # Combine the username, domain name, and TLD to form the email address
    email = f"{username}@{domain_name}.{tld}"

    return email
