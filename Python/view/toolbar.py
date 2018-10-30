import tkinter as tk
from tkinter import ttk


class App(ttk.Frame):
    """ main class for the application """
    def __init__(self,master,*args,**kwargs):
        super().__init__(master,*args,**kwargs)


        self.my_toolbar = Toolbar(self)

        self.my_statusbar = StatusBar(self)
        self.my_statusbar.set("This is the statusbar")

        self.centerframe = CenterFrame(self)

        self.pack(side=tk.TOP, expand=True, fill=tk.BOTH)


    def button_function(self, *event):
        print("filter")


class CenterFrame(ttk.Frame):

    def __init__(self,master,*args,**kwargs):
        super().__init__(master,*args,**kwargs)
        self.master = master
        self.pack(side=tk.BOTTOM, fill=tk.X)
        self.centerlabel = ttk.Label(self, text="Center stuff goes here")
        self.centerlabel.pack()


class StatusBar(ttk.Frame):
    """ Simple Status Bar class - based on Frame """
    def __init__(self,master):
        ttk.Frame.__init__(self,master)
        self.master = master
        self.label = ttk.Label(self,anchor=tk.W)
        self.label.pack()
        self.pack(side=tk.BOTTOM, fill=tk.X)

    def set(self,texto):
        self.label.config(text=texto)
        self.label.update_idletasks()
    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()


class Toolbar(ttk.Frame):
    """ Toolbar """
    def button_one(self):
        print("button 1 pressed")

    def button_two(self):
        print("button 2 pressed")
        self.master.button_function()

    def __init__(self,master):
        super().__init__(master)
        self.master = master
        self.pack(side=tk.TOP, fill=tk.X)
        self.button1 = ttk.Button(self,text="One",command=self.button_one)
        self.button2 = ttk.Button(self,text="Two",command=self.button_two)
        self.button1.grid(row=0,column=0)
        self.button2.grid(row=0,column=1)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()