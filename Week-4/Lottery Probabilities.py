
import math

def probability_of_guessing(total_balls,drawn_balls):
    """
    :param total_balls: the total number of lottery balls
    :param drawn_balls: the number of balls to be drawn
    :return: the number of different lottery lines existing in total

    """
    result = math.factorial(total_balls)/(math.factorial(total_balls-drawn_balls)*math.factorial(drawn_balls))
    return result
def lottery_balls(total_balls,drawn_balls):
    """

    :param total_balls: the total number of lottery balls
    :param drawn_balls: the number of balls to be drawn
    :return: conditional result
    """
    if total_balls < 1:
        print("The number of balls must be a positive number.")
    elif drawn_balls > total_balls:
        print("At most the total number of balls can be drawn.")
    else:
        prob = probability_of_guessing(total_balls, drawn_balls)
        print(f"The probability of guessing all {drawn_balls} balls correctly is 1/{prob:.0f}")
def main():
    total_balls = int(input("Enter the total number of lottery balls: "))
    drawn_balls = int(input("Enter the number of the drawn balls: "))
    lottery_balls(total_balls,drawn_balls)

main()