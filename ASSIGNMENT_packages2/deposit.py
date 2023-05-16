def deposit(account_dict, account_num, amount):
    if account_num not in account_dict:
        print("Error: account does not exist")
        return

    if amount <= 0:
        print("Error: amount must be greater than zero")
        return

    account_dict[account_num] += amount
    print("Depositing ${:.2f} into account {}...".format(amount, account_num))
