import questionary

# Create the `make_deposit` function for the ATM application.
# WRITE YOUR LOGIC HERE!
# YOUR CODE HERE!

def make_deposit(account_holder):
    deposit_amount = int(questionary.text("Enter deposit amount:").ask())
    if not deposit_amount > 0:
        print("Deposit amount must be greater than 0.")
        make_deposit(account_holder)
    else:
        #print(account_holder)
        account_holder["balance"] = account_holder["balance"] + deposit_amount
    
    return account_holder