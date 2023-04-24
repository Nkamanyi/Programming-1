
def main():
    bored = True
    while bored:
        question = input("Bored? (y/n) ")
        if question == "y":
            bored = False
            print("Well, let's stop this, then.")

main()