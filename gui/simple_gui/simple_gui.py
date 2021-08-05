from tkinter import *

#   widgets = GUI elements: buttons, textboxes, labels, images
#   windows = serves as a container to hold or contain widgets

window = Tk()  # instantiate an instance of a window
window.geometry("420x420")  # specify window size
window.title("Simple GUI program")  # change window title
app_icon = PhotoImage(file='./resources/processing.png')  # transform icon asset to PhotoImage object
window.iconphoto(True, app_icon)  # set app icon
window.config(background="#5f7d95")

window.mainloop()  # place the window on the computer screen and listen for events
