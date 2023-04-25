
def longest_substring_in_order(word):
    """
    :param word: the word given by the user
    :return: the longest substring
    """
    sub_string = ""
    tmp_string = ""
    for index in range(len(word)):
        tmp_string += word[index]
        if len(tmp_string) > len(sub_string):
            sub_string = tmp_string
        if index > len(word)-2:
            break
        if word[index] > word[index + 1]:
            tmp_string = ""

    return sub_string


def main():
    word = input("Enter a word: ")
    print(longest_substring_in_order(word))

main()