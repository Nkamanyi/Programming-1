
import math

def area(a,b,c):
    """
    This function is used to calculate the area of a triangle
    a first side of the triangle
    b second side of the triangle
    c third side of the triangle
    """

    s = (a+b+c)/2

    area_triangle = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area_triangle

def main():
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))
    print(f"The triangle's area is {area(a,b,c):.1f}")

main()