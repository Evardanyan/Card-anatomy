from random import randint

client_base = []
balance = 0
check = True


def customer_balance():
    global balance
    balance = 0
    print(f"Balance: {balance}")
    in_banking_system_message()
    customer_choice_in_system()


def random_with_n_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


def create_account():
    card_number = "400000" + str(random_with_n_digits(10))
    pin_number = str(random_with_n_digits(4))
    global client_base
    client_base.append(card_number)
    client_base.append(pin_number)
    print("Your card has been created")
    print("Your card number:")
    print(card_number)
    print("Your card PIN:")
    print(pin_number)
    print(client_base)


def log_into_account():
    print("Enter your card number:")
    customer_card_number = input()
    if customer_card_number in client_base:
        print("Enter your PIN:")
        customer_pin_number = input()
        if customer_pin_number in client_base:
            print("You have successfully logged in!")
            in_banking_system_message()
            customer_choice_in_system()
        else:
            print("Wrong card number or PIN!")
    elif customer_card_number not in client_base:
                print("Wrong card number or PIN!")


def customer_out_from_system():
    out_from_banking_system_message()
    global check
    choice = int(input())
    if choice == 1:
        create_account()
    elif choice == 2:
        log_into_account()
    elif choice == 0:
        print("Bye!")
        check = False


def customer_choice_in_system():
    global check
    check = True
    choice = int(input())
    if choice == 1:
        customer_balance()
        customer_choice_in_system()
    elif choice == 2:
        # check = False
        customer_out_from_system()
    elif choice == 0:
        print("Bye!")
        check = False


def in_banking_system_message():
    print("1. Balance")
    print("2. Log out")
    print("0. Exit")


def out_from_banking_system_message():
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")


while check:
    customer_out_from_system()

