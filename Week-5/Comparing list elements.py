
def are_all_members_same(list):
    """
    :param list: list of elements
    :return: compare if the elements in a list a same
    """
    if len(list) == 0 or len(list) == list.count(list[0]):
        return True
    else:
        return False

def main():
    are_all_members_same([42, 42, 43, 42, 42])

main()