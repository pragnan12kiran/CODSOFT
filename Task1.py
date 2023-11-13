import string
import random

def password_generator(length):
    all_characters = string.ascii_letters + string.digits
    if length < 6:
        print("Password length must be at least 6 characters")
        return
    while True:
        password = ''.join(random.choice(all_characters) for i in range(length))
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password)):
            return password

def get_user_input():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length >= 6:
                return length
            else:
                print("Password length must be at least 6 characters")
        except ValueError:
            print("Please enter a valid integer")

def main():
    length = get_user_input()
    password = password_generator(length)
    print("Generated Password: ", password)

if __name__ == "__main__":
    main()
