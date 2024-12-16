import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("Here is the Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be a positive number")
            return
        password = generate_password(length)
        print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")
if __name__ == "__main__":
    main()
