from pathlib import Path
import csv
from actions.make_deposit import make_deposit
from actions.make_withdrawal import make_withdrawal
import questionary

def login(accounts, account_holder):
    
    for account in accounts:
        if account["username"] == account_holder["username"]:
            if account["pin"] == account_holder["pin"]:
                account_holder["balance"] = account["balance"]
                print(account_holder)
                return account_holder

def load_accounts():

    accounts = []
    filepath = Path("./data/accounts.csv")
    
    with open (filepath, newline='') as csvfile:
        filereader = csv.reader(csvfile)
        skip_header = next(filereader)

        for row in filereader:
            username = row[0]
            pin = int(row[1])
            balance = float(row[2])

            account = {
                "username": username,
                "pin": pin,
                "balance": balance
            }

            accounts.append(account)

        return accounts

def determine_transaction_type(transaction_type, account_holder):
    
    if transaction_type == "deposit":
        make_deposit(account_holder)
        return account_holder
    elif transaction_type == "withdrawal":
        make_withdrawal(account_holder)
        return account_holder
    else:
        print(f"{transaction_type} is not a valid transaction type.  Please make a valid selection.")
        transaction_type = questionary.text("Would you like to make a deposit or a withdrawal?").ask()
        determine_transaction_type(transaction_type, account_holder)