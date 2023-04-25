
def english_to_spanish(words, english_spanish):
    """
    :param words: word given by the user
    :param english_spanish: dic
    :return:
    """
    letters = words.split()
    translated_word = ""

    for i in letters:
        if i in english_spanish:
            translated_word += english_spanish[i]
            translated_word += " "
        else:
            translated_word += i
            translated_word += " "

    print("The text, translated by the dictionary:")
    print(translated_word)


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

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

        elif command == "R":
            removed_word = input("Give the word to be removed: ")
            if removed_word in english_spanish:
                del english_spanish[removed_word]
            else:
                print(f"The word {removed_word} could not be found from the dictionary.")

        elif command == "P":
            for w in sorted(english_spanish):
                print(w, english_spanish[w])

        elif command == "T":
            text = input("Enter the text to be translated into Spanish: ")
            english_to_spanish(text, english_spanish)

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")

main()