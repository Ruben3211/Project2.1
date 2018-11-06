import tkinter as tk
from tkinter import ttk
from tkinter import Menu

import matplotlib

matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
from threading import Thread

# =======================================================================================
class Centrale:
    def __init__(self):
        # Maak object
        self.win = tk.Tk()
        self.bovengrens = 20
        self.switch = True
        self.oprollen = True
        self.frequentie = 10

        # Voeg een titel toe
        self.win.title("De Centrale")
        self.createWidgets()

    # Grenswaarde knop functionaliteit
    def grenswaardeFunc(self):
        try:
            self.bovengrens = self.grenswaardeVar.get()
        except:
            print('Ja.... da kan nie he')
        self.grenslabelVar.set('De bovengrens is: ' + str(self.bovengrens) + ' graden celsius')
        # self.createThread()

    # Switch knop functionaliteit
    def switchFunc(self):
        if self.switch == True:
            self.switch = False
            self.switchlabelVar.set('Deze besturingseenheid is ingesteld op handmatig')
            self.switchKnop.configure(text='Verander de instelling naar automatisch')
            self.oprolKnop.grid(column=0, row=5, sticky=tk.W, in_=self.knopContainer)
            self.uitrolKnop.grid(column=0, row=6, sticky=tk.W, in_=self.knopContainer)
        else:
            self.switch = True
            self.switchlabelVar.set('Deze besturingseenheid is ingesteld op automatisch')
            self.switchKnop.configure(text='Verander de instelling naar handmatig')
            self.oprolKnop.grid_forget()
            self.uitrolKnop.grid_forget()


    # Oprol knop functionaliteit
    def oprollenFunc(self):
        self.oprollen = True
        self.oprollabelVar.set('De rolluik is nu opgerold')

    # Uitrol knop functionaliteit
    def uitrollenFunc(self):
        self.oprollen = False
        self.oprollabelVar.set('De rolluik is nu uitgerold')

    # Creeer thread voor de lijngrafiek
    def createThread(self):
        self.runT = Thread(target=self.grafiek.runGraph())
        self.runT.setDaemon(True)
        self.runT.start()
        print(self.runT)
        print('createThread():', self.runT.isAlive())

    # Sluit de GUI
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    #####################################################################################
    def createWidgets(self):
        # Tab Control  ----------------------------------------------------------------
        tabControl = ttk.Notebook(self.win)  # Creeer tab control

        tab1 = ttk.Frame(tabControl)  # Creeer een tab
        tabControl.add(tab1, text='Rolluik 1')  # Voeg een tab toe

        tab2 = ttk.Frame(tabControl)  # Creeer een tweede tab
        tabControl.add(tab2, text='Rolluik 2')  # Voeg de tweede tab toe

        tabControl.pack(expand=1, fill="both")  # Pack om zichtbaar te maken
        # ~ Tab 1  ---------------------------------------------------------------------

        # Creeer containers
        # -----------------------------------------------------------------

        gegevens = tk.Label(text="Temperatuursensor gegevens", font=('calibri', 16, 'bold'), background='grey91')
        instellingen = tk.Label(text="Instellingen", font=('calibri', 16, 'bold'), background='grey91')
        lijngrafiek = tk.Label(text="Lijngrafiek", font=('calibri', 16, 'bold'), background='grey91')

        self.linksContainer = ttk.Frame(tab1)
        self.linksContainer.grid(column=0, row=0, padx=8, pady=4, sticky='NW')

        self.rechtsContainer = ttk.Frame(tab1)
        self.rechtsContainer.grid(column=1, row=0, padx=8, pady=4, sticky='NW')

        self.infoContainer = ttk.LabelFrame(self.linksContainer, labelwidget=gegevens)
        self.infoContainer.grid(column=0, row=0, padx=8, pady=4, sticky='NW')

        self.graphContainer = ttk.LabelFrame(self.rechtsContainer, labelwidget=lijngrafiek)
        self.graphContainer.grid(column=1, row=0, padx=8, pady=4, rowspan=2)

        self.knopContainer = ttk.LabelFrame(self.linksContainer, labelwidget=instellingen)
        self.knopContainer.grid(column=0, row=1, padx=8, pady=100, sticky='N')

        # -----------------------------------------------------------------

        # Infocontainer ------------------------------------
        # Label voor de bovengrenswaarde
        self.grenslabelVar = tk.StringVar()
        self.grenslabelVar.set('De bovengrens is: ' + str(self.bovengrens) + ' graden celsius')
        ttk.Label(self.infoContainer, textvariable=self.grenslabelVar).grid(column=0, row=1, sticky='W')

        # Label voor handmatig/automatisch switch
        self.switchlabelVar = tk.StringVar()
        self.switchlabelVar.set('Deze besturingseenheid is ingesteld op handmatig')
        ttk.Label(self.infoContainer, textvariable=self.switchlabelVar).grid(column=0, row=2, sticky='W')

        # Label voor handmatig/automatisch switch
        self.oprollabelVar = tk.StringVar()
        self.oprollabelVar.set('De rolluik is nu opgerold')
        ttk.Label(self.infoContainer, textvariable=self.oprollabelVar).grid(column=0, row=3, sticky='W')

        # Knopcontainer ------------------------------------
        # Label voor bovengrens knop
        ttk.Label(self.knopContainer, text="Geef een waarde voor de bovengrens in graden celsius:").grid(column=0, row=0)

        # Maak een invulveld widget
        self.grenswaardeVar = tk.IntVar()
        grenswaardeVeld = ttk.Entry(self.knopContainer, width=10, textvariable=self.grenswaardeVar)
        grenswaardeVeld.grid(column=1, row=0)

        # Knop om bovengrens aan te passen
        self.grenswaardeKnop = ttk.Button(self.knopContainer, text="Verander", command=self.grenswaardeFunc)
        self.grenswaardeKnop.grid(column=2, row=0)

        # Knop om handmatig en automatisch om te wisselen
        self.switchKnop = ttk.Button(self.knopContainer, width=28, text='Verander de instelling naar automatisch', command=self.switchFunc)
        self.switchKnop.grid(column=0, row=4, sticky='W', pady=10)

        # Knoppen om op te rollen of uit te rollen
        self.oprolKnop = ttk.Button(self.knopContainer, text='Oprollen', command=self.oprollenFunc)
        self.uitrolKnop = ttk.Button(self.knopContainer, text='Uitrollen', command=self.uitrollenFunc)
        self.oprolKnop.grid(column=0, row=5, sticky=tk.W, in_=self.knopContainer)
        self.uitrolKnop.grid(column=0, row=6, sticky=tk.W, in_=self.knopContainer)

        # Tab 2  ------------------------------------------------------------------------
        # Creeer een container frame waar alle andere widgets inkomen -- Tab2
        self.container2 = ttk.LabelFrame(tab2, text=' Lichtsensor ')
        self.container2.grid(column=0, row=0, padx=8, pady=4)

        # Creeer een label die test labels vasthoudt
        labelsFrame = ttk.LabelFrame(self.container2, text=' Labels in een frame test ')
        labelsFrame.grid(column=0, row=7)

        # ===================================================

        graphFrame = tk.Frame(self.graphContainer)
        graphFrame.grid(column=0, row=0)
        self.grafiek = Lijngrafiek(graphFrame)

        # ===================================================

        # Creeer wat ruimte om de labels
        for child in labelsFrame.winfo_children():
            child.grid_configure(padx=18)

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

        # Plaats cursor in invulveld
        grenswaardeVeld.focus()


