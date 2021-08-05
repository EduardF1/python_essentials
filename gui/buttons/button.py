from tkinter import *
from PIL import Image, ImageTk

# button = when clicked, triggers some action

count = 0


def click():
    global count
    count += 1
    print(count)


window = Tk()
img = Image.open('./resources/py_icon.png')
resized_image = img.resize((100, 100), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)

button = Button(window,
                text="Click me!",
                command=click,
                font=("Comic Sans", 30),
                fg="#00ff00",
                bg="black",
                activeforeground="#00ff00",
                activebackground="black",
                state=ACTIVE,
                image=new_image,
                compound='top')

button.pack()
window.mainloop()
