
PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def item_from_user():
    """
    :return: Allow the user to input an item and it tells the price.
    """
    while True:
        item = input("Enter product name: ").strip()
        if item == "":
            print("Bye!")
            break
        elif item in PRICES:
            print(f"The price of {item} is {PRICES[item]:.2f} e")
        else:
            print(f"Error: {item} is unknown.")


def main():
    item_from_user()
main()
