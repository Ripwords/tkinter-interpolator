from os import path
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

title = "Interpolation"
WIDTH = 600
HEIGHT = 300
iconPath = path.abspath(path.join(path.dirname(__file__), "pic.ico"))
imagePath = path.abspath(path.join(path.dirname(__file__), "equation.png"))

textFont = ("SF PRO", 35)
entryFont = ("SF PRO DISPLAY", 12)

class tkMain(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.pack(
            side = "top",
            fill = "both",
            expand = True,
        )
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for page in (main, page_1):
            frame = page(container, self)

            self.frames[page] = frame

            frame.grid(
                row = 0,
                column = 0,
                sticky = "nsew"
            )
    
        self.show(main)
    
    def show(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class main(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = ttk.Label(
            self,
            text = "Interpolation",
            font = textFont
        )

        label.place(
            relx = 0.5,
            rely = 0.05,
            relheight = 0.25,
            anchor = "n"
        )
        
        image = Image.open(imagePath) 
        imW, imH = image.size
        image = image.resize((imW//2, imH//2), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        imageLabel = Label(self, image = image)
        imageLabel.image = image
        imageLabel.place(
            relx = 0.5,
            rely = 0.25,
            anchor = "n"
        )

        labelx1 = Label(
            self,
            text = "x1 =",
            font = ("verdana", 14)
        )

        labelx1.place(
            relx = 0.17,
            rely = 0.5,
            relwidth = 0.1,
            relheight = 0.1
        )

        labelx2 = Label(
            self,
            text = "x2 =",
            font = ("verdana", 14)
        )

        labelx2.place(
            relx = 0.17,
            rely = 0.62,
            relwidth = 0.1,
            relheight = 0.1
        )

        labely1 = Label(
            self,
            text = "y1 =",
            font = ("verdana", 14)
        )

        labely1.place(
            relx = 0.37,
            rely = 0.5,
            relwidth = 0.1,
            relheight = 0.1
        )

        labely2 = Label(
            self,
            text = "y2 =",
            font = ("verdana", 14)
        )

        labely2.place(
            relx = 0.37,
            rely = 0.62,
            relwidth = 0.1,
            relheight = 0.1
        )

        labelx = Label(
            self,
            text = " x =",
            font = ("verdana", 14)
        )

        labelx.place(
            relx = 0.57,
            rely = 0.5,
            relwidth = 0.1,
            relheight = 0.1
        )

        x1 = Entry(
            self,
            validate="key",
            font = entryFont
        )
        x1.place(
            relwidth = 0.1,
            relheight = 0.1,
            relx = 0.27,
            rely = 0.5
        )

        x2 = Entry(
            self,
            validate="key",
            font = entryFont
        )
        x2.place(
            relwidth = 0.1,
            relheight = 0.1,
            relx = 0.27,
            rely = 0.62
        )

        y1 = Entry(
            self,
            validate="key",
            font = entryFont
        )
        y1.place(
            relwidth = 0.1,
            relheight = 0.1,
            relx = 0.47,
            rely = 0.5
        )

        y2 = Entry(
            self,
            validate="key",
            font = entryFont
        )
        y2.place(
            relwidth = 0.1,
            relheight = 0.1,
            relx = 0.47,
            rely = 0.62
        )

        x = Entry(
            self,
            validate="key",
            font = entryFont
        )
        x.place(
            relwidth = 0.1,
            relheight = 0.1,
            relx = 0.67,
            rely = 0.5
        )

        button1 = Button(
            self,
            text = "Enter",
            command = lambda : clicked(controller, x1.get(), x2.get(), y1.get(), y2.get(), x.get())
        )
        button1.place(
            relx = 0.85,
            rely = 0.85,
            relheight = 0.1,
            relwidth = 0.1
        )

        clear = Button(
            self,
            text = "Clear",
            command = lambda : clear_text(),
            font = entryFont
        )
        clear.place(
            relx = 0.05,
            rely = 0.85,
            relwidth = 0.1,
            relheight = 0.1
        )

        self.resultString = StringVar()

        def clear_text():
            x1.delete(0, END)
            x2.delete(0, END)
            y1.delete(0, END)
            y2.delete(0, END)
            x.delete(0, END)

        def clicked(controller, x1, x2, y1, y2, x):
            results = float(y1) + (float(x) - float(x1)) * ((float(y2) - float(y1))/(float(x2) - float(x1)))
            self.resultString.set(f"{round(results, 5)}")
            controller.frames[page_1].label = Label(
                controller.frames[page_1], 
                font = textFont, 
                textvariable = self.resultString
            ).place(
                relx = 0.5,
                rely = 0.25,
                relheight = 0.5,
                anchor = "n"
            )
            controller.show(page_1)

        def func1(event):
            clicked(controller, x1.get(), x2.get(), y1.get(), y2.get(), x.get())

        def func2(event):
            clear_text()
        
        controller.bind('<Return>', func1)
        controller.bind('<c>', func2)
        controller.bind('<Escape>', func2)

        x1["validatecommand"] = (x1.register(self.onValidate), '%P', '%d')
        x2["validatecommand"] = (x2.register(self.onValidate), '%P', '%d')
        y1["validatecommand"] = (y1.register(self.onValidate), '%P', '%d')
        y2["validatecommand"] = (y2.register(self.onValidate), '%P', '%d')
        x["validatecommand"] = (x.register(self.onValidate), '%P', '%d')

    def onValidate(self, val, dType): #%d = type of action (1=insert, 0=delete, -1=others)
            return (dType == '1' and (val.isdigit() or '.' in val)) or dType == '0'


class page_1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)


        button1 = ttk.Button(
            self,
            text = "Go Back",
            command = lambda : clicked(controller)
        )
        button1.place(
            relx = 0.85,
            rely = 0.85,
            relheight = 0.1,
            relwidth = 0.1
        )

        def clicked(controller):
            controller.frames[main].resultString.set('')
            controller.show(main)

        def func(event):
            clicked(controller)
        
        controller.bind('b', func)

        
app = tkMain()
app.geometry(f"{WIDTH}x{HEIGHT}")
app.title(title)
app.iconbitmap(iconPath)
app.mainloop()