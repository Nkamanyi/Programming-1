
def read_message():
    """
    :return: input given by the user
    """
    information = []
    while True:
        user_input = input("")
        if user_input == "":
            break
        else:
            information.append(user_input)
    return information


def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    res = ""
    print("The same, shouting:")
    for i in msg:
        print(i.upper())

main()