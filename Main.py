import csv


def main():
    print("Welcome to Your Bank!")
    print("What would you like to do today?")

    while True:
        print("1. View Account Balance")
        print("2. Withdraw Funds")
        print("3. Transfer Funds")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            view_balance()
            break
        elif choice == '2':
            withdraw_funds()
            break
        elif choice == '3':
            transfer_funds()
            break
        else:
            print("Invalid choice. Please try again.")


def view_balance():
    # Logic for viewing account balance
    print("Your account balance is $XXXX.XX")


def withdraw_funds():
    # Logic for withdrawing funds
    amount = input("Enter the amount to withdraw: ")
    print(f"${amount} has been withdrawn from your account.")


def transfer_funds():
    # Logic for transferring funds
    recipient = input("Enter the recipient's account number: ")
    amount = input("Enter the amount to transfer: ")
    print(f"${amount} has been transferred to account {recipient}.")


if __name__ == "__main__":
    main()

