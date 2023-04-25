
PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    #TODO
    def payload(key):
        return PRICES[key]

    for i in sorted(PRICES, key=payload):
        print(f"{i} {PRICES[i]:.2f}")

main()