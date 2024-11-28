import csv

def hash_password(password):
    return "hashed_" + password

def generate_account_number():
    import random
    return str(random.randint(10000000, 99999999))



def store_transaction(transaction_type, amount):
    with open('transactions.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([transaction_type, amount])
    print(f"{transaction_type.capitalize()} of ${amount} recorded in transactions.csv.")
