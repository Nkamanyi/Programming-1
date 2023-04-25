
def repeat_name(nam,num):
    """

    :param nam: name of the variable
    :param num: number of times the sentence has to be printed
    :return:
    """

    for i in range(0,num):
        print(f"{nam}, {nam} Bear")

def verse(phra,nam):
    """

    :param phra: sentence to be printed
    :param nam: name of the variable
    :return:
    """
    print(phra)
    print(f"{nam}, {nam}")
    print(phra)
    repeat_name(nam,3)
    print(phra)
    print(f"{nam}, {nam} Bear")

def main():
    verse("I know someone you don't know", "Yogi")
    print()
    verse("Yogi has a best friend too", "Boo Boo")
    print()
    verse("Yogi has a sweet girlfriend", "Cindy")

main()

