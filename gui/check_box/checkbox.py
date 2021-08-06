from tkinter import *

from PIL import ImageTk, Image


def display():
    if (x.get()):
        print("You agree!")
    else:
        print("You don't agree.")


window = Tk()

img = Image.open('./resources/py_icon.png')
resized_image = img.resize((100, 100), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)

x = BooleanVar()  # returns 0 or 1
check_button = Checkbutton(window,
                           text="I agree to it.",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=('Arial', 20),
                           fg='#00ff00',
                           bg='black',
                           activeforeground="#00ff00",
                           activebackground="black",
                           padx=25,
                           pady=10,
                           image=new_image,
                           compound='left')

check_button.pack()
window.mainloop()
