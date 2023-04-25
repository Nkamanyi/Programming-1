
def print_box(width,height,mark):
    """
    Creates a box whose size depends on the parameters
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
        b = int(input(q))
        if b > 0:
            a = False
            return b

def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()

    print_box(width, height, mark)

main()
