
def main():
    a = 1
    b = int(input("Choose a number: "))
    c = True
    while c:
        print(f"{a} * {b} = {a * b}")
        a += 1
        if a*b >= 100+b:
            c = False

main()