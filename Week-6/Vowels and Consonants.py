
def number_of_vowels_and_consonants(word):
   """
   :param word: the word entered by the user
   :return: the number of vowels and consonants
   """
   conso = 0
   vow = 0
   for k in range(0,len(word)):
       if word[k] == "a" or word[k] == "e" or word[k] == "i" or word[k] == "o" or word[k] == "u" or word[k] == "y":
           vow += 1
       else:
           conso += 1

   print(f"The word \"{word}\" contains {vow} vowels and {conso} consonants.")


def main():
    word = input("Enter a word: ")
    number_of_vowels_and_consonants(word)

main()