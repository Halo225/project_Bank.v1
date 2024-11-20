import random

def ask_if_has_account():
    while True:
        user_input = input("Do you have an account? (Y/N): ").upper()
        if user_input in ['Y', 'N']:
            if user_input == 'Y':
                print("Great! You have an account.")
            else:
                print("No worries! Let's create an account for you.")
                create_account()
            return user_input
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

def create_account():
    username = input("Enter a username: ")
    email = input("Enter an email address: ")
    password = input("Enter a password: ")
    account_number = generate_account_number()
    print(f"Account created for {username}!")
    print(f"Your account number is: {account_number}")


def generate_account_number():
    return random.randint(1000000000, 9999999999)

ask_if_has_account()


# i am trying to get it to save the account created but it is not working
def save_account(username, email, password, account_number):
    with open("sign_up.csv", "a") as file:
        file.write(",".join([username, email, password, account_number]) + "\n")


