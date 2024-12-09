import random
import string

# Function to generate a random password
def generate_password(length=12):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting characters from the set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for password length
length = int(input("Enter the desired password length: "))

# Generate and display the password
password = generate_password(length)
print(f"Your generated password is: {password}")
