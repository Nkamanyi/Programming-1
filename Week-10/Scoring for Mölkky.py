
class Player:

    def __init__(self, name):

        self.__name = name
        self.__points = 0.0
        self.__counter = 0.0
        self.__total_points = 0.0
        self.__hit_score = 0.0

    def get_name(self):

        return self.__name



    def get_points(self):

        return self.__points



    def has_won(self):

        if self.__points == 50:
            return True
        return False

    def add_points(self, points):

        self.__points += points

        if self.__points > 50:
            print(f"{self.get_name()} gets penalty points!")
            self.__points = round(self.__points / 2) - 1
            self.__total_points += points
        elif self.__points == 50:
            self.has_won()
        else:
            self.__total_points += points

        if points > 0:
            self.__hit_score += 1
        self.success_rate()

        self.printout()
        self.__counter += 1

    def printout(self):

        if 40 <= self.get_points() <= 49:
            print(f"{self.get_name()} needs only {50 - self.get_points():.0f} points. "
                  f"It's better to avoid knocking down the pins with higher points.")

    def average_scores(self):

        if self.__total_points > 0:
            return self.__total_points/self.__counter
        return 0.0

    def success_rate(self):

        if self.__counter == 0:
            return 0

        return self.__hit_score/self.__counter * 100


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        # TODO:
        # c) Add a supporting feedback printout "Cheers NAME!" here.
        if pts > in_turn.average_scores():
            print(f"Cheers {in_turn.get_name()}!")

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", f"{player1.get_points():.0f} p,", "hit percentage", f"{player1.success_rate():.1f}")  # TODO: d)
        print(player2.get_name() + ":", f"{player2.get_points():.0f} p,", "hit percentage", f"{player2.success_rate():.1f}")  # TODO: d)
        print("")

        throw += 1

main()