
def main():
    f = range(1, 29)
    j = range(1, 32)
    n = range(1, 31)

    for i in range(1, 13):
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            for x in j:
                print(f"{x}.{i}.")
        if i == 4 or i == 6 or i == 9 or i == 11:
            for y in n:
                print(f"{y}.{i}.")
        if i == 2:
            for z in f:
                print(f"{z}.{i}.")
main()