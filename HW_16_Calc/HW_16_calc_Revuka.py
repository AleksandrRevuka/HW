from tkinter import Tk, W, E
from tkinter.ttk import *
from multipledispatch import dispatch


class Interface(Frame, Label, Style):

    def __init__(self):
        super().__init__()
        self.window_calc()

    def window_calc(self):
        Style().configure("TButton", padding=6, font=("Comic Sans MS", 15, "bold"))

        self.columnconfigure(0)
        self.columnconfigure(1)
        self.columnconfigure(2)
        self.columnconfigure(3)

        self.rowconfigure(0)
        self.rowconfigure(1)
        self.rowconfigure(2)
        self.rowconfigure(3)
        self.rowconfigure(4)
        self.rowconfigure(5)
        self.rowconfigure(6)

        entry = Label(self, font=("Comic Sans MS", 20, "bold"))
        entry.grid(row=0, columnspan=4, sticky=W + E, pady=15)

        percent = Button(self, text="%")
        percent.grid(row=1, column=0)
        clean_all = Button(self, text="CE")
        clean_all.grid(row=1, column=1)
        clean = Button(self, text="C")
        clean.grid(row=1, column=2)
        backspace = Button(self, text="⇐")
        backspace.grid(row=1, column=3)

        one_x = Button(self, text="1/x")
        one_x.grid(row=2, column=0)
        degree = Button(self, text="x²")
        degree.grid(row=2, column=1)
        square_root = Button(self, text="√x")
        square_root.grid(row=2, column=2)
        divide = Button(self, text="÷")
        divide.grid(row=2, column=3)

        seven = Button(self, text="7")
        seven.grid(row=3, column=0)
        eight = Button(self, text="8")
        eight.grid(row=3, column=1)
        nine = Button(self, text="9")
        nine.grid(row=3, column=2)
        multiply = Button(self, text="×")
        multiply.grid(row=3, column=3)

        four = Button(self, text="4")
        four.grid(row=4, column=0)
        five = Button(self, text="5")
        five.grid(row=4, column=1)
        six = Button(self, text="6")
        six.grid(row=4, column=2)
        minus = Button(self, text="-")
        minus.grid(row=4, column=3)

        one = Button(self, text="1")
        one.grid(row=5, column=0)
        two = Button(self, text="2")
        two.grid(row=5, column=1)
        three = Button(self, text="3")
        three.grid(row=5, column=2)
        plus = Button(self, text="+")
        plus.grid(row=5, column=3)

        negative = Button(self, text="∓")
        negative.grid(row=6, column=0)
        zero = Button(self, text="0")
        zero.grid(row=6, column=1)
        dot = Button(self, text=".")
        dot.grid(row=6, column=2)
        equals = Button(self, text="=")
        equals.grid(row=6, column=3)
        self.pack()
        self.bind_all('<Button-1>', self.output_display)

    @staticmethod
    def output_display(e):
        print(f'{e}')


def main():
    root = Tk()
    root.title("My Calc")
    app = Interface()
    root.mainloop()


if __name__ == '__main__':
    main()
