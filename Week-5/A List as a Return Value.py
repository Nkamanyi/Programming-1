
def input_to_list(num):
    """
    :param num: number of numbers we need in the list
    :return: the list
    """
    list = []
    for i in range(1,num+1):
        list.append(int(input()))
    return list


def main():
    num = int(input("How many numbers do you want to process: "))
    print(f"Enter {num} numbers:")
    list = input_to_list(num)
    num_ser = int(input("Enter the number to be searched: "))
    if list.count(num_ser) >=1:
        print(f"{num_ser} shows up {list.count(num_ser)} times among the numbers you have entered.")
    else:
        print(f"{num_ser} is not among the numbers you have entered.")

main()