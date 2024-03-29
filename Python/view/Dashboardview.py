"""
In de klasse Dashboardview maakt een nieuwe master(tk) aan.
Hierin worden vensters van de eenheden aangemaakt voor het dashboard.

Created: 07-11-2018
Author: Jeloambo
Version: 1.0
"""

from .Temperatuursensor import *
from .Lichtsensor import *
from tkinter import ttk
from tkinter import Menu
import matplotlib
matplotlib.use('TkAgg')


class Dashboardview:
    def __init__(self, master):
        """
        :initialiseren van all klas variabelen
        :param win: wordt de master aangemaakt(tk).

        win.title("De Centrale") zet de titel van het venster als De Centrale.
        createWidgets() maakt de frames aan.
        """
        self.win = master
        self.win.title("De Centrale")
        self.createWidgets()

    # Sluit de GUI netjes
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    # Maakt alle vensters aan
    def createWidgets(self):
        tabControl = ttk.Notebook(self.win)  # Creeer tab control

        tab1 = ttk.Frame(tabControl)  # Creeer een tab
        tabControl.add(tab1, text='Rolluik 1')  # Voeg de tab toe

        tab2 = ttk.Frame(tabControl)  # Creeer een tweede tab
        tabControl.add(tab2, text='Rolluik 2')  # Voeg de tweede tab toe

        tabControl.pack(expand=1, fill="both")  # Pack om zichtbaar te maken

        # Maakt een tab aan voor de temperatuursensor
        self.temperatuursensor = Temperatuursensor(tab1)

        # Maakt een tab aan voor de lichtsensor
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
