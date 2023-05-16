def withdraw(account_dict, account_num, amount):
    if account_num not in account_dict:
        print("Error: account does not exist")
        return

    if amount <= 0:
        print("Error: amount must be greater than zero")
        return

    if account_dict[account_num] < amount:
        print("Error: insufficient funds")
        return

    account_dict[account_num] -= amount
    print("Withdrawing ${:.2f} from account {}...".format(amount, account_num))
