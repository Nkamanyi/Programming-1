
def main():
    age = int(input("Please, enter your age: "))

    if 16 < age < 25:
        ticket_price = 1.47
    elif 6 < age < 17:
        ticket_price = 1.02
    elif age < 7:
        ticket_price = 0.00
    else:
        ticket_price = 2.04
    print(f"Your ride will cost: {ticket_price}")
main()

