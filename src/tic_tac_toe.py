# Tic-Tac-Toe Game in Python.
# <--Developed by James George--> #

from tkinter import Tk, messagebox, Button, Label

import random

class Game:

    # The initializer / constructor method which is being invoked on instantiation.

    def __init__(self, master):

        master.title('Tic Tac Toe')

        master.geometry('985x700')

        master.resizable(True, True)
        master.config(bg='skyblue')

        messagebox.showinfo("WELCOME", "Welcome to the Tic tac Toe Game!!")

        ''' Boolean values to keep track whether a button was already clicked or not implemented as a list.
         Initialilzing the list elements to False since the buttons are not clicked. '''

        self.button_clicked_list = [False]*9

        # Creating instances of the Button class which would act as buttons .

        self.result = Label(text="Tic Tac Toe Game", font="algerian 65 bold underline", fg="darkred", bg='skyblue')
        self.result.grid(row=0, column=0, columnspan=3)

        self.button_one = Button(text="", font="times 65 bold", fg="black", bg="green", width="6", bd=5, relief='solid', command=self.button_one_clicked)
        self.button_one.grid(row=1, column=0)

        self.button_two = Button(text="", font="times 65 bold", fg="black", bg="green", width="6", bd=5, relief='solid', command=self.button_two_clicked)
        self.button_two.grid(row=1, column=1)

        self.button_three = Button(text="", font="times 65 bold", fg="black", bg="green", width="6", bd=5, relief='solid', command=self.button_three_clicked)
        self.button_three.grid(row=1, column=2)

        self.button_four = Button(text="", font="times 65 bold", fg="black", bg="green", width="6", bd=5, relief='solid', command=self.button_four_clicked)
        self.button_four.grid(row=2, column=0)

        self.button_five = Button(text="", font="times 65 bold", fg="black", bg="green", width="6", bd=5, relief='solid', command=self.button_five_clicked)
        self.button_five.grid(row=2, column=1)

        self.button_six = Button(text="", font="times 65 bold", fg="black", bg="green", width="6", bd=5, relief='solid', command=self.button_six_clicked)
        self.button_six.grid(row=2, column=2)

        self.button_seven = Button(text="", font="times 65 bold", fg="black", bg="green", width="6", bd=5, relief='solid', command=self.button_seven_clicked)
        self.button_seven.grid(row=3, column=0)

        self.button_eight = Button(text="", font="times 65 bold", fg="black", bg="green", width="6", bd=5, relief='solid', command=self.button_eight_clicked)
        self.button_eight.grid(row=3, column=1)

        self.button_nine = Button(text="", font="times 65 bold", fg="black", bg="green", width="6", bd=5, relief='solid', command=self.button_nine_clicked)
        self.button_nine.grid(row=3, column=2)

        self.button_reset = Button(text="Reset", font="algerian 45 bold underline", fg="darkred", bg='skyblue', command=self.button_reset_clicked)
        self.button_reset.grid(row=4, column=0, columnspan=3)

        # List of all the buttons.

        self.buttons_list = [self.button_one, self.button_two, self.button_three, self.button_four, self.button_five, self.button_six, self.button_seven, self.button_eight, self.button_nine]

    def button_reset_clicked(self):

        # This function will clear the board of all piece and allow for another game to be played

        n = len(self.button_clicked_list)

        for b in range(0, n):
            self.button_clicked_list[b] = False

        for x in self.buttons_list:
            x.config(text="", bg='green', fg='black')

        return

    def button_one_clicked(self):

        if not self.button_clicked_list[0]:

            # clicked the button in the GUI

            self.button_one.config(text="X", bg='darkred', fg='green')

            self.button_clicked_list[0] = True

            # Checks if the board is filled before trying to find a random number

            i = 0

            for x in self.button_clicked_list:
                if not x:
                    i += 1

            if i == 0:
                return

            # Gets a random number and checks to make sure that it hasn't been clicked already

            random_button = random.randint(0, len(self.buttons_list) - 1)

            while random_button == 0 or self.button_clicked_list[random_button]:

                random_button = random.randint(0, len(self.buttons_list) - 1)

            # uses the random number created place a token of 'O' on the board

            self.buttons_list[random_button].config(text="O", bg='lightgreen', fg='darkblue')

            # Updates the button clicked list with the two new buttons

            self.button_clicked_list[random_button] = True

        else:

            messagebox.showwarning("Warning", "Button One was already clicked!")
            return

    def button_two_clicked(self):

        if not self.button_clicked_list[1]:

            # clicked the button in the GUI

            self.button_two.config(text="X", bg='darkred', fg='green')

            self.button_clicked_list[1] = True

            # Checks if the board is filled before trying to find a random number

            i = 0

            for x in self.button_clicked_list:
                if not x:
                    i += 1

            if i == 0:
                return

            # Gets a random number and checks to make sure that it hasn't been clicked already

            random_button = random.randint(0, len(self.buttons_list) - 1)

            while random_button == 1 or self.button_clicked_list[random_button]:

                random_button = random.randint(0, len(self.buttons_list) - 1)

            # uses the random number created place a token of 'O' on the board

            self.buttons_list[random_button].config(text="O", bg='lightgreen', fg='darkblue')

            # Updates the button clicked list with the two new buttons

            self.button_clicked_list[random_button] = True

        else:

            messagebox.showwarning("Warning", "Button Two was already clicked!")
            return

    def button_three_clicked(self):

        if not self.button_clicked_list[2]:

            # clicked the button in the GUI

            self.button_three.config(text="X", bg='darkred', fg='green')

            self.button_clicked_list[2] = True

            # Checks if the board is filled before trying to find a random number

            i = 0

            for x in self.button_clicked_list:
                if not x:
                    i += 1

            if i == 0:
                return

            # Gets a random number and checks to make sure that it hasn't been clicked already

            random_button = random.randint(0, len(self.buttons_list) - 1)

            while random_button == 2 or self.button_clicked_list[random_button]:

                random_button = random.randint(0, len(self.buttons_list) - 1)

            # uses the random number created place a token of 'O' on the board

            self.buttons_list[random_button].config(text="O", bg='lightgreen', fg='darkblue')

            # Updates the button clicked list with the two new buttons

            self.button_clicked_list[random_button] = True

        else:

            messagebox.showwarning("Warning", "Button Three was already clicked!")
            return

    def button_four_clicked(self):

        if not self.button_clicked_list[3]:

            # clicked the button in the GUI

            self.button_four.config(text="X", bg='darkred', fg='green')

            self.button_clicked_list[3] = True

            # Checks if the board is filled before trying to find a random number

            i = 0

            for x in self.button_clicked_list:
                if not x:
                    i += 1

            if i == 0:
                return

            # Gets a random number and checks to make sure that it hasn't been clicked already

            random_button = random.randint(0, len(self.buttons_list) - 1)

            while random_button == 3 or self.button_clicked_list[random_button]:

                random_button = random.randint(0, len(self.buttons_list) - 1)

            # uses the random number created place a token of 'O' on the board

            self.buttons_list[random_button].config(text="O", bg='lightgreen', fg='darkblue')

            # Updates the button clicked list with the two new buttons

            self.button_clicked_list[random_button] = True

        else:

            messagebox.showwarning("Warning", "Button Four was already clicked!")
            return

    def button_five_clicked(self):

        if not self.button_clicked_list[4]:

            # clicked the button in the GUI

            self.button_five.config(text="X", bg='darkred', fg='green')

            self.button_clicked_list[4] = True

            # Checks if the board is filled before trying to find a random number

            i = 0

            for x in self.button_clicked_list:
                if not x:
                    i += 1

            if i == 0:
                return

            # Gets a random number and checks to make sure that it hasn't been clicked already

            random_button = random.randint(0, len(self.buttons_list) - 1)

            while random_button == 4 or self.button_clicked_list[random_button]:

                random_button = random.randint(0, len(self.buttons_list) - 1)

            # uses the random number created place a token of 'O' on the board

            self.buttons_list[random_button].config(text="O", bg='lightgreen', fg='darkblue')

            # Updates the button clicked list with the two new buttons

            self.button_clicked_list[random_button] = True

        else:

            messagebox.showwarning("Warning", "Button Five was already clicked!")
            return

    def button_six_clicked(self):

        if not self.button_clicked_list[5]:

            # clicked the button in the GUI

            self.button_six.config(text="X", bg='darkred', fg='green')

            self.button_clicked_list[5] = True

            # Checks if the board is filled before trying to find a random number

            i = 0

            for x in self.button_clicked_list:
                if not x:
                    i += 1

            if i == 0:
                return

            # Gets a random number and checks to make sure that it hasn't been clicked already

            random_button = random.randint(0, len(self.buttons_list) - 1)

            while random_button == 5 or self.button_clicked_list[random_button]:

                random_button = random.randint(0, len(self.buttons_list) - 1)

            # uses the random number created place a token of 'O' on the board

            self.buttons_list[random_button].config(text="O", bg='lightgreen', fg='darkblue')

            # Updates the button clicked list with the two new buttons

            self.button_clicked_list[random_button] = True

        else:

            messagebox.showwarning("Warning", "Button Six was already clicked!")
            return

    def button_seven_clicked(self):

        if not self.button_clicked_list[6]:

            # clicked the button in the GUI

            self.button_seven.config(text="X", bg='darkred', fg='green')

            self.button_clicked_list[6] = True

            # Checks if the board is filled before trying to find a random number

            i = 0

            for x in self.button_clicked_list:
                if not x:
                    i += 1

            if i == 0:
                return

            # Gets a random number and checks to make sure that it hasn't been clicked already

            random_button = random.randint(0, len(self.buttons_list) - 1)

            while random_button == 6 or self.button_clicked_list[random_button]:

                random_button = random.randint(0, len(self.buttons_list) - 1)

            # uses the random number created place a token of 'O' on the board

            self.buttons_list[random_button].config(text="O", bg='lightgreen', fg='darkblue')

            # Updates the button clicked list with the two new buttons

            self.button_clicked_list[random_button] = True

        else:

            messagebox.showwarning("Warning", "Button Seven was already clicked!")
            return

    def button_eight_clicked(self):

        if not self.button_clicked_list[7]:

            # clicked the button in the GUI

            self.button_eight.config(text="X", bg='darkred', fg='green')

            self.button_clicked_list[7] = True

            # Checks if the board is filled before trying to find a random number

            i = 0

            for x in self.button_clicked_list:
                if not x:
                    i += 1

            if i == 0:
                return

            # Gets a random number and checks to make sure that it hasn't been clicked already

            random_button = random.randint(0, len(self.buttons_list) - 1)

            while random_button == 7 or self.button_clicked_list[random_button]:

                random_button = random.randint(0, len(self.buttons_list) - 1)

            # uses the random number created place a token of 'O' on the board

            self.buttons_list[random_button].config(text="O", bg='lightgreen', fg='darkblue')

            # Updates the button clicked list with the two new buttons

            self.button_clicked_list[random_button] = True

        else:

            messagebox.showwarning("Warning", "Button Eight was already clicked!")
            return

    def button_nine_clicked(self):

        if not self.button_clicked_list[8]:

            # clicked the button in the GUI

            self.button_nine.config(text="X", bg='darkred', fg='green')

            self.button_clicked_list[8] = True

            # Checks if the board is filled before trying to find a random number

            i = 0

            for x in self.button_clicked_list:
                if not x:
                    i += 1

            if i == 0:
                return

            # Gets a random number and checks to make sure that it hasn't been clicked already

            random_button = random.randint(0, len(self.buttons_list) - 1)

            while random_button == 8 or self.button_clicked_list[random_button]:

                random_button = random.randint(0, len(self.buttons_list) - 1)

            # uses the random number created place a token of 'O' on the board

            self.buttons_list[random_button].config(text="O", bg='lightgreen', fg='darkblue')

            # Updates the button clicked list with the two new buttons

            self.button_clicked_list[random_button] = True

        else:

            messagebox.showwarning("Warning", "Button Nine was already clicked!")
            return


# Instantiation
if __name__ == '__main__':

    root = Tk()
    GUI = Game(root)
    root.mainloop()
