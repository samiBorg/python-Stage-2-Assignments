from deposit import deposit
from withdraw import withdraw


def main():
    account_dict = {"1": 100, "2": 13000, "3": 4000}
    while True:
        print("Bank services:")
        print("1. Create Account")
        print("2. Check balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            account_num = input("Enter account number: ")
            if account_num in account_dict:
                print("Error: account already exists")
            else:
                account_dict[account_num] = 100.0
                print("Account {} created successfully".format(account_num))

        elif choice == "2":
            account_num = input("Enter account number: ")
            print("Account Details: Account No.: {}, Balance: {}".format(account_num, account_dict[account_num]))

        elif choice == "3":
            account_num = float(input("Enter account number: "))
            amount = input("Enter deposit amount: ")
            deposit(account_dict, account_num, amount)

        elif choice == "4":
            account_num = float(input("Enter account number: "))
            amount = input("Enter withdrawal amount: ")
            withdraw(account_dict, account_num, amount)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Error: invalid choice")


if __name__ == "__main__":
    main()
