class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited UGX {amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid amount.")
        else:
            self.balance -= amount
            print(f"Withdrawn UGX {amount:.2f}")

    def check_balance(self):
        print(f"Current Balance: UGX {self.balance:.2f}")


# -------- Main Program --------
name = input("Enter account holder name: ")
account = BankAccount(name)

while True:
    print("\n--- BANK MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        print("Thank you for using the system.")
        break

    else:
        print("Invalid option. Try again.")
