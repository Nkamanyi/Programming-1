
def print_box(width,height,mark):
    """

    :param width: width of the box
    :param height: heightof the box
    :param mark: mark to be printed
    :return:
    """
    for i in range(0,height):
        print(width * mark)

def read_input(q):
    """
    accept input from user
    """
    a = True
    while a:
        try:
            b = int(input(q))
            if b > 0:
                a = False
                return b
        except ValueError:
            continue

def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()

    print_box(width, height, mark)

if __name__ == "__main__":
    main()