class Lijngrafiek:

    def __init__(self, master):
        graphFrame = tk.Frame(master)
        self.xar = []
        self.yar = []

        self.fig = plt.figure(figsize=(12, 6), dpi=100)

        self.ax = self.fig.add_subplot(1, 1, 1)
        self.ax.set_ylim(0, 10)
        self.ax.grid()
        self.line, = self.ax.plot(self.xar, self.yar)

        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        # self.canvas.show()
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
        graphFrame.pack()

    def animate(self, i):
        while True:
            # yar.append(99-i)
            self.yar.append(random.randint(0, 10))
            self.xar.append(i)
            self.line.set_data(self.xar, self.yar)
            self.ax.set_xlim(0, i + 1)

    # Lijngrafiek runner
    def runGraph(self):
        animation.FuncAnimation(self.fig, self.animate, interval=100, blit=False)


# ======================
# Start GUI
# ======================
oop = Centrale()
oop.win.mainloop()
=======
import tkinter as tk
from tkinter import ttk
from tkinter import Menu

import matplotlib

matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
from threading import Thread


# =======================================================================================
class Centrale:
    def __init__(self):
        # Maak object
        self.win = tk.Tk()
        self.bovengrens = 20
        self.switch = True
        self.oprollen = True

        # Voeg een titel toe
        self.win.title("De Centrale")
        self.createWidgets()

    # Grenswaarde knop functionaliteit
    def grenswaardeFunc(self):
        try:
            self.bovengrens = self.grenswaardeVar.get()
        except:
            print('Ja.... da kan nie he')
        self.labelVar.set('De bovengrens is: ' + str(self.bovengrens) + ' graden celsius')
        # self.createThread()

    # Switch knop functionaliteit
    def switchFunc(self):
        if self.switch == True:
            self.switch = False
            self.switchKnop.configure(text='Handmatig')
            self.radio1.grid(column=0, row=5, sticky=tk.W, in_=self.container)
            self.radio2.grid(column=0, row=6, sticky=tk.W, in_=self.container)
        else:
            self.switch = True
            self.switchKnop.configure(text='Automatisch')
            self.radio1.grid_forget()
            self.radio2.grid_forget()


    # Radiobuttons functionaliteit
    def radioFunc(self):
        radSel = self.radioVar.get()
        if radSel == 0:
            self.oprollen = True
        elif radSel == 1:
            self.oprollen = False

    # Creeer thread voor de lijngrafiek
    def createThread(self):
        self.runT = Thread(target=self.grafiek.runGraph())
        self.runT.setDaemon(True)
        self.runT.start()
        print(self.runT)
        print('createThread():', self.runT.isAlive())

    # Sluit de GUI
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    #####################################################################################
    def createWidgets(self):
        # Tab Control  -----------------------------------------------------------------
        tabControl = ttk.Notebook(self.win)  # Creeer tab control

        tab1 = ttk.Frame(tabControl)  # Creeer een tab
        tabControl.add(tab1, text='Rolluik 1')  # Voeg een tab toe

        tab2 = ttk.Frame(tabControl)  # Creeer een tweede tab
        tabControl.add(tab2, text='Rolluik 2')  # Voeg de tweede tab toe

        tabControl.pack(expand=1, fill="both")  # Pack om zichtbaar te maken
        # ~ Tab 1  ---------------------------------------------------------------------

        # Creeer een container frame waar alle andere widgets inkomen
        self.container = ttk.LabelFrame(tab1, text=' Temperatuursensor ')
        self.container.grid(column=0, row=0, padx=8, pady=4)

        # Voeg een label toe
        ttk.Label(self.container, text="Geef een waarde voor de bovengrens in graden celsius:").grid(column=0, row=0)

        # Maak een invulveld widget
        self.grenswaardeVar = tk.IntVar()
        grenswaardeVeld = ttk.Entry(self.container, width=10, textvariable=self.grenswaardeVar)
        grenswaardeVeld.grid(column=1, row=0)

        # Knop om bovengrens aan te passen
        self.grenswaardeKnop = ttk.Button(self.container, text="Verander", command=self.grenswaardeFunc)
        self.grenswaardeKnop.grid(column=2, row=0)

        # Knop om handmatig en automatisch om te wisselen
        self.switchKnop = ttk.Button(self.container, width=12, text='Handmatig', command=self.switchFunc)
        self.switchKnop.grid(column=0, row=4, sticky='W', pady=40)

        # Label voor de bovengrenswaarde
        self.labelVar = tk.StringVar()
        self.labelVar.set('De bovengrens is: ' + str(self.bovengrens) + ' graden celsius')
        self.labeltje2 = ttk.Label(self.container, textvariable=self.labelVar).grid(column=0, row=1, sticky='W')

        self.radioVar = tk.IntVar()
        self.radio1 = tk.Radiobutton(self.container, background='grey91', text='Oprollen', variable=self.radioVar, value=0, command=self.radioFunc)
        self.radio2 = tk.Radiobutton(self.container, background='grey91', text='Uitrollen', variable=self.radioVar, value=1, command=self.radioFunc)
        self.radio1.grid(column=0, row=5, sticky=tk.W, in_=self.container)
        self.radio2.grid(column=0, row=6, sticky=tk.W, in_=self.container)

        # Tab 2  ------------------------------------------------------------------------
        # Creeer een container frame waar alle andere widgets inkomen -- Tab2
        self.container2 = ttk.LabelFrame(tab2, text=' Lichtsensor ')
        self.container2.grid(column=0, row=0, padx=8, pady=4)

        # Creeer een label die test labels vasthoudt
        labelsFrame = ttk.LabelFrame(self.container2, text=' Labels in een frame test ')
        labelsFrame.grid(column=0, row=7)

        # Plaats labels in containter - verticaal
        # ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
        # ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)

        # =======================================================================================

        graphFrame = tk.Frame(self.container)
        graphFrame.grid(column=4, row=10, padx=100)
        self.grafiek = Lijngrafiek(graphFrame)

        # =======================================================================================

        # Creeer wat ruimte om de labels
        for child in labelsFrame.winfo_children():
            child.grid_configure(padx=18)

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

        # Plaats cursor in invulveld
        grenswaardeVeld.focus()


class Lijngrafiek:

    def __init__(self, master):
        graphFrame = tk.Frame(master)
        self.xar = []
        self.yar = []

        self.fig = plt.figure(figsize=(12, 6), dpi=100)

        self.ax = self.fig.add_subplot(1, 1, 1)
        self.ax.set_ylim(0, 10)
        self.ax.grid()
        self.line, = self.ax.plot(self.xar, self.yar)

        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        # self.canvas.show()
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
        graphFrame.pack()

    def animate(self, i):
        while True:
            # yar.append(99-i)
            self.yar.append(random.randint(0, 10))
            self.xar.append(i)
            self.line.set_data(self.xar, self.yar)
            self.ax.set_xlim(0, i + 1)

    # Lijngrafiek runner
    def runGraph(self):
        animation.FuncAnimation(self.fig, self.animate, interval=100, blit=False)


# ======================
# Start GUI
# ======================
oop = Centrale()
oop.win.mainloop()