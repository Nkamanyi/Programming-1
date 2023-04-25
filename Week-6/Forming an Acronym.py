
def create_an_acronym(word):
    """
    :param word: given word
    :return: acronym of give word
    """
    acro = ""
    for i in word.split():
        res = i[0].upper()
        acro += res
    return acro

def main():
    print(create_an_acronym("central intelligence agency"))
main()
