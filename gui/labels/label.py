from tkinter import *
from PIL import Image, ImageTk

# label = an area widget that holds text and/or an image within a window

window = Tk()

img = Image.open('./resources/py_icon.png')
resized_image = img.resize((100, 100), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)

label = Label(window,
              text="Hello fellow snake.",
              font=('Arial', 40, 'bold'),
              fg='#00FF00',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=new_image,
              compound='bottom')

# label.place(x=100, y=100)   # specify coordinates in px
label.pack()

window.mainloop()
