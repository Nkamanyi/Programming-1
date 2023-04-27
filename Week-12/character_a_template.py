"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name: Peter Kiplagat
Student no: 441154
Email: peter.kiplagat@tuni.fi

This program models a character adventuring in a video game,
or more like, the stuff that the character carries around.
"""


class Character:
    # TODO: the class implementation goes here.
    def __init__(self, name):
        """
        Constructor

        :param name:str, name of the object
        """
        self.__name = name
        self.__character = {}

    def give_item(self, item):
        """
        Appends an item to the dict list values

        :param item: str, item being appended
        :return:
        """
        self.__character.setdefault(self.__name, []).append(item)

    def remove_item(self, item):
        """
        Removes an item from the dict value list

        :param item: str, item being removed
        :return:
        """
        self.__character[self.__name].remove(item)

    def printout(self):
        """
        For character printout

        :return:
        """
        print(f"Name: {self.get_name()}")
        items = []
        if len(self.__character.items()) < 1:
            print("  --nothing--")
            return
        for name in self.__character:
            if len(self.__character[name]) == 0:
                print("  --nothing--")
                return

            for item in sorted(self.__character[name]):
                if item not in items:
                    items.append(item)

        for i in sorted(items):
            print(f"  {self.how_many(i)} {i}")

    def get_name(self):
        """
        Returns the name of the object
        :return: str, name of object
        """
        return self.__name

    def has_item(self, item):
        """
        Checks if an item is included in the list values of the dict

        :param item: str, item being searched
        :return: bool, true or false if item is found
        """
        for k in self.__character:
            for v in self.__character[k]:
                if v == item:
                    return True
        return False

    def how_many(self, item):
        """
        Counts the number of 'item' from the list values of the dict

        :param item: str, item being checked/counted
        :return: int, the count of the item in question
        """
        count = 0
        for k in self.__character:
            for v in self.__character[k]:
                if v == item:
                    count += 1

        return count


def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
