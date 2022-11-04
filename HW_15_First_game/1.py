from tkinter import *


def callback(e):
   k = []
   j = e.widget['text']
   k.append(j)
   if j == 'c':
      k.clear()
   return k


def operation(data):
   for i in data:
      if i.isdigit


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
