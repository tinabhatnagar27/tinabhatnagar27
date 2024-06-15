import random
import string

def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example usage
password_length = 12  # You can change the length as needed
password = generate_password(password_length)
print(f"Generated password: {password}")