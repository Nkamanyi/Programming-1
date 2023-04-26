
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
    fractions = []

    try:
        print("Enter fractions in the format integer/integer."
              "\nOne fraction per line. Stop by entering an empty line.")
        while True:
            string_input = input()
            if string_input == "":
                break

            fields = string_input.split("/")
            frac = Fraction(int(fields[0]), int(fields[1]))

            fractions.append(frac)

        print("The given fractions in their simplified form:")
        for f in fractions:
            print(f"{f} = {f.simplify()}")

    except ValueError:
        raise print("Value error")


if __name__ == '__main__':
    main()