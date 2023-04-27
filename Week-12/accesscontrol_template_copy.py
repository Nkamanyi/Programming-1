"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Project: accesscontrol, program template
"""

DOORCODES = {'TC114': ['TIE'], 'TC203': ['TIE'], 'TC210': ['TIE', 'TST'],
             'TD201': ['TST'], 'TE111': [], 'TE113': [], 'TE115': [],
             'TE117': [], 'TE102': ['TIE'], 'TD203': ['TST'], 'TA666': ['X'],
             'TC103': ['TIE', 'OPET', 'SGN'], 'TC205': ['TIE', 'OPET', 'ELT'],
             'TB109': ['OPET', 'TST'], 'TB111': ['OPET', 'TST'],
             'TB103': ['OPET'], 'TB104': ['OPET'], 'TB205': ['G'],
             'SM111': [], 'SM112': [], 'SM113': [], 'SM114': [],
             'S1': ['OPET'], 'S2': ['OPET'], 'S3': ['OPET'], 'S4': ['OPET'],
             'K1705': ['OPET'], 'SB100': ['G'], 'SB202': ['G'],
             'SM220': ['ELT'], 'SM221': ['ELT'], 'SM222': ['ELT'],
             'secret_corridor_from_building_T_to_building_F': ['X', 'Y', 'Z'],
             'TA': ['G'], 'TB': ['G'], 'SA': ['G'], 'KA': ['G']}


class Accesscard:
    """
    This class models an access card which can be used to check
    whether a card should open a particular door or not.
    """

    def __init__(self, id, name):
        """
        Constructor, creates a new object that has no access rights.

        :param id: str, card holders personal id
        :param name: str, card holders name

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME OR THE
        PARAMETERS!
        """

        # TODO: Implement the constructor
        self.__id = id
        self.__name = name
        self.__access_codes = []

    def info(self):
        """
        The method has no return value. It prints the information related to
        the access card in the format:
        id, name, access: a1,a2,...,aN
        for example:
        777, Thelma Teacher, access: OPET, TE113, TIE
        Note that the space characters after the commas and semicolon need to
        be as specified in the task description or the test fails.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE PRINTOUT FORMAT!
        """

        # TODO: Implement the method
        print(f"{self.__id}, {self.__name}, access: {self.access_codes_to_string()}")

    def get_name(self):
        """
        :return: Returns the name of the accesscard holder.
        """

        # TODO: Implement the method
        return self.__name

    def add_access(self, new_access_code):
        """
        The method adds a new accesscode into the accesscard according to the
        rules defined in the task description.

        :param new_access_code: str, the accesscode to be added in the card.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """

        # TODO: Implement the method
        if new_access_code in self.__access_codes:
            return
        if new_access_code in DOORCODES:  # is a door
            for area in DOORCODES[new_access_code]:
                if area in self.__access_codes:
                    return

        self.__access_codes.append(new_access_code)

        if new_access_code not in DOORCODES:  # is an areacode
            to_be_removed = []
            for code in self.__access_codes:
                if code in DOORCODES:  # is a door
                    for area in DOORCODES[code]:  # iterate through the doors areas..
                        if area in self.__access_codes:  # do we have the area already
                            to_be_removed.append(code)  # no need for this one
                            break  # no need to check more of this door

            # remove unnecessary codes
            for code in to_be_removed:
                self.__access_codes.remove(code)  # remove the code

    def check_access(self, door):
        """
        Checks if the accesscard allows access to a certain door.

        :param door: str, the doorcode of the door that is being accessed.
        :return: True: The door opens for this accesscard.
                 False: The door does not open for this accesscard.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """

        # TODO: Implement the method
        if door in self.__access_codes:
            return True
        for c in DOORCODES[door]:
            if c in self.__access_codes:
                return True

        return False

    def merge(self, card):
        """
        Merges the accesscodes from another accesscard to this accesscard.

        :param card: Accesscard, the accesscard whose access rights are added to this card.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """

        # TODO: Implement the method
        new_codes = card.get_access_codes()
        for code in new_codes:
            if code not in self.__access_codes:
                self.add_access(code)

    # additional methods
    def get_access_codes(self):
        """
        :return: Returns the access codes of the card holder
        """
        return self.__access_codes

    def access_codes_to_string(self):
        """
        :return: Returns the access codes of a card holder as a string
        """
        return ', '.join(sorted(self.__access_codes))


# TODO: Implement helper functions here.
def read_file(file_name):
    """
    Reading the file

    :param file_name:
    :return:
    """
    access_cards = {}   # for storing the access cards
    try:
        file = open(file_name, mode="r")

        for line in file:
            card_id, name, access_codes = line.rstrip().split(";")
            card = Accesscard(card_id, name)

            codes = access_codes.split(",")
            for c in codes:
                card.add_access(c)

            access_cards[card_id] = card

        file.close()
        return access_cards

    except OSError:
        print("Error: file cannot be read.")
        return


def is_valid_code(code):
    """
    Checks if the access code is in DOORCODES

    :param code: str, code to check
    :return: bool, true or false depending on the check
    """
    if code in DOORCODES:  # check for doorcode
        return True
    for areas in DOORCODES.values():  # check for areacodes
        if code in areas:
            return True

    return False  # not a doorcode, not an areacode..


def main():
    # TODO: Implement the reading of the inputfile and
    # storing the information into a data structure.
    access_cards = read_file(file_name="accessinfo.txt")

    while True:
        line = input("command> ")

        if line == "":
            break

        strings = line.split()
        command = strings[0]

        if command == "list" and len(strings) == 1:
            # TODO: Excecute the command list here
            for card in sorted(access_cards):
                access_cards[card].info()

        elif command == "info" and len(strings) == 2:
            card_id = strings[1]
            # TODO: Excecute the command info here
            if card_id in access_cards:
                access_cards[card_id].info()
            else:
                print("Error: unknown id.")

        elif command == "access" and len(strings) == 3:
            card_id = strings[1]
            door_id = strings[2]
            # TODO: Excecute the command access here
            if card_id in access_cards:
                if door_id not in DOORCODES:
                    print("Error: unknown doorcode.")
                else:
                    if access_cards[card_id].check_access(door_id):
                        print(f"Card {card_id} ( {access_cards[card_id].get_name()} ) has access to door {door_id}")
                    else:
                        print(f"Card {card_id} ( {access_cards[card_id].get_name()} ) has no access to door {door_id}")
            else:
                print("Error: unknown id.")

        elif command == "add" and len(strings) == 3:
            card_id = strings[1]
            access_code = strings[2]
            # TODO: Excecute the command add here
            if card_id in access_cards:
                if is_valid_code(access_code):
                    access_cards[card_id].add_access(access_code)
                else:
                    print("Error: unknown accesscode.")
            else:
                print("Error: unknown id.")

        elif command == "merge" and len(strings) == 3:
            card_id_to = strings[1]
            card_id_from = strings[2]
            # TODO: Excecute the command merge here
            if card_id_to in access_cards and card_id_from in access_cards:
                access_cards[card_id_to].merge(access_cards[card_id_from])
            else:
                print("Error: unknown id.")

        elif command == "quit":
            print("Bye!")
            return
        else:
            print("Error: unknown command.")


if __name__ == "__main__":
    main()
