
def capitalize_initial_letters(sentence):
    """
    :param sentence: given sentence
    :return: sentence with each word capitalize
    """
    new = ""
    for i in sentence.split():

        re = i.strip().capitalize()+ " "
        new += re
    return new.strip()


def main():
    a = capitalize_initial_letters("the boy is handsome")
    print(a)
main()