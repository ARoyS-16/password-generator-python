import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== PASSWORD GENERATOR ===")
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Length must be positive.")
            return
        password = generate_password(length)
        print("Generated Password:", password)
    except:
        print("Please enter a valid number.")

main()
