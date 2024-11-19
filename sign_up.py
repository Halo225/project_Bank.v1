import random

# Function to ask if the user has an account and prompt to create one if they don't
def ask_if_has_account():
    while True:
        user_input = input("Do you have an account? (Y/N): ").strip().upper()
        if user_input in ['Y', 'N']:
            if user_input == 'Y':
                print("Great! You have an account.")
            else:
                print("No worries! Let's create an account for you.")
                create_account()
            return user_input
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

# Function to create an account
def create_account():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    account_number = generate_account_number()
    print(f"Account created for {username}!")
    print(f"Your account number is: {account_number}")

# Function to generate a random account number
def generate_account_number():
    return random.randint(1000000000, 9999999999)

# Call the function
ask_if_has_account()


