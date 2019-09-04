from tkinter import *
from tkinter.ttk import *  # Form Template
from tkinter import ttk
import turtle
import os
import time
import sys

root = Tk()
s = ttk.Style()
root.configure(background='lightblue')
root.geometry("1280x600")
root.title("Cumulative frequency")
root.resizable(True, True)
root.attributes('-fullscreen', True)
Label(root, text="Cumulative frequency").pack()
topframe = Frame(root)
topframe.pack(side=TOP, fill=BOTH, padx=50, pady=10)
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM, fill=BOTH, padx=50, pady=10)


list=[]
height = 10
width = 5
for i in range(height): #Rows
    for j in range(width): #Columns
        a2 = DoubleVar(bottomframe)
        a = ttk.Entry(bottomframe, style='TEntry', textvariable=a2)
        a.grid(row=i, column=j,)
        list.append(a2.get())

root.mainloop()
