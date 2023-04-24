
def main():
    num = int(input("How many Fibonacci numbers do you want? "))
    a = 1
    b = 0
    sum = 1
    count = 1
    for i in range(1, num + 1):
        while count <= num:
            print(f"{i}. {sum}")
            count +=1
            a = b
            b = sum
            sum = a+b
            i+=1

main()