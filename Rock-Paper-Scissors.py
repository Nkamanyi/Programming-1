
def main():
    player_1 = input("Player 1, enter your choice (R/P/S): ")
    player_2 = input("Player 2, enter your choice (R/P/S): ")

    if player_1 == "P" and player_2 == "S":
        print("Player 2 won!")
    elif player_1 == "P" and player_2 == "R":
        print("Player 1 won!")
    elif player_1 == "R" and player_2 == "S":
        print("Player 1 won!")
    elif player_1 == "S" and player_2 == "P":
        print("Player 1 won!")
    elif player_1 == "R" and player_2 == "P":
        print("Player 2 won!")
    elif player_1 == "S" and player_2 == "R":
        print("Player 2 won!")
    else:
        print("It's a tie!")

main()