import questionary

def make_withdrawal(account_holder):
    withdrawal_amount = int(questionary.text("Enter withdrawal amount:").ask())

    if withdrawal_amount > account_holder["balance"]:
        print("Requested withdrawal amount exceeds available funds.")
        make_withdrawal(account_holder)
    else:
        account_holder["balance"] = account_holder["balance"] - withdrawal_amount
        print(f"You have received cash in the amount of {withdrawal_amount}.")
        return account_holder