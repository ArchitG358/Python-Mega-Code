from tkinter import *

window = Tk()


def km_to_miles():
    print("Success!")
    miles = float(e1_value.get())*1.6
    t1.insert(END,miles)


b1 = Button(window, text = "Execute", command = km_to_miles)
b1.grid(row = 1, column = 0)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row =0, column = 0)

t1 = Text(window, height =2, width = 15)
t1.grid(row = 0, column = 10)

window.mainloop()
