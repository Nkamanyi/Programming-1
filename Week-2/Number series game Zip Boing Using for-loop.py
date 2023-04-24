
def main():
    num = int(input("How many numbers would you like to have? "))
    for c in range(1,num+1):
        if c%3 == 0 and c%7 == 0:
            print("zip boing")
        elif c%3 ==0:
            print("zip")
        elif c%7 == 0:
            print("boing")
        else:
            print(c)
main()