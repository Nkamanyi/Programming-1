
EPSILON = 0.000000001

def compare_floats(a,b,EPSILON):
    """This function compare_floats that uses two floating point
    numbers and an epsilon as a parameter and returns information
    on whether the numbers are same to a sufficient degree
    (the parameter epsilon) as a truth value
    """
    res = abs(a-b) < EPSILON
    return res


def main():
    a = float(input("Enter the first floating number: "))
    b = float(input("Enter the second floating number: "))

    print(compare_floats(a,b,EPSILON))

main()
