import csv
from sign_up import login_account


def main():
    username = login_account()
    if not username:
        return
    print(f"Welcome to Your Bank, {username}!")
    print("What would you like to do today?")

    while True:
        print("\n1. View Account Balance")
        print("2. Withdraw Funds")
        print("3. Transfer Funds")
        print("4. Deposit Funds")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            view_balance(username)
        elif choice == '2':
            withdraw_funds(username)
        elif choice == '3':
            transfer_funds(username)
        elif choice == '4':
            deposit_funds(username)
        else:
            print("Invalid choice. Please try again.")

def view_balance(username):
    balance = get_balance(username)
    if balance is not None:
        print(f"Your account balance is ${balance}")
    else:
        print("Account not found.")

def withdraw_funds(username):
    amount = input("Enter the amount to withdraw: ")
    current_balance = get_balance(username)
    if current_balance is not None:
        new_balance = float(current_balance) - float(amount)
        update_balance(username, new_balance)
        print(f"${amount} has been withdrawn from your account.")
    else:
        print("Account not found.")

def transfer_funds(username):
    recipient = input("Enter the recipient's account number: ")
    amount = input("Enter the amount to transfer: ")
    current_balance = get_balance(username)
    recipient_balance = get_balance_by_account_number(recipient)
    if current_balance is not None and recipient_balance is not None:
        new_balance = float(current_balance) - float(amount)
        new_recipient_balance = float(recipient_balance) + float(amount)
        update_balance(username, new_balance)
        update_balance_by_account_number(recipient, new_recipient_balance)
        print(f"${amount} has been transferred to account {recipient}.")
        store_transaction("transfer_funds", amount)
    else:
        print("Account not found.")

def deposit_funds(username):
    amount = input("Enter the amount to deposit: ")
    current_balance = get_balance(username)
    if current_balance is not None:
        new_balance = float(current_balance) + float(amount)
        update_balance(username, new_balance)
        print(f"${amount} has been deposited into your account.")
        store_transaction("deposit", amount)
    else:
        print("Account not found.")

def get_balance(username):
    with open('sign_up.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                return row[4]
    return None

def get_balance_by_account_number(account_number):
    with open('sign_up.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[3] == account_number:
                return row[4]
    return None

def update_balance(username, new_balance):
    rows = []
    updated = False
    with open('sign_up.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                row[4] = new_balance
                updated = True
            rows.append(row)

    if updated:
        with open('sign_up.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"Balance updated for {username} to ${new_balance}")
    else:
        print("Account not found.")

def update_balance_by_account_number(account_number, new_balance):
    rows = []
    updated = False
    with open('sign_up.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[3] == account_number:
                row[4] = new_balance
                updated = True
            rows.append(row)

    if updated:
        with open('sign_up.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"Balance updated for account number: {account_number} to ${new_balance}")
    else:
        print("Account number not found.")

if __name__ == "__main__":
    main()
