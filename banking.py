import random
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

delete_table = "DROP TABLE card"
cur.execute(delete_table)

sql = '''CREATE TABLE IF NOT EXISTS card(
   id INTEGER,
   number TEXT,
   pin TEXT,
   balance INTEGER DEFAULT 0
);'''
cur.execute(sql)
conn.commit()

row = cur.fetchall()
for row in cur:
    print(f">>> {row}")

z = 0

id = 0
client_base = []
balance = 0
check = True
card_id = 0

show_balance = 0

def customer_balance():
    # global balance
    # balance = 0
    global show_balance
    # balance = str(show_balance)
    # x = balance.strip("(").strip(")").strip(",").strip(" ")

    # print(f"Balance: {balance}")
    # cur.execute('SELECT balance FROM card WHERE card=')
    # row = cur.fetchoneall()
    # show_balanc = "".join(row)
    cur.execute(f'SELECT balance FROM card WHERE id = {card_id}')
    # conn.commit()
    row3 = cur.fetchone()
    show_balance = row3
    balance = str(show_balance)
    x = balance.strip("(").strip(")").strip(",").strip(" ")
    print(show_balance)

    # print(f"Balance: {x}")
    print(f"Balance: {x}")
    in_banking_system_message()
    customer_choice_in_system()


def random_with_n_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return random.randint(range_start, range_end)


def create_account():
    global id
    id += 1
    sum_custom = 0
    check_sum = 0
    card_number = [4, 0, 0, 0, 0, 0]
    card_number_str = 0
    for i in range(10):
        n = random.randint(0, 9)
        card_number.append(n)
        # cur.execute(f"INSERT INTO ")
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

    cur.execute('INSERT INTO card (id, number, pin) VALUES (?, ?, ?);', (id, card_number_str, pin_number))
    conn.commit()
    # conn.close()

    # print("Your card has been created")
    # print("Your card number:")
    # # print(card_number_str)
    # cur.execute('SELECT number FROM card;')
    # row = cur.fetchone()
    # print(row
    # # conn.commit()
    # print("Your card PIN:")
    # # print()
    # # print(pin_number)
    # cur.execute('SELECT pin FROM card;')
    # # conn.commit()
    # row = cur.fetchone()
    # print(row)
    # print(f">>> {z}")
    # conn.commit()

    # print(client_base)


def read_from_db():
    global z
    global show_balance
    global card_id
    temp_id = str(card_id)
    print("Your card has been created")
    print("Your card number:")
    cur.execute('SELECT number FROM card;')
    row1= cur.fetchall()
    ' '.join(str(y) for y in row1)
    print("".join(row1[z]))
    # conn.commit()
    print("Your card PIN:")
    # print()
    # print(pin_number)
    cur.execute('SELECT pin FROM card;')
    # conn.commit()
    row2 = cur.fetchall()
    print("".join(row2[z]))
    # print("".join(row3[z]))

    z = z + 1


def log_into_account():
    global card_id
    print("Enter your card number:")
    customer_card_number = int(input())
    cur.execute('SELECT number FROM card;')
    row1 = cur.fetchall()
    cur.execute('SELECT pin FROM card;')
    # conn.commit()
    row2 = cur.fetchall()
    
    if any(str(customer_card_number) in i for i in row1):
        # if customer_card_number in row1:
        print("Enter your PIN:")
        customer_pin_number = int(input())
        if any(str(customer_pin_number) in j for j in row2):
            # if customer_pin_number in row2:
            cur.execute(f'SELECT id FROM card where number={customer_card_number}')
            card_id = cur.fetchone()[0]
            print(card_id)
            print("You have successfully logged in!")
        
            in_banking_system_message()
            customer_choice_in_system()
        else:
            print("Wrong card number or PIN!")

    # if customer_card_number in client_base:
    #     print("Enter your PIN:")
    #     customer_pin_number = int(input())
    #
    #     if customer_pin_number in client_base:
    #         print("You have successfully logged in!")
    #
    #         in_banking_system_message()
    #         customer_choice_in_system()
    #     else:
    #         print("Wrong card number or PIN!")
    elif customer_card_number not in client_base:
        print("Wrong card number or PIN!")


def customer_out_from_system():
    out_from_banking_system_message()
    global check
    choice = int(input())
    if choice == 1:
        create_account()
        read_from_db()
    elif choice == 2:
        log_into_account()
    elif choice == 0:
        print("Bye!")
        check = False


def add_income():
    global card_id
    temp_id = str(card_id)
    print("Enter  income:")
    custom_input = input()
    cur.execute('UPDATE card SET balance = balance + ? WHERE id = ?', (custom_input, temp_id))
    conn.commit()
    print("Income was added!")
    in_banking_system_message()
    customer_choice_in_system()

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0


def add_transfer():
    print("Transfer")
    print("Enter card number:")
    card_number_transfer = input()
    cur.execute('SELECT number FROM card;')
    row1 = cur.fetchall()
    if is_luhn_valid(card_number_transfer) != True:
        print("Probably you made a mistake in the card number. Please try again!")
        in_banking_system_message()
        customer_choice_in_system()

    elif any(card_number_transfer in row_value for row_value in row1) == False:
        print("Such a card does not exist.")
        in_banking_system_message()
        customer_choice_in_system()

    elif any(str(card_number_transfer)  in i for i in row1):
        cur.execute(f'SELECT id FROM card where number={card_number_transfer}')
        card_id_local = cur.fetchone()[0]
        if  card_id_local == card_id:
            print("You can't transfer money to the same account!")
            in_banking_system_message()
            customer_choice_in_system()
        else:
            print("Enter how much money you want to transfer:")
            money_for_transfer = input()
            cur.execute(f"SELECT balance FROM card WHERE id={card_id}")
            money_from_transfer_balance = cur.fetchone()[0]
            if money_from_transfer_balance < int(money_for_transfer):
                print("Not enough money!")
                in_banking_system_message()
                customer_choice_in_system()
            else:
                cur.execute('UPDATE card SET balance = balance + ? WHERE id = ?', (money_for_transfer, card_id_local))
                cur.execute('UPDATE card SET balance = balance - ? WHERE id = ?', (money_for_transfer, card_id))
                conn.commit()
                print("Success!")
                in_banking_system_message()
                customer_choice_in_system()


def close_account():
    cur.execute(f'DELETE FROM card WHERE id = {card_id}')
    conn.commit()
    print("The account has been closed!")


def customer_choice_in_system():
    global check
    check = True
    choice = int(input())
    if choice == 1:
        customer_balance()
        customer_choice_in_system()
    if choice == 2:
        add_income()
    if choice == 3:
        add_transfer()
    if choice == 4:
        close_account()
    elif choice == 5:
        # check = False
        customer_out_from_system()
    elif choice == 0:
        print("Bye!")
        check = False


def in_banking_system_message():
    print("1. Balance")
    print("2. Add income")
    print("3. Do transfer")
    print("4. Close account")
    print("5. Log out")
    print("0. Exit")



def out_from_banking_system_message():
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")


while check:
    customer_out_from_system()
