"""This is a basic ATM Application.

This is a program consists of the basic actions of an ATM.

Example:
    $ python app.py
"""

import questionary
import csv
from pathlib import Path
from utils import load_accounts
from actions.make_deposit import make_deposit
from utils import determine_transaction_type
from utils import login
import sys

# Create the `check_balance` function for the ATM application.
# WRITE YOUR LOGIC HERE!
# YOUR CODE HERE!
    
def run():

    accounts = load_accounts()

    account_holder = {
        "username": " ",
        "pin": 0,
        "balance": 0,
    }
    
    account_holder["username"] = questionary.text("Enter username:").ask()
    account_holder["pin"] = int(questionary.text("Enter PIN:").ask())
    
    account_holder = login(accounts, account_holder)

    transaction_type = questionary.text("Would you like to make a deposit or a withdrawal?").ask()

    transaction_type = determine_transaction_type(transaction_type, account_holder)
    print(account_holder)

run()