import random

class BankApp:
    def __init__(self):
        self.pin = "pin"
        self.account_num = "account_num"
        self.balance = 0
        self.my_pin = "my_pin"
        self.my_account = "my_account"

    def home_page(self):
        print("\n1. Create an account\n2. Log into account\n0. Exit")

    def create_account(self):
        password = random.sample(range(10), 4)
        self.pin = "".join((str(num) for num in password))
        account1_ = "400000"
        account2 = random.sample(range(10), 9)
        account2_ = "".join(str(num) for num in account2)
        account3_ = random.randint(0, 10)
        self.account_num = account1_ + account2_ + str(account3_)
        print(f"\nYour card has been created\nYour card number:{self.account_num}\nYour card PIN:\n{self.pin}")

    def login_info(self):
        print("Enter your card number:")
        self.my_account = input()
        print("Enter your PIN:")
        self.my_pin = input()

    def after_balance(self):
        while True:
            print("\n1. Balance\n2. Log out\n0. Exit")
            choice2 = input()
            if choice2 == "1":
                print(f"Balance: {self.balance}")
            elif choice2 == "2":
                print("\nYou have successfully logged out!")
                break
            elif choice2 == "0":
                print("\nBye!")
                exit()

    def verify_login(self):
        if self.my_pin == self.pin and self.my_account == self.account_num:
            print("\nYou have successfully logged in!\n1. Balance\n2. Log out\n0. Exit")
            choices = input()
            if choices == "1":
                print(f"Balance: {self.balance}")
            elif choices == "2":
                print("\nYou have successfully logged out!")
                exit()
            elif choices == "0":
                print("Bye!")
                exit()
        else:
            print("\nWrong card number or PIN!")


bank = BankApp()


while True:
    bank.home_page()
    choice = input()
    if choice == "1":
        bank.create_account()
    elif choice == "2":
        bank.login_info()
        bank.verify_login()
        bank.after_balance()
    elif choice == "0":
        print("Bye!")
        break
