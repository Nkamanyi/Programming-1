
def count_abbas(word):
    """
    :param word: word given by the user
    :return: the number of abba in the word
    """
    i = 0
    counter = 0
    while i < len(word):
        if word[i: i+4] == "abba":
            counter += 1
        i += 1

    return counter


def main():
    word = input("Enter a word: ")
    print(count_abbas(word))

main()