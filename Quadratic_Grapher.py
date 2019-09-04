from tkinter import *
from tkinter.ttk import *  # Form Template
from tkinter import ttk
import turtle
import os
import time
import sys

def main():
    def b1 ():
        def submit ():
            def hl(y):
                t.pencolor('black')
                t.penup()
                t.setpos(-630, y)
                t.pendown()
                t.setpos(630, y)
            def vl(y):
                t.pencolor('black')
                t.penup()
                t.setpos(y, -600)
                t.pendown()
                t.setpos(y, 600)
            root.destroy()
            t = turtle.Pen()
            wn=turtle.Screen()
            wn.screensize()
            wn.setup(width=1.0, height=1.0)
            y=-330
            n=-630
            t.speed(0)
            t.width(4)
            hl(0)
            vl(0)
            t.width(1)
            for x in range (23):
                hl(y)
                y+=30
                vl(n)
                n+=30
                vl(n)
                n+=30
            t.penup()
            xno=-598
            t.pencolor('red')
            for x in range (40):
                t.setpos(xno,2)
                t.write(xno//30)
                xno+=30
            yno = -598
            t.pencolor('red')
            for x in range (40):
                t.setpos(2,yno)
                t.write(yno//30)
                yno+=30

            t.speed(0)
            xcordinate=0
            ycordinate=0
            while -300<=ycordinate <=300:
                xcordinate-=1
                ycordinate = (xcordinate ** 2) * a2.get()

            ycordinate = (xcordinate ** 2) * a2.get()
            t.penup()
            t.setpos(xcordinate*30,ycordinate*30)
            t.pendown()
            t.width(2)
            for x in range (round(xcordinate*-20)):
                xcordinate+=0.1
                ycordinate=(xcordinate**2)*a2.get()
                t.setpos(xcordinate*30, ycordinate*30)
            time.sleep(displaytime.get())
            os.startfile(r"C:\Quadratic_Grapher2\Quadratic_Grapher2.exe")
            turtle.Screen().bye()
            sys.exit()


        Label1 = Label(bottomframe,
                       text='y = ')
        Label1.grid(row=0, column=0, sticky=E,)
        a2=DoubleVar(bottomframe)
        a = ttk.Entry(bottomframe, style='TEntry', textvariable=a2)
        a.grid(row=0, column=1,
                     sticky=NSEW)
        Label2 = Label(bottomframe,
                       text='x^2')
        Label2.grid(row=0, column=2, sticky=NSEW)
        Label3 = Label(bottomframe,
                       text='Display Time (s)')
        Label3.grid(row=1, column=0, sticky=NSEW)
        displaytime = IntVar(bottomframe)
        SpinBox1 = Spinbox(bottomframe, from_=1, to=10, increment=1,
                           textvariable=displaytime)
        SpinBox1.grid(row=1, column=1, sticky=NSEW)
        regbutton = Button(bottomframe, text="Submit",
                           state=ACTIVE, width=30, command=submit)
        regbutton.grid(row=2, column=1,)


    def b2 ():
        def submit ():
            def hl(y):
                t.pencolor('black')
                t.penup()
                t.setpos(-630, y)
                t.pendown()
                t.setpos(630, y)
            def vl(y):
                t.pencolor('black')
                t.penup()
                t.setpos(y, -600)
                t.pendown()
                t.setpos(y, 600)
            root.destroy()
            t = turtle.Pen()
            wn = turtle.Screen()
            wn.screensize()
            wn.setup(width=1.0, height=1.0)
            y=-330
            n=-630
            t.speed(0)
            t.width(4)
            hl(0)
            vl(0)
            t.width(1)
            for x in range (23):
                hl(y)
                y+=30
                vl(n)
                n+=30
                vl(n)
                n+=30
            t.penup()
            xno=-598
            t.pencolor('red')
            for x in range (40):
                t.setpos(xno,2)
                t.write(xno//30)
                xno+=30
            yno = -598
            t.pencolor('red')
            for x in range (40):
                t.setpos(2,yno)
                t.write(yno//30)
                yno+=30

            t.speed(0)
            xcordinate=0
            ycordinate=0
            while -300<=ycordinate <=300:
                xcordinate-=1
                ycordinate = (xcordinate ** 2) * a2.get() + xcordinate*b2.get() + c2.get()

            ycordinate = (xcordinate ** 2) * a2.get() + xcordinate * b2.get() + c2.get()
            t.penup()
            t.setpos(xcordinate*30,ycordinate*30)
            t.pendown()
            t.width(2)
            for x in range (round(xcordinate*-20)):
                xcordinate+=0.1
                ycordinate = (xcordinate ** 2) * a2.get() + xcordinate*b2.get() + c2.get()
                t.setpos(xcordinate*30, ycordinate*30)
            time.sleep(displaytime.get())
            os.startfile(r"C:\Quadratic_Grapher2\Quadratic_Grapher2.exe")
            turtle.Screen().bye()
            sys.exit()


        Label1 = Label(bottomframe,
                       text='y = ')
        Label1.grid(row=0, column=0, sticky=E,)
        a2=DoubleVar(bottomframe)
        a = ttk.Entry(bottomframe, style='TEntry', textvariable=a2)
        a.grid(row=0, column=1,
                     sticky=NSEW)
        Label2 = Label(bottomframe,
                       text='x^2 +')
        Label2.grid(row=0, column=2, sticky=NSEW)
        b2 = DoubleVar(bottomframe)
        b = ttk.Entry(bottomframe, style='TEntry', textvariable=b2)
        b.grid(row=0, column=3,
               sticky=NSEW)
        Label2b = Label(bottomframe,
                       text='x +')
        Label2b.grid(row=0, column=4, sticky=NSEW)
        c2 = DoubleVar(bottomframe)
        c = ttk.Entry(bottomframe, style='TEntry', textvariable=c2)
        c.grid(row=0, column=5,
               sticky=NSEW)
        Label3 = Label(bottomframe,
                       text='Display Time (s)')
        Label3.grid(row=1, column=0, sticky=NSEW)
        displaytime = IntVar(bottomframe)
        SpinBox1 = Spinbox(bottomframe, from_=1, to=10, increment=1,
                           textvariable=displaytime)
        SpinBox1.grid(row=1, column=1, sticky=NSEW)
        regbutton = Button(bottomframe, text="Submit",
                           state=ACTIVE, width=30, command=submit)
        regbutton.grid(row=2, column=1,)


    root = Tk()
    s = ttk.Style()
    root.configure(background='lightblue')
    root.geometry("1280x600")
    root.title("Quadratic Grapher")
    root.resizable(True, True)
    root.attributes('-fullscreen', True)
    Label(root, text="Quadratic grapher").pack()
    topframe = Frame(root)
    topframe.pack(side=TOP, fill=BOTH, padx=50, pady=10)
    bottomframe = Frame(root)
    bottomframe.pack(side=BOTTOM, fill=BOTH, padx=50, pady=10)

    b1 = Button(topframe, text="y=ax^2",
                         state=ACTIVE, width=50, command=b1)  # Height is measures in lines and Width is defined in characters and not Pixels
    b1.grid(row=0,padx=10,pady=10)

    b2 = Button(topframe, text="y=ax^2+bx+c",
                     state=ACTIVE, width=50, command=b2)  # Height is measures in lines and Width is defined in characters and not Pixels
    b2.grid(row=1,padx=10,pady=10)


    root.mainloop()

while True:
    main()
