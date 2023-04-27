"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name: Peter Kiplagat
Email: peter.kiplagat@tuni.fi
Student no: 441154
This program models a character adventuring in a video game.
"""


class Character:
    """
    This class defines what a character is in the game and what
    he or she can do.
    """

    # TODO: copy your Character class implementation from
    #       the previous assignment here and implement the
    #       following new methods.
    #
    #       Also note, that you have to modify at least
    #       __init__ and printout methods to conform with
    #       the new behaviour of the class.

    def __init__(self, name, hit_points):
        """
        Constructor

        :param name:str, name of the object
        """
        self.__name = name
        self.__weapons = {}
        self.__hit_points = hit_points

    def give_item(self, item):
        """
        Appends an item to the dict list values

        :param item: str, item being appended
        :return:
        """
        self.__weapons.setdefault(self.__name, []).append(item)

    def remove_item(self, item):
        """
        Removes an item from the dict value list

        :param item: str, item being removed
        :return:
        """
        self.__weapons[self.__name].remove(item)

    def printout(self):
        """
        For character printout

        :return:
        """
        items = []
        print(f"Name: {self.get_name()}")
        print("Hitpoints:", self.__hit_points)
        if len(self.__weapons.items()) < 1:
            print("  --nothing--")
            return
        for name in self.__weapons:
            if len(self.__weapons[name]) == 0:
                print("  --nothing--")
                return

            for item in sorted(self.__weapons[name]):
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
        for k in self.__weapons:
            for v in self.__weapons[k]:
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
        for k in self.__weapons:
            for v in self.__weapons[k]:
                if v == item:
                    count += 1

        return count

    def pass_item(self, item, target):
        """
        Passes (i.e. transfers) an item from one person (self)
        to another (target).

        :param item: str, the name of the item in self's inventory
                     to be given to target.
        :param target: Character, the target to whom the item is to
                     to be given.
        :return: True, if passing the item to target was successful.
                 False, it passing the item failed for any reason.
        """

        # TODO: implementation of the method
        if item in self.__weapons[self.__name]:
            target.__weapons.setdefault(target.get_name(), []).append(item)
            self.remove_item(item)
            return True

        return False

    def attack(self, target, weapon):
        """
        A character (self) attacks the target using a weapon.
        This method will also take care of all the printouts
        relevant to the attack.

        There are three error conditions:
          (1) weapon is unknown i.e. not a key in WEAPONS dict.
          (2) self does not have the weapon used in the attack
          (3) character tries to attack him/herself.
        You can find the error message to printed in each case
        from the example run in the assignment.

        The damage the target receives if the attack succeeds is
        defined by the weapon and can be found as the payload in
        the WEAPONS dict. It will be deducted from the target's
        hitpoints. If the target's hitpoints go down to zero or
        less, the target is defeated.

        The format of the message resulting from a successful attack and
        the defeat of the target can also be found in the assignment.

        :param target: Character, the target of the attack.
        :param weapon: str, the name of the weapon used in the attack
                       (must be exist as a key in the WEAPONS dict).
        :return: True, if attack succeeds.
                 False, if attack fails for any reason.
        """

        # TODO: the implementation of the method
        if weapon not in WEAPONS:
            print("Attack fails: unknown weapon", f'"{weapon}".')
            return
        elif weapon not in self.__weapons[self.__name]:
            print("Attack fails:", self.get_name(), "doesn't have", f'"{weapon}".')
            return
        elif self.get_name() == target.get_name():
            print(f"Attack fails: {self.get_name()} can't attack him/herself.")
            return
        else:
            print(f"{self.get_name()} attacks {target.get_name()} delivering {WEAPONS[weapon]} damage.")
            target.__hit_points -= WEAPONS[weapon]

        #Checks the winner
        if target.__hit_points <= 0:
            print(f"{self.get_name()} successfully defeats {target.get_name()}.")
            return


WEAPONS = {
    # Weapon          Damage
    #--------------   ------
    "elephant gun":     15,
    "gun":               5,
    "light saber":      50,
    "sword":             7,
}


def main():
    conan = Character("Conan the Barbarian", 10)
    deadpool = Character("Deadpool", 45)


    # Testing the pass_item method

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        conan.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        deadpool.give_item(test_item)

    conan.pass_item("sword", deadpool)
    deadpool.pass_item("hero outfit", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)

    print("-" * 5, "How are things after passing items around", "-" * 20)
    conan.printout()
    deadpool.printout()


    # Testing a fight i.e. the attack method

    print("-" * 5, "Let's see how a fight proceeds", "-" * 32)

    # Conan's turn
    conan.attack(deadpool, "sword") # Conan doesn't have a sword.
    conan.attack(conan, "gun")      # A character is not allowed to attack himself.
    conan.attack(conan, "pen")      # Pen is not a known weapon in WEAPONS dict.
    conan.attack(deadpool, "gun")   # Attack with a gun.

    # Deadpool retaliates
    deadpool.attack(conan, "sword") # Deadpool has a sword.

    # Conan's 2nd turn
    conan.attack(deadpool, "gun")   # Attack with a gun again.

    # Deadpool strikes back again and Conan drops "dead".
    deadpool.attack(conan, "sword")

    print("Are You Not Entertained?!")

    print("-" * 5, "How are things after beating each other up", "-" * 20)

    conan.printout()
    deadpool.printout()


if __name__ == "__main__":
    main()
