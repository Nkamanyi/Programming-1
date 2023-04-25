
def main():
    print("Game of sticks")

    total_sticks = 21
    sticks_picked = 0

    while sticks_picked < total_sticks: # Main loop: Checks that there are still sticks to pick
        # Loop 1 for checking player 1
        while True:
            player_1_sticks = int(input("Player 1 enter how many sticks to remove: "))
            if player_1_sticks == 1 or player_1_sticks == 2 or player_1_sticks == 3:
                sticks_picked += player_1_sticks
                sticks_remaining = total_sticks - sticks_picked
                if sticks_remaining > 0:
                    print(f"There are {sticks_remaining} sticks left")

                    # Loop 2 for checking player 2
                    while True:
                        player_2_sticks = int(input("Player 2 enter how many sticks to remove: "))
                        if player_2_sticks == 1 or player_2_sticks == 2 or player_2_sticks == 3:
                            sticks_picked += player_2_sticks
                            sticks_remaining = total_sticks - sticks_picked
                            if sticks_remaining > 0:
                                print(f"There are {sticks_remaining} sticks left")
                                break
                            else:
                                print("Player 2 lost the game!")
                                break
                        else:
                            print("Must remove between 1-3 sticks!")
                            continue
                    break

                else:
                    print("Player 1 lost the game!")
                    break
            else:
                print("Must remove between 1-3 sticks!")
                continue
main()

