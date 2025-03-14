import random
import string

def generate_password(length=12):
    if length < 4:
        return "Password length must be at least 4."

    # Define character sets
    lowercase = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    uppercase = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = string.digits              # '0123456789'
    symbols = string.punctuation        # '!@#$%^&*()_+{}[]...'

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_characters = lowercase + uppercase + digits + symbols
    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)

    return ''.join(password)


if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        print("Generated Password:", generate_password(length))
    except ValueError:
        print("Invalid input! Please enter a number.")
