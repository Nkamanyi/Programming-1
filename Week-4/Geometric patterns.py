
def circumferen_of_square(length_square):
    """
    :param length_square: length of a square side
    :return: the circumference of a square
    """
    res_sq = length_square*4
    return res_sq

def surfa_area_of_square(length_square):
    """
    :param length_square: length of a square side
    :return: surface area of a square
    """
    res_sq = length_square**2
    return res_sq

def circumferen_of_rectangle(side_1,side_2):
    """
    :param side_1: length of the first side of a rectangle
    :param side_2: length of the second side of a rectangle
    :return: circumference of a rectangle
    """
    res_rect = (side_1+side_2)*2
    return res_rect

def surfa_area_of_rectangle(side_1,side_2):
    """
    :param side_1: length of the first side of a rectangle
    :param side_2: length of the second side of a rectangle
    :return: surface area of a rectangle
    """
    res_rect = side_1*side_2
    return res_rect

def cicumferen_of_circle(radius):
    """
    :param radius: radius of the circle
    :return: circumference of the circle
    """
    pi = 3.141592653589793238462643383279502
    res_cir = 2*pi*radius
    return res_cir

def surfa_area_of_circle(radius):
    """
    :param radius: radius of the circle
    :return: area of the circle
    """
    pi = 3.141592653589793238462643383279502
    res_cir = pi*radius**2
    return res_cir



def menu():
    """
    This function prints a menu for user to select which
    geometric shape to use in calculations.
    """

    while True:
        answer = input("Enter the pattern's first letter or (q)uit: ")
        if answer == "s":
            length_square = float(input("Enter the length of the square's side: "))
            while length_square <= 0:
                length_square = float(input("Enter the length of the square's side: "))
                continue
            print(f"The circumference is {circumferen_of_square(length_square):.2f}")
            print(f"The surface area is {surfa_area_of_square(length_square):.2f}")

        elif answer == "r":
            side_1 = float(input("Enter the length of the rectangle's side 1: "))
            while side_1 <= 0:
                side_1 = float(input("Enter the length of the rectangle's side 1: "))
                continue
            side_2 = float(input("Enter the length of the rectangle's side 2: "))
            while side_2 <= 0:
                side_2 = float(input("Enter the length of the rectangle's side 2: "))
                continue
            print(f"The circumference is {circumferen_of_rectangle(side_1,side_2):.2f}")
            print(f"The surface area is {surfa_area_of_rectangle(side_1,side_2):.2f}")

        elif answer == "c":
            radius = float(input("Enter the circle's radius: "))
            while radius <= 0:
                radius = float(input("Enter the circle's radius: "))
                continue
            print(f"The circumference is {cicumferen_of_circle(radius):.2f}")
            print(f"The surface area is {surfa_area_of_circle(radius):.2f}")

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        print()  # Empty row for the sake of readability


def main():
    menu()
    print("Goodbye!")

main()