
def main():
    list = []

    num = 1
    while num <= 5:
        list.append(float(input(f"Enter the time for performance {num}: ")))
        num +=1
    list.pop(0)
    list.pop(-1)
    average = sum(list)/len(list)
    print(f"The official competition score is {average:.2f} seconds.")

main()