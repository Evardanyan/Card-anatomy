import random

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
    return random.randint(range_start, range_end)


def create_account():
    sum_custom = 0
    check_sum = 0
    card_number = [4, 0, 0, 0, 0, 0]
    card_number_str = 0
    for i in range(10):
        n = random.randint(0, 9)
        card_number.append(n)
    del card_number[-1]
    card_number_temp = [x for x in card_number]
    # card_number_temp[0] = 2 * card_number_temp[0]

    for i in range(0, len(card_number_temp)):
        if i % 2 == 0:
            card_number_temp[i] = 2 * card_number_temp[i]

    for i in range(len(card_number_temp)):
        if card_number_temp[i] > 9:
            card_number_temp[i] = card_number_temp[i] - 9

    for i in range(len(card_number_temp)):
        sum_custom = sum_custom + card_number_temp[i]
    if sum_custom % 10 == 0:
        check_sum = 0
    else:
        check_sum = 10 - sum_custom % 10

    card_number.append(check_sum)

    card_number_convert = [str(x) for x in card_number]
    card_number_str = int("".join(card_number_convert))

    pin_number = random_with_n_digits(4)
    global client_base
    client_base.append(card_number_str)
    client_base.append(pin_number)
    print("Your card has been created")
    print("Your card number:")
    print(card_number_str)
    print("Your card PIN:")
    print(pin_number)
    # print(client_base)


def log_into_account():
    print("Enter your card number:")
    customer_card_number = int(input())
    if customer_card_number in client_base:
        print("Enter your PIN:")
        customer_pin_number = int(input())
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
