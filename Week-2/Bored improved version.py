
def main():
    bored = True

    while bored:
        que = input("Bored? (y/n) ")
        if que == "Y" or que == "y":
            print("Well, let's stop this, then.")
            break
        elif que == "N" or que == "n":
            continue
        else:
            print("Incorrect entry.")

main()



