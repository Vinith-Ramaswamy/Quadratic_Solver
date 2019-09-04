from tkinter import *
from tkinter.ttk import *  # Form Template
from tkinter import ttk
import turtle
import os
import sys
import turtle as z
import math

global basedir
basedir = os.path.abspath(os.path.dirname(__file__))


def main():
    def b1 ():#the top button (vertex form)
        bottomframe1.pack_forget() #clears the other frame
        bottomframe.pack(side=BOTTOM, fill=BOTH, padx=50, pady=10) #displays the new frame
        def submit ():  #command for the submit button
            def loop(): #to exit this program and opens the other one
                def end():
                    os.startfile(basedir+"\Quadratic_Solver2.exe")
                    info.destroy()
                    sys.exit()

                turtle.Screen().bye()
                info = Tk()
                s = Style()  # Default Theme is Default - Other Themes are Clam, Alt and Classic
                s.theme_use('clam')  # Code to Change the Theme

                s.configure('.', font=('arial', 26), background='dark green', foreground='white')  # Applies to All
                s.configure('TLabel', foreground='white', background='dark green')
                s.configure('TFrame', foreground='white', background='dark green')
                s.map('TButton', background=[('pressed', 'yellow'), ('active', 'white')],
                      foreground=[('pressed', 'black'), ('active', 'blue')])

                info.configure(background='black')
                info.geometry("1280x600")
                info.title("Quadratic Grapher")
                info.resizable(True, True)
                info.attributes('-fullscreen', True)
                Label(info, text="Information About Quadratics", font=('arial', 26)).pack(pady=10)
                regbutton = Button(info, text="          Press here to continue          ",
                                   state=NORMAL, command=end, style='TButton')
                regbutton.pack(pady=10, side=BOTTOM)

                leftframe = Frame(info, style='TFrame')
                leftframe.pack(side=LEFT, fill=BOTH, padx=18, pady=20)
                rightframe = Frame(info, style='TFrame')
                rightframe.pack(side=RIGHT, fill=BOTH, padx=18, pady=20)
                middleframe = Frame(info, style='TFrame')
                middleframe.pack(side=LEFT, fill=BOTH, padx=18, pady=20)

                Label(leftframe, text="General form", font=('arial', 26)).pack(padx=80, pady=10)
                Label(leftframe,
                      text='A quadratic equation in the\ngeneral form can be written\nin the form: y=ax\u00b2+bx+c',
                      font=('arial', 20)).pack(padx=20, pady=10, anchor=W)
                Label(leftframe,
                      text='The x coordinate for the\nvertex of the parabola can be\ncalculated using the formula \n-b/2a',
                      font=('arial', 20)).pack(padx=20, pady=10, anchor=W)
                Label(leftframe,
                      text='The y coordinate for the\nvertex of the parabola can be\ncalculated by substituting x\nfor -b/2a in the equation',
                      font=('arial', 20)).pack(padx=20, pady=10, anchor=W)

                Label(rightframe, text="Vertex form", font=('arial', 26)).pack(padx=105, pady=10)
                Label(rightframe,
                      text='A quadratic equation in\nthe general form can be\nwritten in the form:\ny=(x-3)\u00b2+1\n',
                      font=('arial', 24)).pack(padx=20, pady=10, anchor=W)
                Label(rightframe,
                      text='The coordinates for the\nvertex of a parabola in\nthe vertex form is equal\n to (h,k)',
                      font=('arial', 24)).pack(padx=20, pady=10, anchor=W)

                Label(middleframe, text="Quadratic Equations", font=('arial', 26)).grid(row=0, column=1, padx=10,
                                                                                        pady=10)
                Label(middleframe, text="When a Quadratic Equation\nis graphed, a curve is\ndrawn",
                      font=('arial', 21)).grid(row=1, column=1, padx=20, pady=10, sticky=W)
                Label(middleframe, text='A quadratic equation can \nbe in either the vertex\nor general form',
                      font=('arial', 21)).grid(row=2, column=1, padx=20, pady=10, sticky=W)
                Label(middleframe, text="The larger the Value of 'a',\nthe wider the parabola",
                      font=('arial', 21)).grid(row=3, column=1, padx=20, pady=10, sticky=W)
                Label(middleframe,
                      text="If 'a' is positive, the parabola\n opens upward and if a is\nnegative, the opens\ndownward",
                      font=('arial', 21)).grid(row=4, column=1, padx=20, pady=10, sticky=W)
                middleframe.grid_columnconfigure(0, weight=1)
                middleframe.grid_columnconfigure(2, weight=1)



            def hl(y): #to draw a horizontal line
                t.pencolor('black')
                t.penup()
                t.setpos(-630, y)
                t.pendown()
                t.setpos(630, y)
            def vl(y):#to draw a verticle line
                t.pencolor('black')
                t.penup()
                t.setpos(y, -600)
                t.pendown()
                t.setpos(y, 600)
            root.destroy() #destroys the mainpage
            t = turtle.Pen()
            wn = turtle.Screen()
            wn.screensize()
            wn.setup(width=1.0, height=1.0) #for full screen
            y=-330
            n=-630 #used n because x was taken in the for loop
            t.speed(0)
            t.width(4)
            hl(0)
            vl(0)
            t.width(1)
            for x in range (23): #draws up the full grid
                hl(y)
                y+=30
                vl(n)
                n+=30
                vl(n)
                n+=30
            t.penup()
            xno=-598
            t.pencolor('red')
            for x in range (40): #labels the x axis
                t.setpos(xno,2)
                t.write(xno//30)
                xno+=30
            yno = -598
            t.pencolor('red')
            for x in range (40): #labels the y axis
                t.setpos(2,yno)
                t.write(yno//30)
                yno+=30

            t.speed(0)
            xcordinate=h2.get()
            xtimes=0
            ycordinate=0
            while -12<=ycordinate <=12: #checks what x cordinate to start with
                xtimes+=1
                xcordinate-=1
                ycordinate = ((xcordinate*a2.get() - h2.get()*a2.get()) ** 2 + k2.get())
            t.penup()
            t.setpos(xcordinate*30,ycordinate*30) #puts the pen in place before starting to draw (prevents connecting line
            t.pendown()
            t.width(2)
            for x in range (round(xtimes*20)): #draws the parabola
                xcordinate+=0.1
                ycordinate = ((xcordinate*a2.get() - h2.get()*a2.get()) ** 2 + k2.get())
                t.setpos(xcordinate*30, ycordinate*30)

            t.penup()
            t.pencolor('blue')
            t.setpos(330, -120)
            t.write('Press the Spacebar to Continue', font='comicsansms, 15')
            try: #calculates the x intercept
                a=a2.get()**2
                b=-2*a2.get()*(h2.get()*a2.get())
                c=(h2.get()*a2.get())**2+k2.get()
                ans1 = ((b * -1) + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
                ans2 = ((b * -1) - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
                t.setpos(-450, -90)
                t.write(f'x = {ans1} ', font='comicsansms, 15')
                t.setpos(-450, -150)
                t.write(f'x = {ans2} ', font='comicsansms, 15')
            except:
                t.setpos(-450, -90)
                t.write('No Solution', font='comicsansms, 15')

            t.setpos(-600,300)
            if h2.get()<0:
                if k2.get()<0:
                    t.write(f'y=({a2.get()}x+{h2.get()*-1})\u00b2{k2.get()}', font='comicsansms, 15')
                elif k2.get()>0:
                    t.write(f'y=({a2.get()}x+{h2.get()*-1})\u00b2+{k2.get()}', font='comicsansms, 15')
            if h2.get() > 0:
                if k2.get() < 0:
                    t.write(f'y=({a2.get()}x{h2.get()*-1})\u00b2{k2.get()}', font='comicsansms, 15')
                elif k2.get() > 0:
                    t.write(f'y=({a2.get()}x{h2.get()*-1})\u00b2+{k2.get()}', font='comicsansms, 15')

            z.onkey(loop, 'space') #code for press space to continue
            z.listen()
            z.mainloop()

#----------------------starts writting the text for the equation-----------------#
        Label1 = Label(bottomframe,
                       text='y = ', style='TLabel')
        Label1.grid(row=0, column=0, sticky=E, padx=10,pady=10)
        a2 = DoubleVar(bottomframe)
        a = ttk.Entry(bottomframe, style='TEntry', textvariable=a2)
        a.grid(row=0, column=1,
               sticky=NSEW, padx=10, pady=10)
        Label1 = Label(bottomframe,
                       text='(x-', style='TLabel')
        Label1.grid(row=0, column=2, sticky=E, padx=10, pady=10)
        h2=DoubleVar(bottomframe)
        h = ttk.Entry(bottomframe, style='TEntry', textvariable=h2)
        h.grid(row=0, column=3,
                     sticky=NSEW, padx=10,pady=10)
        Label2 = Label(bottomframe,
                       text=')\u00b2', style='TLabel')
        Label2.grid(row=0, column=4, sticky=NSEW, padx=10,pady=10)
        Label2 = Label(bottomframe,
                       text='+', style='TLabel')
        Label2.grid(row=0, column=5, sticky=NSEW, padx=10, pady=10)
        k2 = DoubleVar(bottomframe)
        k = ttk.Entry(bottomframe, style='TEntry', textvariable=k2)
        k.grid(row=0, column=6,
               sticky=NSEW, padx=10, pady=10)

        regbutton = Button(bottomframe, text="Submit",
                           state=NORMAL, command=submit, style='TButton')
        regbutton.grid(row=2, column=1, padx=10,pady=10)

# ----------------------ends writting the text for the equation-----------------#

    def b2 ():
        bottomframe.pack_forget()
        bottomframe1.pack(side=BOTTOM, fill=BOTH, padx=50, pady=10)
        def submit ():
            def loop():  # to exit this program and opens the other one
                def end():
                    os.startfile(basedir+"\Quadratic_Solver2.exe")
                    info.destroy()
                    sys.exit()

                turtle.Screen().bye()
                info = Tk()
                s = Style()  # Default Theme is Default - Other Themes are Clam, Alt and Classic
                s.theme_use('clam')  # Code to Change the Theme

                s.configure('.', font=('arial', 26), background='dark green', foreground='white')  # Applies to All
                s.configure('TLabel', foreground='white', background='dark green')
                s.configure('TFrame', foreground='white', background='dark green')
                s.map('TButton', background=[('pressed', 'yellow'), ('active', 'white')],
                      foreground=[('pressed', 'black'), ('active', 'blue')])

                info.configure(background='black')
                info.geometry("1280x600")
                info.title("Quadratic Grapher")
                info.resizable(True, True)
                info.attributes('-fullscreen', True)
                Label(info, text="Information About Quadratics", font=('arial', 26)).pack(pady=10)
                regbutton = Button(info, text="          Press here  to continue          ",
                                   state=NORMAL, command=end, style='TButton')
                regbutton.pack(pady=10, side=BOTTOM)

                leftframe = Frame(info, style='TFrame')
                leftframe.pack(side=LEFT, fill=BOTH, padx=18, pady=20)
                rightframe = Frame(info, style='TFrame')
                rightframe.pack(side=RIGHT, fill=BOTH, padx=18, pady=20)
                middleframe = Frame(info, style='TFrame')
                middleframe.pack(side=LEFT, fill=BOTH, padx=18, pady=20)

                Label(leftframe, text="General form", font=('arial', 26)).pack(padx=80, pady=10)
                Label(leftframe,
                      text='A quadratic equation in the\ngeneral form can be written\nin the form: y=ax\u00b2+bx+c',
                      font=('arial', 20)).pack(padx=20, pady=10, anchor=W)
                Label(leftframe,
                      text='The x coordinate for the\nvertex of the parabola can be\ncalculated using the formula \n-b/2a',
                      font=('arial', 20)).pack(padx=20, pady=10, anchor=W)
                Label(leftframe,
                      text='The y coordinate for the\nvertex of the parabola can be\ncalculated by substituting x\nfor -b/2a in the equation',
                      font=('arial', 20)).pack(padx=20, pady=10, anchor=W)

                Label(rightframe, text="Vertex form", font=('arial', 26)).pack(padx=105, pady=10)
                Label(rightframe,
                      text='A quadratic equation in\nthe general form can be\nwritten in the form:\ny=(x-3)\u00b2+1\n',
                      font=('arial', 24)).pack(padx=20, pady=10, anchor=W)
                Label(rightframe,
                      text='The coordinates for the\nvertex of a parabola in\nthe vertex form is equal\n to (h,k)',
                      font=('arial', 24)).pack(padx=20, pady=10, anchor=W)

                Label(middleframe, text="Quadratic Equations", font=('arial', 26)).grid(row=0, column=1, padx=10,
                                                                                        pady=10)
                Label(middleframe, text="When a Quadratic Equation\nis graphed, a curve is\ndrawn",
                      font=('arial', 21)).grid(row=1, column=1, padx=20, pady=10, sticky=W)
                Label(middleframe, text='A quadratic equation can \nbe in either the vertex\nor general form',
                      font=('arial', 21)).grid(row=2, column=1, padx=20, pady=10, sticky=W)
                Label(middleframe, text="The larger the Value of 'a',\nthe wider the parabola",
                      font=('arial', 21)).grid(row=3, column=1, padx=20, pady=10, sticky=W)
                Label(middleframe,
                      text="If 'a' is positive, the parabola\n opens upward and if a is\nnegative, the opens\ndownward",
                      font=('arial', 21)).grid(row=4, column=1, padx=20, pady=10, sticky=W)
                middleframe.grid_columnconfigure(0, weight=1)
                middleframe.grid_columnconfigure(2, weight=1)

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
            xcordinate = -b2.get()/(2*a2.get())
            xtimes = 0
            ycordinate = 0
            while -12 <= ycordinate <= 12:
                xtimes += 1
                xcordinate -= 1
                ycordinate = (xcordinate ** 2) * a2.get() + xcordinate * b2.get() + c2.get()
            t.penup()
            t.setpos(xcordinate * 30, ycordinate * 30)
            t.pendown()
            t.width(2)
            for x in range(round(xtimes * 20)):
                xcordinate += 0.1
                ycordinate = (xcordinate ** 2) * a2.get() + xcordinate * b2.get() + c2.get()
                t.setpos(xcordinate * 30, ycordinate * 30)

            t.penup()
            t.pencolor('blue')
            t.setpos(330, -120)
            t.write('Press the Spacebar to Continue', font='comicsansms, 15')
            try:
                ans1 = ((b2.get() * -1) + math.sqrt((b2.get() ** 2) - 4 * a2.get() * c2.get())) / (2 * a2.get())
                ans2 = ((b2.get() * -1) - math.sqrt((b2.get() ** 2) - 4 * a2.get() * c2.get())) / (2 * a2.get())
                t.setpos(-450, -90)
                t.write(f'x = {ans1} ', font='comicsansms, 15')
                t.setpos(-450, -150)
                t.write(f'x = {ans2} ', font='comicsansms, 15')
            except:
                t.setpos(-450, -90)
                t.write('No Solution', font='comicsansms, 15')
            t.setpos(-600,300)
            if b2.get()<0:
                if c2.get()<0:
                    t.write(f'y={a2.get()}x\u00b2{b2.get()}x{c2.get()}', font='comicsansms, 15')
                elif c2.get()>0:
                    t.write(f'y={a2.get()}x\u00b2{b2.get()}x+{c2.get()}', font='comicsansms, 15')
            if b2.get() > 0:
                if c2.get() < 0:
                    t.write(f'y={a2.get()}x\u00b2+{b2.get()}x{c2.get()}', font='comicsansms, 15')
                elif c2.get() > 0:
                    t.write(f'y={a2.get()}x\u00b2+{b2.get()}x+{c2.get()}', font='comicsansms, 15')

            z.onkey(loop, 'space')
            z.listen()
            z.mainloop()

        Label1 = Label(bottomframe1,
                       text='y = ', style='TLabel')
        Label1.grid(row=0, column=0, sticky=E, padx=10,pady=10)
        a2=DoubleVar(bottomframe1)
        a = ttk.Entry(bottomframe1, style='TEntry', textvariable=a2)
        a.grid(row=0, column=1,
                     sticky=NSEW, padx=10,pady=10)
        Label2 = Label(bottomframe1,
                       text='x\u00b2 +', style='TLabel')
        Label2.grid(row=0, column=2, sticky=NSEW, padx=10,pady=10)
        b2 = DoubleVar(bottomframe1)
        b = ttk.Entry(bottomframe1, style='TEntry', textvariable=b2)
        b.grid(row=0, column=3,
               sticky=NSEW, padx=10,pady=10)
        Label2b = Label(bottomframe1,
                       text='x +', style='TLabel')
        Label2b.grid(row=0, column=4, sticky=NSEW, padx=10,pady=10)
        c2 = DoubleVar(bottomframe1)
        c = ttk.Entry(bottomframe1, style='TEntry', textvariable=c2)
        c.grid(row=0, column=5,
               sticky=NSEW, padx=10,pady=10)
        regbutton = Button(bottomframe1, text="Submit",
                           state=NORMAL, command=submit, style='TButton')
        regbutton.grid(row=1, column=1, padx=10,pady=10)

    def b3 ():
        def submit():
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

            xcordinate = -b2.get() / (2 * a2.get())
            xtimes = 0
            ycordinate = 0
            while -12 <= ycordinate <= 12:
                xtimes += 1
                xcordinate -= 1
                ycordinate = (xcordinate ** 2) * a2.get() + xcordinate * b2.get() + c2.get()
            t.penup()
            t.setpos(xcordinate * 30, ycordinate * 30)
            t.pendown()
            t.width(2)
            for x in range(round(xtimes * 20)):
                xcordinate += 0.1
                ycordinate = (xcordinate ** 2) * a2.get() + xcordinate * b2.get() + c2.get()
                t.setpos(xcordinate * 30, ycordinate * 30)

        Label1 = Label(bottomframe1,
                       text='y = ', style='TLabel')
        Label1.grid(row=0, column=0, sticky=E, padx=10, pady=10)
        a2 = DoubleVar(bottomframe1)
        a = ttk.Entry(bottomframe1, style='TEntry', textvariable=a2)
        a.grid(row=0, column=1,
               sticky=NSEW, padx=10, pady=10)
        Label2 = Label(bottomframe1,
                       text='(x +', style='TLabel')
        Label2.grid(row=0, column=2, sticky=NSEW, padx=10, pady=10)
        b2 = DoubleVar(bottomframe1)
        b = ttk.Entry(bottomframe1, style='TEntry', textvariable=b2)
        b.grid(row=0, column=3,
               sticky=NSEW, padx=10, pady=10)
        Label2b = Label(bottomframe1,
                        text=') (x +', style='TLabel')
        Label2b.grid(row=0, column=4, sticky=NSEW, padx=10, pady=10)
        c2 = DoubleVar(bottomframe1)
        c = ttk.Entry(bottomframe1, style='TEntry', textvariable=c2)
        c.grid(row=0, column=5,
               sticky=NSEW, padx=10, pady=10)
        Label2b = Label(bottomframe1,
                        text=')', style='TLabel')
        Label2b.grid(row=0, column=6, sticky=NSEW, padx=10, pady=10)
        regbutton = Button(bottomframe1, text="Submit",
                           state=NORMAL, command=submit, style='TButton')
        regbutton.grid(row=1, column=1, padx=10, pady=10)
    root = Tk()
    s = Style()  # Default Theme is Default - Other Themes are Clam, Alt and Classic
    s.theme_use('clam')  # Code to Change the Theme

    s.configure('.', font=('verdana', 14), background='yellow')  # Applies to All
    s.configure('TEntry', foreground='darkblue')
    s.configure('TLabel', foreground='white', background='dark green')
    s.configure('TFrame', foreground='white', background='dark green')
    s.map('TButton', background=[('pressed', 'orange'), ('active', 'white')],
          foreground=[('pressed', 'red'), ('active', 'blue')])

    root.configure(background='black')
    root.geometry("1280x600")
    root.title("Quadratic Grapher")
    root.resizable(True, True)
    root.attributes('-fullscreen', True)
    Label(root, text="Quadratic grapher, Designed by Vinith Ramaswamy:Year 9").pack()
    topframe = Frame(root, style='TFrame')
    topframe.pack(side=TOP, fill=BOTH, padx=50, pady=10)
    bottomframe = Frame(root, style='TFrame')
    bottomframe.pack(side=BOTTOM, fill=BOTH, padx=50, pady=10)
    bottomframe1 = Frame(root, style='TFrame')
    bottomframe1.pack(side=BOTTOM, fill=BOTH, padx=50, pady=10)

    b1 = Button(topframe, text="Vertex Form",
                         state=NORMAL, width=20, command=b1, style='TButton')  # Height is measures in lines and Width is defined in characters and not Pixels
    b1.grid(row=0,padx=100, pady=10)


    b2 = Button(topframe, text="General Form",
                     state=NORMAL, width=20, command=b2, style='TButton')  # Height is measures in lines and Width is defined in characters and not Pixels
    b2.grid(row=1,padx=100, pady=10)

    b2 = Button(topframe, text="Factorising Form",
                state=NORMAL, width=20, command=b3,
                style='TButton')  # Height is measures in lines and Width is defined in characters and not Pixels
    b2.grid(row=2, padx=100, pady=10)



    Label1 = Label(topframe,
                   text=' eg. y=(x-3)\u00b2+1', style='TLabel')
    Label1.grid(row=0, column=1, sticky=NSEW, padx=100, pady=10)
    Label1 = Label(topframe,
                   text=' eg. y=-x\u00b2+2x+1', style='TLabel')
    Label1.grid(row=1, column=1, sticky=NSEW, padx=100, pady=10)

    Label1 = Label(topframe,
                   text=' eg. y=-x\u00b2+2x+1', style='TLabel')
    Label1.grid(row=2, column=1, sticky=NSEW, padx=100, pady=10)

    b1photo=PhotoImage(file=basedir+"/b1.GIF")
    b1photo = b1photo.zoom(9)  # with 250, I ended up running out of memory
    b1photo = b1photo.subsample(10)
    label = Label(topframe,image=b1photo)
    label.image = b1photo  # keep a reference!
    label.grid(row=0, column=2, sticky=NSEW, padx=100, pady=10)

    b2photo = PhotoImage(file=basedir+"/b2.GIF")
    b2photo = b2photo.zoom(9)  # with 250, I ended up running out of memory
    b2photo = b2photo.subsample(10)
    label = Label(topframe, image=b2photo)
    label.image = b2photo  # keep a reference!
    label.grid(row=1, column=2, sticky=NSEW, padx=100, pady=10)

    b2photo = PhotoImage(file=basedir + "/b2.GIF")
    b2photo = b2photo.zoom(9)  # with 250, I ended up running out of memory
    b2photo = b2photo.subsample(10)
    label = Label(topframe, image=b2photo)
    label.image = b2photo  # keep a reference!
    label.grid(row=2, column=2, sticky=NSEW, padx=100, pady=10)

    root.mainloop()


while True:
    main()