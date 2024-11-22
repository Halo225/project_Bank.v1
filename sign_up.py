import random
import csv
import hashlib
from os import write


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
            return user_input
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")


def hash_password(password):
    password_bytes = password.encode()
    hash_object = hashlib.sha256(password_bytes)
    hex_dig = hash_object.hexdigest()
    return hex_dig


def create_account():
    username = input("Enter a username: ")
    email = input("Enter an email address: ")
    password = input("Enter a password: ")
    hashed_password = hash_password(password)
    save_account(username, email, hashed_password, account_number=(generate_account_number()))
    # print(f"Hashed Password: {hashed_password}")
    account_number = generate_account_number()
    print(f"Account created for {username}!, Your Account number is:{account_number}")



def generate_account_number():
    return random.randint(1000000000, 9999999999)



def save_account(username, email, password, account_number):
    with open("sign_up.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, email, password, account_number])
        # print(f'Account saved: {username}, {email}, {password}, {account_number}')

ask_if_has_account()




