import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
import matplotlib.animation as animation
from matplotlib import style


matplotlib.use("TkAgg")
readings = []


HEADER1 = ("Verdana", 18)
HEADER2 = ("Verdana", 10)
style.use("ggplot")

#dictionary key = gesture name , value = readings in millivolt
gestures={}

gestures['fist'] = [1,2,3,4,5,6,7,8]
gestures['release'] = [1,2,3,4,5,6,7,8]

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)


def animate(i):
    pullData = open("readings", "r").read()
    dataList = pullData.split('\n')
    xList=[]
    yList=[]

    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))

    global readings
    readings = yList

    a.clear()
    a.plot(xList,yList)


class MyoArm(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self,*args,**kwargs)
        tk.Tk.wm_title(self , "Myo Arm")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, DemoPage, AddGesturePage):
            frame = F(container , self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self , cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Myo Arm", font=HEADER1)
        label.pack(pady=10, padx=10)

        TEXT = "Detect and predict hand gestures using Myo Armband"

        text = tk.Label(self, text=TEXT, font=HEADER1)
        text.pack()

        button1 = tk.Button(self, text="Get Started",
                            command=lambda : controller.show_frame(PageOne))
        button1.pack()


class DemoPage(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Demo Page", font=HEADER1)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back",
                            command=lambda : controller.show_frame(PageOne))
        button1.pack()

        LeftFrame = tk.Frame(self)
        LeftFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, anchor=tk.N)

        canvas = FigureCanvasTkAgg(f, LeftFrame)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


        RightFrame = tk.Frame(self)
        RightFrame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1, anchor=tk.N)

        heading = tk.Label(RightFrame, text='Readings', font=HEADER2)
        heading.pack()


        entry_1 = tk.Text(RightFrame, height=2, width=10)
        entry_2 = tk.Text(RightFrame, height=2, width=10)
        entry_3 = tk.Text(RightFrame, height=2, width=10)
        entry_4 = tk.Text(RightFrame, height=2, width=10)
        entry_5 = tk.Text(RightFrame, height=2, width=10)
        entry_6 = tk.Text(RightFrame, height=2, width=10)
        entry_7 = tk.Text(RightFrame, height=2, width=10)
        entry_8 = tk.Text(RightFrame, height=2, width=10)

        entry_1.pack()
        entry_2.pack()
        entry_3.pack()
        entry_4.pack()
        entry_5.pack()
        entry_6.pack()
        entry_7.pack()
        entry_8.pack()




class AddGesturePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Add Gesture", font=HEADER1)
        label.grid(pady=10, padx=10)

        tag = tk.Label(self, text="Current Gestures", font=HEADER2)
        tag.grid(row=1)

        for i , name in enumerate(gestures):
            name_label = tk.Label(self, text=name, font=HEADER2)
            name_label.grid(row=i+2)


        button1 = tk.Button(self, text="Back",
                            command=lambda : controller.show_frame(PageOne))
        button1.grid()


class PageOne(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Welcome to Myo Arm", font=HEADER1)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Demo",
                            command=lambda : controller.show_frame(DemoPage))
        button1.pack()

        button2 = ttk.Button(self, text="Add Gesture",
                            command=lambda : controller.show_frame(AddGesturePage))
        button2.pack()

        button3 = ttk.Button(self, text="Home",
                            command=lambda : controller.show_frame(StartPage))
        button3.pack()

        # testButton = ttk.Button(self, text="test",
        #                     command=lambda : controller.show_frame(TestPage))
        # testButton.pack()



myapp = MyoArm()

ani = animation.FuncAnimation(f, animate, interval=1000)

myapp.mainloop()