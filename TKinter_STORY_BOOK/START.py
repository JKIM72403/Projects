from tkinter import *
from tkinter import ttk, font

#This is the Title Page

root = Tk()

#Styles
style = ttk.Style()
style.configure("TFrame", background="White")
style.configure("TLabel", background="White")
style.configure("TButton", background="Black")

mainframe = ttk.Frame(root).grid(column=0, row=0)

#Changed up the font
Biggertitlefont = font.Font(family='Helvetica', size=30, weight='bold')

storyframe1 = ttk.Frame(mainframe, borderwidth=5, relief = "ridge", width=800, height= 800).grid(row=0, column=1, rowspan=5, columnspan=5)
label = ttk.Label(storyframe1, text = "WELCOME TO HERO VS VILLAIN", font = Biggertitlefont).grid(column=3, row=2)

#import command
def switch():
    root.destroy() 
    import TKinterStory

#button
story1tostory2 = ttk.Button(mainframe, text="START", command=switch).grid(row=4, column=3)

root.mainloop()
