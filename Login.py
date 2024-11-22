from sign_up import hash_password
import csv


def login_account():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed_password = hash_password(password)

    with open('sign_up.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
         if row [0] == username and row[2] == hashed_password:
             print(f"Login successful! Welcome back, {username}")
             return
         print("Login failed. Invalid username or password.")
