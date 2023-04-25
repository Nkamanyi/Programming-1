
def is_the_list_in_order(list):
    """
    :param list: chosen list of numbers
    :return: boolean whether the list is in ascending order
    """
    if sorted(list)==list:
        return True
    else:
        return False

def main():
    is_the_list_in_order()

main()