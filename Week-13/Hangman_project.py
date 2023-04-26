"""
Game implementation:

- The GUI gives the user a hint of the search word.
- The user then interact with the program by entry characters using the keyboard.
- Everytime the user makes a bad choice, a hanger is built.
- Everytime the user guess right, the character is displaced on the screen.
- If the user fail to guess the correct word after the trial counts, he/she is hanged.
- Other than that the user wins and gets.
"""

from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random


COUNTRIES = ["TANZANIA", "LIBYA", "CONGO", "KENYA", "LIBERIA", "MOROCCO", "CAMEROON", "NAMIBIA", "BOTSWANA",
         "NIGERIA", "SOMALIA", "ZIMBABWE", "GUINEA", "BURUNDI", "ETHIOPIA"]
COMPONENTS = ["comp0.png", "comp1.png", "comp2.png", "comp3.png", "comp4.png", "comp5.png", "comp6.png", "comp7.png",
          "comp8.png", "comp9.png"]


class Hangman:
    def __init__(self):
        self.__main_window = Tk()
        self.__main_window.title(f"Welcome to the Hangman game")
        self.__main_window.option_add("*Font", "Helvetica 15 bold")
        self.__guess_count= 0
        self.__guess_country = self.pick_country()
        self.__guessed_characters = [" _ "] * len(self.__guess_country)

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # hangman component parts
        self.__hang_comp = PhotoImage(file=COMPONENTS[self.__guess_count])
        self.__comp_label = Label(self.__main_window, image=self.__hang_comp)
        self.__comp_label.grid(row=0, column=0)

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # this here give the user a clue of the guess word
        self.__clue_label = Label(self.__main_window, text=f"Guess a country in Africa with {len(self.__guess_country)} letters")
        self.__clue_label.grid(row=0, column=3)

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # this help display the country on the window
        self.__country_label = Label(self.__main_window, text=self.__guessed_characters)
        self.__country_label.grid(row=1, column=3, sticky=N)

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # this creates the GUI keyboard
        n = 0
        for char in ascii_uppercase:
            Button(self.__main_window, text=char, command=lambda char=char: self.keyboard(char),
                   font="Helvetica 15", width=4).grid(row=2 + n//9, column=n % 9)
            n += 1
        self.__restart_button = Button(self.__main_window, text="RESTART", command=self.restart)
        self.__restart_button.grid(row=5, column=0)
        self.__give_up_button = Button(self.__main_window, text="GIVE UP", command=self.give_up)
        self.__give_up_button.grid(row=5, column=8)

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        self.__main_window.mainloop()

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    def pick_country(self):
        """
        picks randomly a country from the list of COUNTRIES

        :return:
        """
        return random.choice(COUNTRIES)

    def update_country(self):
        """
        Updates the country that is sent to the screen

        :return:
        """
        self.__country_label.configure(text=self.__guessed_characters)

    def keyboard(self, character):
        """
         - Allows the user to interact with the program. It takes a character and check if its withtin the guess country.
         - In the case where the character is present in the country, it displays it in the right position of the 'country'.
         - Otherwise a hanger is built a step forward.
         - If the user guess the country with the guess count, the user wins otherwisw he is hanged.

        :param character: char, the character input using the keyboard
        :return:
        """
        indices = self.get_index(character)

        if list(self.__guessed_characters) == list(self.__guess_country):
            messagebox.showinfo(f"You won! Correct country is:{self.__guess_country}")
            return

        if self.__guess_count == 9:
            messagebox.showinfo(f"You've been hanged, Correct country was: {self.__guess_country}")
            return

        if character in self.__guess_country:
            for i in range(len(indices)):
                self.__guessed_characters[indices[i]] = character
            self.update_country()
        else:
            self.__guess_count += 1
            self.__hang_comp = PhotoImage(file=COMPONENTS[self.__guess_count])
            self.__comp_label.configure(image=self.__hang_comp)

    def get_index(self, character):
        """
        Returns the positions of the characters in th 'country' word.

        :param character: char, the input character
        :return: list, of the country's index positions
        """

        indices = [i for i, val in enumerate(self.__guess_country) if val == character]
        return indices

    def restart(self):
        """
        Restarts the game

        :return:
        """
        self.__guess_country = self.pick_country()
        self.__guessed_characters = [" _ "] * len(self.__guess_country)
        self.__guess_count = 0
        self.__hang_comp = PhotoImage(file=COMPONENTS[self.__guess_count])
        self.__clue_label.config(text=f"Guess a country in Africa with {len(self.__guess_country)} letters")
        self.__country_label.config(text=self.__guessed_characters)

    def give_up(self):
        """
        Ends the game

        :return:
        """
        self.__main_window.destroy()


def main():
    Hangman()

main()