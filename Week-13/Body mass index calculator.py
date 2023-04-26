
from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()

        # TODO: Create an Entry-component for the weight.
        self.__weight_label = Label(self.__mainwindow, text="Enter weight in Kg")
        self.__weight_label.pack()
        self.__weight_value = Entry()
        self.__weight_value.pack()



        # TODO: Create an Entry-component for the height.
        self.__height_label = Label(self.__mainwindow, text="Enter height in Cm")
        self.__height_label.pack()
        self.__height_value = Entry()
        self.__height_value.pack()


        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        #       the default colour.
        self.__calculate_button = Button(self.__mainwindow, text="BMI", command=self.calculate_BMI, background="green", foreground="red")
        self.__calculate_button.pack()


        # TODO: Create a Label that will show the decimal value of the BMI
        #      after it has been calculated.
        self.__result_text_label = Label(self.__mainwindow, text="Result")
        self.__result_text_label.pack()
        self.__result_text = Label(self.__mainwindow, text="")
        self.__result_text.pack()

        # TODO: Create a Label that will show a verbal description of the BMI
        #       after the BMI has been calculated.
        self.__explanation_text = Label(self.__mainwindow, text="BMI calculated")
        self.__explanation_text.pack()


        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow, text="Stop", command=self.stop)
        self.__stop_button.pack()


        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!
        # self.__weight_value.grid()
        # self.__height_value.grid()
        # self.__calculate_button.grid()
        # self.__stop_button.grid()
        # self.__result_text.grid()
        # self.__explanation_text.grid()

    # TODO: Implement this method.
    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """

        value_of_weight = self.__weight_value.get()
        value_of_height = self.__height_value.get()

        try:
            value_of_weight = float(value_of_weight)
            value_of_height = float(value_of_height)

            if value_of_weight <= 0 or value_of_height <= 0:
                self.__explanation_text.configure(text=f"Error: height and weight must be positive.")
                self.reset_fields()
                return

            result = value_of_weight / (value_of_height / 100 * value_of_height / 100)
            self.__result_text.configure(text=f"{result:.2f}")

            if 18.5 <= result <= 25:
                self.__explanation_text.configure(text=f"Your weight is normal.")
            elif result > 25:
                self.__explanation_text.configure(text=f"You are overweight.")
            else:
                self.__explanation_text.configure(text=f"You are underweight.")

        except ValueError:
            self.__explanation_text.configure(text="Error: height and weight must be numbers.")
            self.reset_fields()
            return



    # TODO: Implement this method.
    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """

        self.__weight_value.configure(text="")
        self.__height_value.configure(text="")
        self.__result_text.configure(text="")



    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()

main()
