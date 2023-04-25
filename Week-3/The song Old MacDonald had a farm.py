
def print_verse(ani,voca):
    """
    :param ani: variable for the animal
    :param voca: variable for the sound of the animal
    :return:
    """

    print(f"Old MACDONALD had a farm")
    print(f"E-I-E-I-O")
    print(f"And on his farm he had a {ani}")
    print(f"E-I-E-I-O")
    print(f"With a {voca} {voca} here")
    print(f"And a {voca} {voca} there")
    print(f"Here a {voca}, there a {voca}")
    print(f"Everywhere a {voca} {voca}")
    print(f"Old MacDonald had a farm")
    print(f"E-I-E-I-O")

def main():
    print_verse("cow", "moo")
    print()
    print_verse("pig", "oink")
    print()
    print_verse("duck", "quack")
    print()
    print_verse("horse", "neigh")
    print()
    print_verse("lamb", "baa")

main()