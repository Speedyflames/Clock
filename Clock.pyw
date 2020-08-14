from tkinter import *
from datetime import datetime
from threading import Timer


class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master

        self.create()

    def create(self):
        global time
        global t
        
        self.master.title("Clock")
        self.pack(fill = BOTH, expand = 1)

        time = StringVar()
        t = Label(self, textvariable=time, font=("Verdana", 22), justify=CENTER)
        t.pack()

        self.clock()

    def clock(self):
        now = datetime.now()
        midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
        secs = (now - midnight).seconds
        
        percent = str(round((secs/864), 2)) + "%"
        time.set(percent)

        c = Timer(1, self.clock)
        c.setDaemon(True)
        c.start()


root = Tk()
root.geometry("200x45")

app = Window(root)

root.mainloop()
