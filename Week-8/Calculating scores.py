
def main():
    dict = {}
    filename = input("Enter the name of the score file: ")
    with open(filename, 'r') as f_in:
        for line in map(str.strip, f_in):
            if not line:
                continue
            name, cnt = line.split()
            if name not in dict:
                dict[name] = int(cnt)
            else:
                dict[name] += int(cnt)

    print("Contestant score:")
    for name in sorted(dict):
        print(name, dict[name])

    f_in.close()

main()