"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name: Nkamanyi Martin Asungu Chatutie
Email: Chatutie.Nkamanyimartin@tuni.fi
Student no: K440302

Project: Level Changes in Seawater

This program calculates characteristic values based on sea water level measurements.
It prompts the user to enter sea water levels in centimeters, calculates and prints
the minimum, maximum, median, mean, and standard deviation of the measurements.
"""

import math

def get_measurements():
    """
    Prompts the user to enter sea water levels in centimeters and returns a list of
    the entered measurements. Continues prompting until the user enters an empty line.
    """
    measurements = []
    while True:
        level = input()
        if level == "":
            break

        try:
            measurements.append(float(level))
        except ValueError:
            print("Error: Invalid input. Enter only numbers.")
            measurements = []
            break

    return measurements

def calculate_minimum(measurements):
    """
    Returns the smallest measurement from the list of measurements.
    """
    return min(measurements)

def calculate_maximum(measurements):
    """
    Returns the largest measurement from the list of measurements.
    """
    return max(measurements)

def calculate_median(measurements):
    """
    Returns the median measurement from the list of measurements.
    """
    sorted_measurements = sorted(measurements)
    length = len(sorted_measurements)
    if length % 2 == 0:
        return (sorted_measurements[length // 2 - 1] + sorted_measurements[length // 2]) / 2
    else:
        return sorted_measurements[length // 2]

def calculate_mean(measurements):
    """
    Returns the mean of the measurements from the list of measurements.
    """
    return sum(measurements) / len(measurements)

def calculate_deviation(measurements):
    """
    Returns the standard deviation of the measurements from the list of measurements.
    """
    mean = calculate_mean(measurements)
    deviation_sum = sum([(x - mean)**2 for x in measurements])
    return math.sqrt(deviation_sum / (len(measurements)-1))

def main():
    """
    Main function that gets the measurements from the user, calculates the characteristic
    values, and prints them to the screen.
    """
    print("Enter seawater levels in centimeters one per line.")
    print("End by entering an empty line.")
    measurements = get_measurements()

    if len(measurements) < 2:
        print("Error: At least two measurements must be entered!")
        return
    print("Minimum:   {:.2f} cm".format(calculate_minimum(measurements)))
    print("Maximum:   {:.2f} cm".format(calculate_maximum(measurements)))
    print("Median:    {:.2f} cm".format(calculate_median(measurements)))
    print("Mean:      {:.2f} cm".format(calculate_mean(measurements)))
    print("Deviation: {:.2f} cm".format(calculate_deviation(measurements)))

main()
