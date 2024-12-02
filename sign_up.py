import random, hashlib, csv
# from os import write
from Main import main

def ask_if_has_account():
    while True:
        user_input = input("Do you have an account? (Y/N): ").upper()
        if user_input in ['Y', 'N']:
            if user_input == 'Y':
                print("Great! You have an account.")
                login_account()
            else:
                print("No worries! Let's create an account for you.")
                create_account()
                print("Your accounts has been created, Now log in")
                login_account()
                main()
            return user_input
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")


def hash_password(password):
    password_bytes = password.encode()
    hash_object = hashlib.sha256(password_bytes)
    hex_dig = hash_object.hexdigest()
    return hex_dig

def create_account():
    while True:
        username = input("Enter a username: ").strip()
        if not username:
            print("Username cannot be empty. Please try again.")
            continue

        email = input("Enter an email address: ").strip()
        if not email or "@" not in email:
            print("Invalid email address. Please try again.")
            continue

        password = input("Enter a password: ").strip()
        if not password:
            print("Password cannot be empty. Please try again.")
            continue

        hashed_password = hash_password(password)
        account_number = generate_account_number()
        save_account(username, email, hashed_password, account_number)
        print(f"Account created for {username}! Your Account number is: {account_number}")
        break


def generate_account_number():
    return random.randint(1000000000, 9999999999)


def login_account():
    attempts = 0
    while attempts < 3:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        hashed_password = hash_password(password)

        with open('sign_up.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[2] == hashed_password:
                    print(f"Login successful! Welcome to Maze_bank, {username}")
                    main()
                    return
        attempts += 1
        if attempts < 3:
            print(f"Login failed. Invalid username or password. You have {3 - attempts} attempts left.")
        else:
            print("Login failed. No attempts left. Please try again later.")



def save_account(username, email, password, account_number):
    with open("sign_up.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, email, password, account_number])
        # print(f'Account saved: {username}, {email}, {password}, {account_number}')

ask_if_has_account()




