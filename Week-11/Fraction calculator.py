
class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def __lt__(self, other):
        """
        Tells if the fraction is less than the 2nd fraction

        :param other: frac, the fraction to compare with
        :return:bool, True if less than, False if less than
        """
        return (self.__numerator/self.__denominator) < other

    def __gt__(self, other):
        """
        Tells if the fraction is greater than the 2nd fraction

        :param other: frac, fraction being compared to
        :return: bool, True if greater and False if less than
        """
        return (self.__numerator/self.__denominator) > other

    def __str__(self):
        """
        Returns the object's string representation

        :return: str, string representation of the fraction
        """
        if self.__numerator * self.__denominator < 0:
            sign = "-"
        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        d = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator//d
        self.__denominator = self.__denominator//d
        return f"{self.__numerator}/{self.__denominator}"

    def multiply(self, frac2):
        """
        Calculates the product of two fractions

        :param frac2: frac, the fraction being multiplied with
        :return: frac, the result of the multiplication
        """
        product = Fraction(self.__numerator * frac2.__numerator, self.__denominator * frac2.__denominator)

        return product


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a


def main():
    calculator = {}

    try:
        while True:
            command = input("> ")
            if command == "add":
                string_input = input("Enter a fraction in the form integer/integer: ")
                fields = string_input.split("/")
                frac = Fraction(int(fields[0]), int(fields[1]))

                name = input("Enter a name: ")
                calculator[name] = frac

            elif command == "quit":
                print("Bye bye!")
                break

            elif command == "print":
                to_print = input("Enter a name: ")
                if to_print in calculator:
                    print(f"{to_print} = {calculator[to_print]}")
                else:
                    print(f"Name {to_print} was not found")
                continue

            elif command == "list":
                if len(calculator) > 0:
                    for f in sorted(calculator):
                        print(f"{f} = {calculator[f]}")
                continue

            elif command == "*":
                frac1 = input("1st operand: ")
                if frac1 not in calculator.keys():
                    print(f"Name {frac1} was not found")
                    continue
                frac2 = input("2nd operand: ")
                if frac2 not in calculator.keys():
                    print(f"Name {frac2} was not found")
                    continue

                print(f"{calculator[frac1]} * {calculator[frac2]} = {calculator[frac1].multiply(calculator[frac2])}")
                print("simplified", (calculator[frac1].multiply(calculator[frac2])).simplify())
                continue

            elif command == "file":
                try:
                    filename = input("Enter the name of the file: ")

                    file = open(filename, mode="r")
                    for line in file:
                        lines = line.rstrip().split("=")
                        calculator[lines[0]] = lines[1]
                        values = lines[1].split("/")
                        frak = Fraction(int(values[0]), int(values[1]))
                        calculator[lines[0]] = frak
                    continue

                except OSError:
                    print("Error: the file cannot be read.")
                except IndexError:
                    print("Error: the file cannot be read.")
            else:
                print("Unknown command!")
                continue

    except ValueError:
        raise print("Value error")


if __name__ == '__main__':
    main()