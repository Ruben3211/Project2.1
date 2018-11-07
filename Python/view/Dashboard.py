import tkinter as tk
from tkinter import ttk
from tkinter import Menu

import matplotlib
matplotlib.use('TkAgg')
from Temperatuursensor import *
from Lichtsensor import *

# =======================================================================================
class Dashboard:
    def __init__(self):
        # Maak object
        self.win = tk.Tk()

        # Voeg een titel toe
        self.win.title("De Centrale")
        self.createWidgets()

    # Sluit de GUI netjes
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def createWidgets(self):
        # Tab Control  ----------------------------------------------------------------
        tabControl = ttk.Notebook(self.win)  # Creeer tab control

        tab1 = ttk.Frame(tabControl)  # Creeer een tab
        tabControl.add(tab1, text='Rolluik 1')  # Voeg de tab toe

        tab2 = ttk.Frame(tabControl)  # Creeer een tweede tab
        tabControl.add(tab2, text='Rolluik 2')  # Voeg de tweede tab toe

        tabControl.pack(expand=1, fill="both")  # Pack om zichtbaar te maken
        # ~ Tab 1  --------------------------------------------------------------------
        self.temperatuursensor = Temperatuursensor(tab1)

        # Tab 2  ----------------------------------------------------------------------
        self.lichtsensor = Lichtsensor(tab2)

        # Creeer de menu bar
        menuBar = Menu(tab1)
        self.win.config(menu=menuBar)

        # Voeg menu items toe
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="New")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self._quit)
        menuBar.add_cascade(label="File", menu=fileMenu)

        # Voeg een menu aan het menu bar toe en creeer nog een item
        helpMenu = Menu(menuBar, tearoff=0)
        helpMenu.add_command(label="About")
        menuBar.add_cascade(label="Help", menu=helpMenu)


# ======================
# Start GUI
# ======================

oop = Dashboard()

grafiek1 = animation.FuncAnimation(oop.temperatuursensor.grafiek.fig, oop.temperatuursensor.grafiek.animate, interval=1000, blit=False)
grafiek2 = animation.FuncAnimation(oop.lichtsensor.grafiek.fig, oop.lichtsensor.grafiek.animate, interval=1000, blit=False)
oop.win.mainloop()
