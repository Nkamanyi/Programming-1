
def read_message():
    """

    :return: it takes a phrase from the user and return a list of string
    """
    message = []
    while True:
        msg = input("")
        if msg == "":
            break
        else:
            message.append(msg)
            continue

    return message


def encrypt(phrase):
    """

    :param phrase: phrase to be encrypted
    :return: the encrypted phrase using the ROT13
    """

    regular_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                     "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]


    ch = ""
    i = 0
    for index in range(len(phrase)):
        while i < len(regular_chars):
            if phrase[index].isupper():
                k = phrase[index].lower().find(regular_chars[i])
                if k == 0:
                    ch = phrase[index].lower().replace(regular_chars[i], encrypted_chars[i])
                    return ch.upper()
                else:
                    ch = phrase[index]
                i += 1
            else:
                j = phrase[index].find(regular_chars[i])
                if j == 0:
                    ch = phrase[index].replace(regular_chars[i], encrypted_chars[i])
                    break
                else:
                    ch = phrase[index]
                i += 1
        return ch


def row_encryption(phrase_string):
    """

    :param phrase_string: the phrase string to be encrypted
    :return: encrypted phrase
    """
    encrypted_string = ""
    for ch in phrase_string:
        encrypted_string += encrypt(ch)

    return encrypted_string


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("ROT13:")
    for m in msg:
        print(row_encryption(m))

main()