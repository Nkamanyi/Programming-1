
def print_box(width, height, border_mark = "#", inner_mark = " "):
    """
    This function prints the box with the marks the user has picked.
    :param width: width of the desire shape
    :param height: height of the desire shape
    :param border_mark: border mark for the desire shape
    :param inner_mark: inner mark for the desire shape
    :return:
    """
    print(border_mark * width)
    for i in range(2, height):
        print(border_mark, inner_mark * (width - 2), border_mark, sep="")
    print(border_mark * width)


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)

main()