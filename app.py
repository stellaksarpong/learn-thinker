# import tkinter


# #it is use to create a window
# window =tkinter.Tk()



# window.mainloop()
# two ways
from tkinter import Tk
window= Tk()
#setting window title
window.title("Netflix")
# increase width and height
window.geometry('600x700')
# restricting user for increasing or reducing window
window.resizable(False,False)
#setting icon
window.iconbitmap("netflix.ico")
#backgroung colour
window.config(bg="blue")


window.mainloop()