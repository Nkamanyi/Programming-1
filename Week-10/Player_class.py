unknown_position = None

class Player:
    def __init__(self, name):

        self.__name = name
        self.__position = unknown_position

    def printout(self):
        print("-" * 25)
        print("Name: ", self.__name)
        print("position: ", self.__position)

    def set_player_position(self, position):
        if position <= 0:
            raise ValueError("Player position must be greater than 0.")
        else:
            self.__position = position
def main():
    john = Player("John")
    john.printout()
    print()
    john.set_player_position(9)
    john.printout()

main()