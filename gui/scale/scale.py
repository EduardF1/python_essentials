from tkinter import *
from PIL import ImageTk, Image


def submit():
    print("The temperature is: " + str(scale.get()) + " degrees C")


window = Tk()

hotImage = Image.open('resources/fire.png')
resized_image = hotImage.resize((100, 100), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
hotLabel = Label(image=new_image)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,  # scale orientation
              font=('Consolas', 20),
              tickinterval=10,  # adds numeric indicators for value
              # showvalue=0,  # hide current value
              resolution=5,  # increment of slider
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='black'
              )
scale.set((scale['from'] - scale['to']) / 2 + scale['to'])  # set starting value
scale.pack()

coldImage = Image.open('resources/cold.png')
resized_image = coldImage.resize((100, 100), Image.ANTIALIAS)
new_image2 = ImageTk.PhotoImage(resized_image)
coldLabel = Label(image=new_image2)
coldLabel.pack()

button = Button(window, text="submit", command=submit)
button.pack()
window.mainloop()
