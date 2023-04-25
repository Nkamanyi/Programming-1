
def main():
    sche = [630,1015,1415,1620,1720,2000]
    time_now = int(input("Enter the time (as an integer): "))
    print("The next buses leave:")
    bus_list = []
    for x in sche:
        if x >= time_now:
            bus_list.append(x)
    if len(bus_list) >= 3:
        for i in bus_list[:3]:
            print(i)
    elif len(bus_list) >= 2:
        for x in bus_list[:2]:
            print(x)
        print(sche[0])
    elif len(bus_list) >= 1:
        for y in bus_list[:1]:
            print(y)
        print(sche[0])
        print(sche[1])
    elif len(bus_list) >= 0:
        for w in sche[:3]:
            print(w)

main()
