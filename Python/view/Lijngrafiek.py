"""
In de klasse Lijngrafiek wordt de graphFrame aangemaakt voor de lijngrafiek die wij gebruiken per eenheid.

Created: 05-11-2018
Author: Jeloambo
Version: 1.2
"""


import matplotlib
import tkinter as tk
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')


class Lijngrafiek:

    def __init__(self, master):
        """
        :initialiseren van all klas variabelen.
        :param graphFrame: wordt een nieuw Frame aangemaakt.
        :param xar: is een lege list voor de x-as.
        :param yar: is een lege list voor de y-as.
        :param variabele: is een lege variabele.
        :param fig: maakt een figure aan met de grote en dpi voor het figuur.
        :param ax: maakt een subplot aan voor het figuur.
        :param line: maakt een plot aan met de xar en yar lists
        :param canvas: maakt een nieuw canvas aan.
        """
        graphFrame = tk.Frame(master)
        self.xar = []
        self.yar = []
        self.variabele = None
        self.fig = plt.figure(figsize=(14, 4.5), dpi=100)
        self.ax = self.fig.add_subplot(1,1,1)
        self.ax.set_ylim(0, 70) # zet de y-as waarden van 0 tot 70
        self.ax.grid() # Maakt de grid aan voor de ax parameter
        self.line, = self.ax.plot(self.xar, self.yar)
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1) # Zet de positie van de lijngrafiek
        graphFrame.pack() # voer de graphFrame uit

    # Hier voert hij de animatie van de lijngrafiek uit.
    def animate(self,i):
        self.yar.append(self.variabele) # voegt een nieuwe variabele toe aan de yar list
        self.xar.append(i) # voegt een nieuwe variabele toe aan de xar list
        self.line.set_data(self.xar, self.yar) # zet de data voor de x- en y-as
        if i < 70:
            self.ax.set_xlim(0, i+10) # zet de nieuwe waarde voor de x-as
        else:
            self.ax.set_xlim(i - 69, i + 10) # zet de nieuwe waarde voor de x-as
