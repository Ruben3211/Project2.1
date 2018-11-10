import matplotlib
matplotlib.use('TkAgg')
import tkinter as tk
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random


class Lijngrafiek:

    def __init__(self, master):
        graphFrame = tk.Frame(master)
        self.xar = []
        self.yar = []

        self.variabele = None

        self.fig = plt.figure(figsize=(14, 4.5), dpi=100)

        self.ax = self.fig.add_subplot(1,1,1)
        self.ax.set_ylim(0, 70)
        self.ax.grid()
        self.line, = self.ax.plot(self.xar, self.yar)

        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        # self.canvas.show()
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
        graphFrame.pack()

    def animate(self,i):
        # yar.append(99-i)
        self.yar.append(self.variabele)
        self.xar.append(i)
        self.line.set_data(self.xar, self.yar)
        if i < 70:
            self.ax.set_xlim(0, i+10)
        else:
            self.ax.set_xlim(i - 69, i + 10)