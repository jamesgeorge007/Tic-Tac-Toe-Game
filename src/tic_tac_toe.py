# Tic-Tac-Toe Game in Python.
# <--Developed by James George--> #

from tkinter import Tk, messagebox, Button, Label

import random

import sys

class Game:

    # The initializer / constructor method which is being invoked on instantiation.
    
    def __init__(self, master):

        master.title('Tic Tac Toe')
        master.geometry('985x700')
        
        master.resizable(False, False)
        master.config(bg='skyblue')

        messagebox.showinfo("WELCOME", "Welcome to the Tic tac Toe Game!!")

        ''' Boolean values to keep track whether a button was already clicked or not implemented as a list.
         Initialilzing the list elements to False since the buttons are not clicked. '''

        self.one_clicked = False
        self.two_clicked = False
        self.three_clicked = False
        self.four_clicked = False
        self.five_clicked = False
        self.six_clicked = False
        self.seven_clicked = False
        self.eight_clicked = False
        self.nine_clicked = False
        
        self.button_clicked_list = [self.one_clicked, self.two_clicked, self.three_clicked, self.four_clicked, self.five_clicked, self.six_clicked, self.seven_clicked, self.eight_clicked, self.nine_clicked] 

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

        # List of all the buttons.

        self.buttons_list = [self.button_one, self.button_two, self.button_three, self.button_four, self.button_five, self.button_six, self.button_seven, self.button_eight, self.button_nine]

        # Intializing an empty list which will hold the list of all buttons already clicked by the user.       
        
        self.already_clicked_buttons = []
    
    def button_one_clicked(self):

        if not self.button_clicked_list[0]:
            
            self.button_one.config(text="X", bg='darkred', fg='white')

            self.already_clicked_buttons.append(self.buttons_list[0])

            self.random_button = random.randint(0, len(self.buttons_list)-1)

            if self.random_button == 0 or self.buttons_list[self.random_button] in self.already_clicked_buttons:
                
                self.button_one_clicked()

            else:

                self.buttons_list[self.random_button].config(text="O", bg='lightgreen', fg='darkblue')                  
            
                self.button_clicked_list[self.random_button] = True

            self.button_clicked_list[0] = True
            
            if len(self.buttons_list) > 0:

                self.buttons_list.remove(self.buttons_list[self.random_button])

            else:

                messagebox.showwarning("Warning", "The list is empty!")
                sys.exit()

        else:

            messagebox.showwarning("Warning", "Button One was already clicked!")
            return


    def button_two_clicked(self):

        if not self.button_clicked_list[1]:

            self.button_two.config(text="X", bg='darkred', fg='white')

            self.already_clicked_buttons.append(self.buttons_list[1])

            self.random_button = random.randint(0, len(self.buttons_list) - 1)

            if self.random_button == 1 or self.buttons_list[self.random_button] in self.already_clicked_buttons:

                self.button_two_clicked()

            else:

                self.buttons_list[self.random_button].config(text="O", bg='lightgreen', fg='darkblue')

                self.button_clicked_list[self.random_button] = True

            self.button_clicked_list[1] = True

            if len(self.buttons_list) > 0:
                
                self.buttons_list.remove(self.buttons_list[self.random_button])

            else:

                messagebox.showwarning("Warning", "The list is empty!")
                sys.exit()

        else:

            messagebox.showwarning("Warning", "Button Two was already clicked!")
            return


    def button_three_clicked(self):

        if not self.button_clicked_list[2]:

            self.button_three.config(text="X", bg='darkred', fg='white')

            self.already_clicked_buttons.append(self.buttons_list[2])

            self.random_button = random.randint(0, len(self.buttons_list) - 1)

            if self.random_button == 2 or self.buttons_list[self.random_button] in self.already_clicked_buttons:

                self.button_three_clicked()

            else:

                self.buttons_list[self.random_button].config(text="O", bg='lightgreen', fg='darkblue')

                self.button_clicked_list[self.random_button] = True
            

            self.button_clicked_list[2] = True
            
            if len(self.buttons_list) > 0:

                self.buttons_list.remove(self.buttons_list[self.random_button])

            else:

                messagebox.showwarning("Warning", "The list is empty!")
                sys.exit()

        else:

            messagebox.showwarning("Warning", "Button Three was already clicked!")
            return


    def button_four_clicked(self):

        if not self.button_clicked_list[3]:

            self.button_four.config(text="X", bg='darkred', fg='white')

            self.already_clicked_buttons.append(self.buttons_list[3])

            self.random_button = random.randint(0, len(self.buttons_list) - 1)

            if self.random_button == 3 or self.buttons_list[self.random_button] in self.already_clicked_buttons:

                self.button_four_clicked()

            else:

                self.buttons_list[self.random_button].config(text="O", bg='lightgreen', fg='darkblue')

                self.button_clicked_list[self.random_button] = True

            self.button_clicked_list[3] = True
            
            if len(self.buttons_list) > 0:

                self.buttons_list.remove(self.buttons_list[self.random_button])

            else:

                messagebox.showwarning("Warning", "The list is empty!")
                sys.exit()

        else:

            messagebox.showwarning("Warning", "Button Four was already clicked!")
            return


    def button_five_clicked(self):

        if not self.button_clicked_list[4]:

            self.button_five.config(text="X", bg='darkred', fg='white')

            self.already_clicked_buttons.append(self.buttons_list[4])

            self.random_button = random.randint(0, len(self.buttons_list) - 1)

            if self.random_button == 4 or self.buttons_list[self.random_button] in self.already_clicked_buttons:

                self.button_five_clicked()

            else:

                self.buttons_list[self.random_button].config(text="O", bg='lightgreen', fg='darkblue')

                self.button_clicked_list[self.random_button] = True

            self.button_clicked_list[4] = True
            
            if len(self.buttons_list) > 0:

                self.buttons_list.remove(self.buttons_list[self.random_button])

            else:

                messagebox.showwarning("Warning", "The list is empty!")
                sys.exit()

        else:

            messagebox.showwarning("Warning", "Button Five was already clicked!")
            return


    def button_six_clicked(self):

        if not self.button_clicked_list[5]:

            self.button_six.config(text="X", bg='darkred', fg='white')

            self.already_clicked_buttons.append(self.buttons_list[5])

            self.random_button = random.randint(0, len(self.buttons_list) - 1)

            if self.random_button == 5 or self.buttons_list[self.random_button] in self.already_clicked_buttons:

                self.button_six_clicked()

            else:

                self.buttons_list[self.random_button].config(text="O", bg='lightgreen', fg='darkblue')

                self.button_clicked_list[self.random_button] = True

            self.button_clicked_list[5] = True
            
            if len(self.buttons_list) > 0:
                
                self.buttons_list.remove(self.buttons_list[self.random_button])

            else:

                messagebox.showwarning("Warning", "The list is empty!")
                sys.exit()

        else:

            messagebox.showwarning("Warning", "Button Six was already clicked!")
            return


    def button_seven_clicked(self):

        if not self.button_clicked_list[6]:

            self.button_seven.config(text="X", bg='darkred', fg='white')

            self.already_clicked_buttons.append(self.buttons_list[6])

            self.random_button = random.randint(0, len(self.buttons_list) - 1)

            if self.random_button == 6 or self.buttons_list[self.random_button] in self.already_clicked_buttons:

                self.button_seven_clicked()

            else:

                self.buttons_list[self.random_button].config(text="O", bg='lightgreen', fg='darkblue')

                self.button_clicked_list[self.random_button] = True

            self.button_clicked_list[6] = True
            
            if len(self.buttons_list) > 0:

                self.buttons_list.remove(self.buttons_list[self.random_button])

            else:

                messagebox.showwarning("Warning", "The list is empty!")
                sys.exit()

        else:

            messagebox.showwarning("Warning", "Button Seven was already clicked!")
            return


    def button_eight_clicked(self):

        if not self.button_clicked_list[7]:

            self.button_eight.config(text="X", bg='darkred', fg='white')

            self.already_clicked_buttons.append(self.buttons_list[7])

            self.random_button = random.randint(0, len(self.buttons_list) - 1)

            if self.random_button == 7 or self.buttons_list[self.random_button] in self.already_clicked_buttons:

                self.button_eight_clicked()

            else:

                self.buttons_list[self.random_button].config(text="O", bg='lightgreen', fg='darkblue')

                self.button_clicked_list[self.random_button] = True

            self.button_clicked_list[7] = True
            
            if len(self.buttons_list) > 0:

                self.buttons_list.remove(self.buttons_list[self.random_button])

            else:

                messagebox.showwarning("Warning", "The list is empty!")
                sys.exit()

        else:

            messagebox.showwarning("Warning", "Button Eight was already clicked!")
            return


    def button_nine_clicked(self):

        if not self.button_clicked_list[8]:

            self.button_nine.config(text="X", bg='darkred', fg='white')

            self.already_clicked_buttons.append(self.buttons_list[8])

            self.random_button = random.randint(0, len(self.buttons_list) - 1)

            if self.random_button == 8 or self.buttons_list[self.random_button] in self.already_clicked_buttons:

                self.button_nine_clicked()

            else:

                self.buttons_list[self.random_button].config(text="O", bg='lightgreen', fg='darkblue')

                self.button_clicked_list[self.random_button] = True

            self.button_clicked_list[8] = True
            
            if len(self.buttons_list) > 0:
                
                self.buttons_list.remove(self.buttons_list[self.random_button])

            else:

                messagebox.showwarning("Warning", "The list is empty!")
                sys.exit()

        else:

            messagebox.showwarning("Warning", "Button Nine was already clicked!")
            return

# Instantiation
if __name__ == '__main__':
    
    root = Tk()
    GUI = Game(root)
    root.mainloop()        
        
