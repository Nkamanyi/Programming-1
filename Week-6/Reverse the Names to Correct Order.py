
def reverse_name(word):
    """
    :param word: the given names in wrong order
    :return: the names in right order
    """
    if word == ",":
        return "".strip()
    elif word.find(",") == -1:
        return word.strip()
    else:
        return " ".join(reversed(word.strip().split(","))).strip()

def main():
    print(reverse_name("   Duck,     Donald  "))
main()
