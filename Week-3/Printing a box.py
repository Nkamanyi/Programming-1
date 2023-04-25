
def print_box(width,height,mark):
    """
    :param width: width of the box
    :param height: heightof the box
    :param mark: mark to be printed
    :return:
    """
    for i in range(0,height):
        print(width * mark)
def main():

    width = int(input("Enter the width of a frame: "))
    height = int(input("Enter the height of a frame: "))
    mark = input("Enter a print mark: ")
    print()
    print_box(width,height,mark)

main()