# radio button = similar to checkbox, but only one option can be selected from the group
from tkinter import *

food = ["pizza", "hamburger", "hotdog"]


def order():
    if x.get() == 0:
        print("You ordered pizza")
    elif x.get() == 1:
        print("You ordered a hamburger")
    elif x.get() == 2:
        print("You ordered a hotdog")
    else:
        print("Undefined")


window = Tk()
pizzaImage = PhotoImage(file='./resources/pizza.png')
hamburgerImage = PhotoImage(file='./resources/hamburger.png')
hotdogImage = PhotoImage(file='./resources/hotdog.png')

foodImages = [pizzaImage, hamburgerImage, hotdogImage]

x = IntVar()

for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index],  # add text to radio buttons
                               variable=x,  # groups radio buttons together if they share the same variable
                               value=index,  # assign each radio button a different value
                               padx=25,  # add padding to the x-axis
                               font=("Impact", 30),
                               image=foodImages[index],  # add image to radiobutton
                               compound='left',  # adds image & text (left-side)
                               indicatoron=0,  # eliminate circle indicators
                               width=375,  # set width of radio buttons
                               command=order  # set command of radiobutton to function
                               )
    radio_button.pack(anchor=W)

window.mainloop()
