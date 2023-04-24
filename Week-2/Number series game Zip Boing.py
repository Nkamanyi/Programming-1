
def main():
    num = int(input("How many numbers would you like to have? "))
    c = 1
    while c <= num:

        if c%3 == 0 and c%7 == 0:
            print("zip boing")
        elif c%3 ==0:
            print("zip")
        elif c%7 == 0:
            print("boing")
        else:
            print(c)

        c+=1
main()