
def main():
    list = []
    i = 1
    print("Give 5 numbers:")
    while i < 6:
        num = int(input("Next number: "))
        list.append(num)
        i+=1
    print("The numbers you entered, in reverse order:")
    for n in list[::-1]:
        print(n)

main()


