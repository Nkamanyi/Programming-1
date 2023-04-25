
def english_to_spanish(word, english_spanish):
    """

    :param word: word given by the user
    :param english_spanish: dic
    :return:
    """
    letters = word.split()
    translated_text = ""

    for i in fields:
        if i in english_spanish:
            translated_text += english_spanish[i]
            translated_text += " "
        else:
            translated_text += i
            translated_text += " "

    print("The text, translated by the dictionary:")
    print(translated_text)


def content_of_dic(english_spanish):
    """
    prints the contents of a dic

    :param english_spanish: the dictionary
    :return:
    """
    contents = ", ".join(sorted(english_spanish))
    print("Dictionary contents:")
    print(contents)


def spanish_to_english(english_spanish):
    """

    :param english_spanish: print spanish to english
    :return:
    """
    new_dic = {value: key for key, value in english_spanish.items()}
    for w in sorted(new_dic):
        print(w, new_dic[w])


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    content_of_dic(english_spanish)

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(word, "in Spanish is", english_spanish[word])
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            english_word = input("Give the word to be added in English: ")
            spanish_word = input("Give the word to be added in Spanish: ")
            english_spanish[english_word] = spanish_word
            content_of_dic(english_spanish)

        elif command == "R":
            removed_word = input("Give the word to be removed: ")
            if removed_word in english_spanish:
                del english_spanish[removed_word]
            else:
                print(f"The word {removed_word} could not be found from the dictionary.")

        elif command == "P":
            print("English-Spanish")
            for w in sorted(english_spanish):
                print(w, english_spanish[w])
            print()
            print("Spanish-English")
            spanish_to_english(english_spanish)

        elif command == "T":
            text = input("Enter the text to be translated into Spanish: ")
            english_to_spanish(word, english_spanish)

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")
main()