
def main():
    feel = int(input("How do you feel? (1-10) "))
    if feel == 1:
        print("A suitable smiley would be :'(")
    elif feel >= 2 and feel <= 3:
        print("A suitable smiley would be :-(")
    elif feel >= 4 and feel <= 7:
        print("A suitable smiley would be :-|")
    elif feel >= 8 and feel <= 9:
        print("A suitable smiley would be :-)")
    elif feel == 10:
        print("A suitable smiley would be :-D")
    else:
        print("Bad input!")
main()


