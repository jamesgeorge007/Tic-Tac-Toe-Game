# Tic-Tac-Toe Game in Python.
# <--Developed by James George--> #

from tkinter import Tk, messagebox, Button, Label

class Game:

    # The initializer / constructor method which is being invoked on instantiation.
    
    def __init__(self, master):

        master.title('Tic Tac Toe')
        master.geometry('768x600')
        
        master.resizable(False, False)
        master.config(bg='skyblue')

        messagebox.showinfo("WELCOME", "Welcome to the Tic tac Toe Game!!")

        # Boolean variables (atributes) to keep track whether a button ws already clicked or not.
        
        self.one_clicked = False
        self.two_clicked = False
        self.three_clicked = False
        self.four_clicked = False
        self.five_clicked = False
        self.six_clicked = False
        self.seven_clicked = False
        self.eight_clicked = False
        self.nine_clicked = False

        self.result = Label(text="Tic Tac Toe Game", font="algerian 50 bold underline", fg="darkred", bg='skyblue')
        self.result.grid(row=0, column=0, columnspan=3)

        self.button_one = Button(text="X", font="times 50 bold", fg="black", bg="green", width="6", bd=5, relief='solid', command=self.button_one_clicked)
        self.button_one.grid(row=1, column=0)

        self.button_two = Button(text="X", font="times 50 bold", fg="black", bg="green", width="6", bd=5, relief='solid', command=self.button_two_clicked)
        self.button_two.grid(row=1, column=1)

        self.button_three = Button(text="X", font="times 50 bold", fg="black", bg="green", width="6", bd=5, relief='solid', command=self.button_three_clicked)
        self.button_three.grid(row=1, column=2)

        self.button_four = Button(text="O", font="times 50 bold", fg="black", bg="green", width="6", bd=5, relief='solid', command=self.button_four_clicked)
        self.button_four.grid(row=2, column=0)

        self.button_five = Button(text="O", font="times 50 bold", fg="black", bg="green", width="6", bd=5, relief='solid', command=self.button_five_clicked)
        self.button_five.grid(row=2, column=1)

        self.button_six = Button(text="O", font="times 50 bold", fg="black", bg="green", width="6", bd=5, relief='solid', command=self.button_six_clicked)
        self.button_six.grid(row=2, column=2)

        self.button_seven = Button(text="", font="times 50 bold", fg="black", bg="green", width="6", bd=5, relief='solid', command=self.button_seven_clicked)
        self.button_seven.grid(row=3, column=0)

        self.button_eight = Button(text="", font="times 50 bold", fg="black", bg="green", width="6", bd=5, relief='solid', command=self.button_eight_clicked)
        self.button_eight.grid(row=3, column=1)

        self.button_nine = Button(text="", font="times 50 bold", fg="black", bg="green", width="6", bd=5, relief='solid', command=self.button_nine_clicked)
        self.button_nine.grid(row=3, column=2)

    def button_one_clicked(self):

        if not self.one_clicked:
            
            messagebox.showinfo("Info", "Button One clicked!")
            self.one_clicked = True

        else:

            messagebox.showwarning("Warning", "Button One was already clicked!")
            return


    def button_two_clicked(self):

        if not self.two_clicked:

            messagebox.showinfo("Info", "Button Two clicked!")
            self.two_clicked = True

        else:

            messagebox.showwarning("Warning", "Button Two was already clicked!")
            return


    def button_three_clicked(self):

        if not self.three_clicked:

            messagebox.showinfo("Info", "Button Three clicked!")
            self.three_clicked = True

        else:

            messagebox.showwarning("Warning", "Button Three was already clicked!")
            return


    def button_four_clicked(self):

        if not self.four_clicked:

            messagebox.showinfo("Info", "Button Four clicked!")
            self.four_clicked = True

        else:

            messagebox.showwarning("Warning", "Button Four was already clicked!")
            return


    def button_five_clicked(self):

        if not self.five_clicked:

            messagebox.showinfo("Info", "Button Five clicked!")
            self.five_clicked = True

        else:

            messagebox.showwarning("Warning", "Button Five was already clicked!")
            return


    def button_six_clicked(self):

        if not self.six_clicked:

            messagebox.showinfo("Info", "Button Six clicked!")
            self.six_clicked = True

        else:

            messagebox.showwarning("Warning", "Button Six was already clicked!")
            return


    def button_seven_clicked(self):

        if not self.seven_clicked:

            messagebox.showinfo("Info", "Button Seven clicked!")
            self.seven_clicked = True

        else:

            messagebox.showwarning("Warning", "Button Seven was already clicked!")
            return


    def button_eight_clicked(self):

        if not self.eight_clicked:

            messagebox.showinfo("Info", "Button Eight clicked!")
            self.eight_clicked = True

        else:

            messagebox.showwarning("Warning", "Button Eight was already clicked!")
            return


    def button_nine_clicked(self):

        if not self.nine_clicked:

            messagebox.showinfo("Info", "Button Nine clicked!")
            self.nine_clicked = True

        else:

            messagebox.showwarning("Warning", "Button Nine was already clicked!")
            return

# Instantiation
if __name__ == '__main__':
    
    root = Tk()
    GUI = Game(root)
    root.mainloop()        
        
