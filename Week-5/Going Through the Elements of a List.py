
def main():
    list = []
    i = 1
    print("Give 5 numbers:")
    while i < 6:
        num = int(input("Next number: "))
        list.append(num)
        i+=1

    print("The numbers you entered that were greater than zero were:")
    for n in list:
        if n > 0:
            print(n)

main()