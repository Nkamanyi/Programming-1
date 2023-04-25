
def word_reader():
    """
    read the word input by the user
    :return:
    """

    print("Enter rows of text for word counting. Empty row to quit.")
    word_string = ""
    while True:
        word = input()
        if word == "":
            break
        else:
            word_string += word
            word_string += " "

    return word_string.lower()


def counter():
    """
    Counts word input by the user
    :return:
    """
    word = word_reader().split()
    word_dic = {}
    for w in word:
        if w in word_dic:
            word.count(w)
        else:
            word_dic[w] = word.count(w)

    return word_dic


def calculator():
    """
    Prints the dictionary that is included word in alphabetical order
    :return:
    """
    word_dic = counter()
    for w in sorted(word_dic):
        print(f"{w} : {word_dic[w]} times")


def main():
    calculator()

main()