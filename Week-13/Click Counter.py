
from tkinter import *


class Counter:
    def __init__(self):
        # TODO: You have to create one label and four buttons and store
        #       them in the following attributes:
        #
        #       self.__current_value_label  # Label displaying the current value of the counter.
        #       self.__reset_button         # Button which resets counter to zero.
        #       self.__increase_button      # Button which increases the value of the counter by one.
        #       self.__decrease_button      # Button which decreases the value of the counter by one.
        #       self.__quit_button          # Button which quits the program.
        #
        #       Make sure you name the components exactly as shown above,
        #       otherwise the automated tests will fail.

        self.__main_window = Tk()
        self.__counter = 0

        self.__current_value_label = Label(self.__main_window, text ="0", borderwidth=2)
        self.__current_value_label.grid(row=0,column=0,columnspan=4,sticky=W+E)

        self.__reset_button = Button(self.__main_window, text="Reset", borderwidth=2, command=self.reset)
        self.__reset_button.grid(row=1,column=0)

        self.__increase_button = Button(self.__main_window, text="Increase", command=self.increase)
        self.__increase_button.grid(row=1, column=1)

        self.__decrease_button = Button(self.__main_window, text="Decrease", command=self.decrease)
        self.__decrease_button.grid(row=1, column=2)

        self.__quit_button = Button(self.__main_window, text="Quit", command=self.quit)
        self.__quit_button.grid(row=1, column=3)

        self.__main_window.mainloop()


    # TODO: Implement the rest of the needed methods here.

    def reset(self):
        """
        Resets the counter to zero(0).
        :return:
        """
        self.__counter = 0
        self.__current_value_label.configure(text=self.__counter)

    def increase(self):
        """
        The value of the counter increase by one.
        :return:
        """
        self.__counter += 1
        self.__current_value_label.configure(text=self.__counter)

    def decrease(self):
        """
        The value of the counter decrease by one.
        :return:
        """
        self.__counter -= 1
        self.__current_value_label.configure(text=self.__counter)

    def quit(self):
        """
        Quits the program.
        :return:
        """
        self.__main_window.destroy()


def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()

main()
