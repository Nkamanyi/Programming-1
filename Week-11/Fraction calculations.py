
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
        """
        Simplifies the numerator and denominator by diving it with the greatest number divisible by
        both using the function greatest_common_divisor()

        :return: None
        """
        d = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator = self.__numerator//d
        self.__denominator = self.__denominator//d

    def complement(self):
        """
        Returns the complementary of the fraction

        :return: frac, the complementary of the input fraction
        """
        if self.__denominator < 0 and self.__numerator < 0:
            return Fraction(abs(self.__denominator) - abs(self.__numerator), abs(self.__denominator))
        elif self.__numerator < 0 and self.__denominator > 0:
            return Fraction(self.__denominator + self.__numerator, self.__denominator)
        elif self.__numerator > 0 and self.__denominator < 0:
            return Fraction(abs(self.__denominator) - self.__numerator, abs(self.__denominator))

        return Fraction(self.__numerator - self.__denominator, self.__denominator)

    def reciprocal(self):
        """
        Returns the reciprocal of the fraction

        :return: fra, the reciprocal of the input fraction
        """
        frac = Fraction(self.__denominator, self.__numerator)

        return frac

    def multiply(self, frac2):
        """
        Calculates the product of two fractions

        :param frac2: frac, the fraction being multiplied with
        :return: frac, the result of the multiplication
        """
        product = Fraction(self.__numerator * frac2.__numerator, self.__denominator * frac2.__denominator)

        return product

    def divide(self, frac2):
        """
        Calculates the division of two fractions

        :param frac2: fra, the 2nd fraction
        :return: frac, the result of division
        """
        frac2 = frac2.reciprocal()
        quotient = Fraction(self.__numerator, self.__denominator)

        return quotient.multiply(frac2)

    def add(self, frac2):
        """
        Calculates and returns the addition result of two fractions

        :param frac2: the fraction being added
        :return: frac, the result of the addition
        """
        x = self.__denominator
        y = frac2.__denominator

        self.__numerator = self.__numerator * y
        self.__denominator = self.__denominator * y
        frac2.__numerator = frac2.__numerator * x
        frac2.__denominator = frac2.__denominator * x

        sum = Fraction(self.__numerator + frac2.__numerator, x * y)

        return sum

    def deduct(self, frac2):
        """
        Calculates and returns the subtraction of two fractions

        :param frac2: frac, the fraction being subtracted
        :return: frac, the result of subtraction
        """
        x = self.__denominator
        y = frac2.__denominator

        self.__numerator = self.__numerator * y
        self.__denominator = self.__denominator * y
        frac2.__numerator = frac2.__numerator * x
        frac2.__denominator = frac2.__denominator * x

        difference = Fraction(self.__numerator - frac2.__numerator, x * y)

        return difference


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
    frac = Fraction(2, 4)
    print(frac.return_string())

    complement = frac.complement()
    print(complement.return_string())

    reciprocal = frac.reciprocal()
    print(reciprocal.return_string())

    frac1 = Fraction(2, 3)
    frac2 = Fraction(1, 6)

    product = frac1.multiply(frac2)
    print(product.return_string())

    product.simplify()
    print(product.return_string())

    quotient = frac1.divide(frac2)
    print(quotient.return_string())
    quotient.simplify()
    print(quotient.return_string())

    sum = frac1.add(frac2)
    print(sum.return_string())
    sum.simplify()
    print(sum.return_string())

    difference = frac1.deduct(frac2)
    print(difference.return_string())
    difference.simplify()
    print(difference.return_string())


if __name__ == '__main__':
    main()