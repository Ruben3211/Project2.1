import tkinter as tk
from tkinter import ttk
from tkinter import Menu

#===================================================================
class centrale():
    def __init__(self):
        # Maak object
        self.win = tk.Tk()

        # Voeg een titel toe
        self.win.title("De Centrale")
        self.createWidgets()

    # Knop actie
    def clickMe(self):
        self.action.configure(text='Hello ' + self.name.get())

    # Sluit de GUI
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    #####################################################################################
    def createWidgets(self):
        # Tab Control  --------------------------------------
        tabControl = ttk.Notebook(self.win)     # Creeer tab control

        tab1 = ttk.Frame(tabControl)            # Creeer een tab
        tabControl.add(tab1, text='Rolluik 1')      # Voeg een tab toe

        tab2 = ttk.Frame(tabControl)            # Creeer een tweede tab
        tabControl.add(tab2, text='Rolluik 2')      # Maak de tweede tab zichtbaar

        tabControl.pack(expand=1, fill="both")  # Pack om zichtbaar te maken
        # ~ Tab Control  -------------------------------------

        # Creeer een container frame waar alle andere widgets inkomen
        self.container = ttk.LabelFrame(tab1, text=' Temperatuursensor ')
        self.container.grid(column=0, row=0, padx=8, pady=4)

        # Verander het label
        ttk.Label(self.container, text="Geef een waarde:").grid(column=0, row=0, sticky='W')

        # Maak een invulveld widget
        self.name = tk.StringVar()
        nameEntered = ttk.Entry(self.container, width=12, textvariable=self.name)
        nameEntered.grid(column=0, row=1, sticky='W')

        # Maak een knopje
        self.action = ttk.Button(self.container, text="Klik mij!", command=self.clickMe)
        self.action.grid(column=2, row=1)

        ttk.Label(self.container, text="Test label").grid(column=1, row=1)

        # Tab Control 2  -----------------------------------------
        # Creeer een container frame waar alle andere widgets inkomen -- Tab2
        self.container2 = ttk.LabelFrame(tab2, text=' Lichtsensor ')
        self.container2.grid(column=0, row=0, padx=8, pady=4)

        # Creeer een label die test labels vasthoudt
        labelsFrame = ttk.LabelFrame(self.container2, text=' Labels in een frame test ')
        labelsFrame.grid(column=0, row=7)

        # Plaats labels in containter - verticaal
        ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
        ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)

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
        nameEntered.focus()

#======================
# Start GUI
#======================
oop = centrale()
oop.win.mainloop()
