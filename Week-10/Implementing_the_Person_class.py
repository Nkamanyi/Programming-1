
class Person:
    def __init__(self, name, money, address):

        self.__name = name
        self.__money = money
        self.__address = address

    def printout(self):
        print("-" * 25)
        print("Name: ", self.__name)
        print("Wealth: ", self.__money)
        print("Address: ", self.__address)

    def add_money(self, amount):
        if amount < 0.0:
            return False
        else:
            self.__money += amount
            return True


    def make_payment(self, price):
        if price < 0.0:
            print("The price can't be negative.")
        elif price > self.__money:
            print("You can't afford that.")
        else:
            self.__money -= price

    def move(self, address):
        if address != self.__address:
            self.__address = address

def main():

    denzil = Person("Denzil Dexter", 100.00, "Tammelan Puistokatu")
    dave = Person("Dave Angel", 8.21, "Sammonkatu")
    bob = Person("Bob", 62.79, "Hammeankatu")


    denzil.printout()
    dave.printout()
    bob.printout()
    print()
    denzil.add_money(50.0)
    dave.add_money(70.0)
    bob.add_money(100.0)
    print()
    denzil.move("Kullervonkatu")
    dave.move("Tursokatu")
    bob.move("Papinkatu")
    print()
    denzil.printout()
    dave.printout()
    bob.printout()

main()
