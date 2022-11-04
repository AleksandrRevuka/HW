from tkinter import *


def callback(e):
   print(e)


root = Tk()
button1 = Button(root, text='1')
button1.pack()
button2 = Button(root, text='2')
button2.pack()
button2 = Button(root, text='+')
button2.pack()
button2 = Button(root, text='=')
button2.pack()
root.bind_class('Button', '<1>', callback)
root.mainloop()
