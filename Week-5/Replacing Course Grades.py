
def convert_grades(grades):
    """
    :param grades: students grades
    :return: converting any student grade greater 0 to be 6
    """
    length_of_list = len(grades)
    for k in range(0,length_of_list):
        if grades[k] == 0:
            grades[k] = 0
        elif len(grades) == 0:
            pass
        else:
            grades[k]=6


def main():
    grades = [3]
    convert_grades(grades)
    #print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]

main()