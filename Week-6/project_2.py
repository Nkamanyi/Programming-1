
def input_data():
    """
    Here the user is demanded for energy consumption and the program ends with a whitespace.

    :return: list, whose values are energy consumption from the user.
    """
    energy_consumption = []
    while True:
        energy_value = input("Enter energy consumption (kWh): ")
        if energy_value == "":
            break
        energy_value = int(energy_value)
        if energy_value < 0:
            print(f"You entered: {energy_value}. Enter non-negative numbers only!")
            continue
        else:
            energy_consumption.append(energy_value)
            continue

    return energy_consumption



def class_minimum_value(class_number):
    """
    Given a specific class, it calculates and return its smallest value

    :param class_number: the given class
    :return: int, the smallest value in that class
    """
    smallest_value = 10 ** class_number // 100 * 10

    return smallest_value


def class_maximum_value(class_number):
    """
    Given a specific class, it calculates and return its largest value

    :param class_number: the given class
    :return: int, the largest value in that class
    """
    largest_value = 10 ** class_number - 1
    return largest_value



def largest_class_number(energy_consumption):
    """
    Given a list, the function calculate and returns the largest value

    :param energy_consumption:list, data from the user
    :return: int, the largest value from the list
    """
    data = energy_consumption
    data.sort()
    largest_num = data[len(data)-1]
    count = 0
    while largest_num > 0:
        count = count + 1
        largest_num = largest_num // 10

    return count



def num_of_value_in_class_estimator(energy_consumption):
    """
    Calculates the number of values belonging to each class and stores it in a list

    :param energy_consumption: list, energy data from the user
    :return: list, containing the number of values of each class
    """
    largest_class_value = largest_class_number(energy_consumption)
    category_list = [0] * (largest_class_value + 1)

    class_number = 0
    while class_number <= largest_class_value:
        counter = 0
        for energy_value in energy_consumption:
            if class_minimum_value(class_number) <= energy_value <= class_maximum_value(class_number):
                counter += 1
        category_list.append(counter)
        class_number += 1

    return category_list



def print_histogram():
    """
    Produces a histogram from the energy consumption data given by the user

    :return: histogram
    """
    energy_consumption = input_data()

    if len(energy_consumption) > 1:
        category_list = num_of_value_in_class_estimator(energy_consumption)
        largest_class_value = largest_class_number(energy_consumption)

        class_number = 1
        del category_list[0:largest_class_value+1]
        #print(category_list)
        while class_number <= largest_class_value:
            count = category_list[class_number]
            print_single_histogram_line(class_number, count, largest_class_value)
            class_number += 1
    else:
        print("Nothing to print. Done.")



def main():
    print("Enter energy consumption data.")
    print("End by entering an empty line.")
    print()

    # Test values for the input data, so they don't have to be manually
    # entered every single time you want to test your program.  Before
    # submitting your program to Plussa these must be replaced by values
    # read from the user, otherwise the tests will fail.

    print_histogram()


def print_single_histogram_line(class_number, count, largest_class_number):
    """
    This function is probably the most challenging one in this assignment.
    It will print one correctly indented histogram line as described
    in the assignment instructions. Your job is to call it with
    correct parameters.

    :param class_number: int,
        Expresses which consumption class (1, 2, 3, ...)
        should the histogram line be printed for. The <class_number> is used
        to decide which value range (0-9, 10-99, 100-999, ...) should be
        printed in front of the histogram markers ("*").

    :param count: int,
        How many of the values entered by the user belong to <class_number>.

    :param largest_class_number: int,
        What is the largest class out of all input values
        the user entered. This is needed when deciding the indentations
        for all other histogram lines.  For example, if the largest
        number the user entered was 91827364 (8 digits) the value
        of this paramter should be 8.
    """

    # <range_string> represents the range of the values the line's
    # histogram will represent in the printout.  For example "1000-9999".
    # Uses the functions class_minimum_value and class_maximum_value which
    # have to be defined elsewhere.

    min_value = class_minimum_value(class_number)
    max_value = class_maximum_value(class_number)
    range_string = f"{min_value}-{max_value}"

    # How many characters will the largest class' range need when printed.
    # For example if the <largest_class_number> is 7, it would print
    # "1000000-9999999" in the beginning of the line and requires 15 characters.
    # This value defines the print width for all the other <range_string>'s.

    largest_width = 2 * largest_class_number + 1

    # Now all the preparations have been done and we can print the
    # histogram line with the correct number of whitespaces in the
    # beginning of the line followed by the correct number of '*'
    # characters. ">" character in the following f-string places
    # <range_string>'s value to the right edge of the output field
    # (filler white spaces will be printed in the beginning).

    print(f"{range_string:>{largest_width}}: {'*' * count}")


if __name__ == "__main__":
    main()
