import tkinter as tk
from tkinter import ttk

# from Temperatuurinfo import *
# from temperatuurknoppen import *
from .Lijngrafiek import *

class Sensor:
        def __init__(self, _frame, _soort, _bovengrens, _frequentie, _titel, _eenheid):
            # Maak object
            self.frame = _frame
            self.soort = _soort
            self.bovengrens = _bovengrens
            self.frequentie = _frequentie
            self.titel = _titel
            self.eenheid = _eenheid
            self.switch = True
            self.oprollen = True
            self.maakFrame()

        # Frequentie knop functionaliteit
        def frequentieFunc(self):
            try:
                    self.frequentie = self.frequentieVar.get()
            except:
                    print('Ja.... da kan nie he')
            self.frequentielabelVar.set(
                    'De ' + self.soort + ' wordt om de ' + str(self.frequentie) + ' seconden gemeten')

        # Grenswaarde knop functionaliteit
        def grenswaardeFunc(self):
            try:
                    self.bovengrens = self.grenswaardeVar.get()
            except:
                    print('Ja.... da kan nie he')
            self.grenslabelVar.set('De bovengrens is: ' + str(self.bovengrens) + str(self.eenheid))

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

        def maakFrame(self):
            # Creeer containers
            # -----------------------------------------------------------------

            gegevensLabel = tk.Label(text=self.titel + "sensor gegevens", font=('calibri', 16, 'bold'), background='grey91')
            instellingenLabel = tk.Label(text="Instellingen", font=('calibri', 16, 'bold'), background='grey91')
            lijngrafiekLabel = tk.Label(text="Lijngrafiek", font=('calibri', 16, 'bold'), background='grey91')

            self.linksContainer = ttk.Frame(self.frame)
            self.linksContainer.grid(column=0, row=0, padx=8, pady=4, sticky='NW')

            self.rechtsContainer = ttk.Frame(self.frame)
            self.rechtsContainer.grid(column=1, row=0, padx=8, pady=4, sticky='NW')

            self.infoContainer = ttk.LabelFrame(self.linksContainer, labelwidget=gegevensLabel)
            self.infoContainer.grid(column=0, row=0, padx=8, pady=4, sticky='NW')

            self.graphContainer = ttk.LabelFrame(self.rechtsContainer, labelwidget=lijngrafiekLabel)
            self.graphContainer.grid(column=1, row=0, padx=8, pady=4, rowspan=2)

            self.knopContainer = ttk.LabelFrame(self.linksContainer, labelwidget=instellingenLabel)
            self.knopContainer.grid(column=0, row=1, padx=8, pady=100, sticky='N')

            # -----------------------------------------------------------------

            # Infocontainer ------------------------------------
            # Label voor de bovengrenswaarde
            self.grenslabelVar = tk.StringVar()
            self.grenslabelVar.set('De bovengrens is: ' + str(self.bovengrens) + str(self.eenheid))
            ttk.Label(self.infoContainer, textvariable=self.grenslabelVar).grid(column=0, row=1, sticky='W')

            # Label voor de frequentie van het meten
            self.frequentielabelVar = tk.StringVar()
            self.frequentielabelVar.set('De ' + self.soort + ' wordt om de ' + str(self.frequentie) + ' seconden gemeten')
            ttk.Label(self.infoContainer, textvariable=self.frequentielabelVar).grid(column=0, row=2, sticky='W')

            # Label voor handmatig/automatisch switch
            self.switchlabelVar = tk.StringVar()
            self.switchlabelVar.set('Deze besturingseenheid is ingesteld op handmatig')
            ttk.Label(self.infoContainer, textvariable=self.switchlabelVar).grid(column=0, row=3, sticky='W')

            # Label om aan te geven of rolluik is opgerold of niet
            self.oprollabelVar = tk.StringVar()
            self.oprollabelVar.set('De rolluik is nu opgerold')
            ttk.Label(self.infoContainer, textvariable=self.oprollabelVar).grid(column=0, row=4, sticky='W')

            # Knopcontainer ------------------------------------
            # Label voor bovengrens knop
            ttk.Label(self.knopContainer, text="Geef een waarde voor de bovengrens in" + self.eenheid + ":").grid(column=0, row=0, sticky='W')

            # Invulveld voor bovengrenswaarde
            self.grenswaardeVar = tk.IntVar()
            grenswaardeVeld = ttk.Entry(self.knopContainer, width=10, textvariable=self.grenswaardeVar)
            grenswaardeVeld.grid(column=1, row=0)

            # Knop om bovengrens aan te passen
            self.grenswaardeKnop = ttk.Button(self.knopContainer, text="Verander", command=self.grenswaardeFunc)
            self.grenswaardeKnop.grid(column=2, row=0)

            # Label voor frequentie knop
            ttk.Label(self.knopContainer, text="Geef een waarde voor de meetfrequentie in seconden:").grid(column=0, row=1, sticky="W")

            # Invulveld voor frequentie
            self.frequentieVar = tk.IntVar()
            frequentieVeld = ttk.Entry(self.knopContainer, width=10, textvariable=self.frequentieVar)
            frequentieVeld.grid(column=1, row=1)

            # Knop om frequentie aan te passen
            self.frequentieKnop = ttk.Button(self.knopContainer, text="Verander", command=self.frequentieFunc)
            self.frequentieKnop.grid(column=2, row=1)

            # Knop om handmatig en automatisch om te wisselen
            self.switchKnop = ttk.Button(self.knopContainer, text='Verander de instelling naar automatisch', command=self.switchFunc)
            self.switchKnop.grid(column=0, row=4, sticky='W', pady=10)

            # Knoppen om op te rollen of uit te rollen
            self.oprolKnop = ttk.Button(self.knopContainer, text='Oprollen', command=self.oprollenFunc)
            self.uitrolKnop = ttk.Button(self.knopContainer, text='Uitrollen', command=self.uitrollenFunc)
            self.oprolKnop.grid(column=0, row=5, sticky=tk.W, in_=self.knopContainer)
            self.uitrolKnop.grid(column=0, row=6, sticky=tk.W, in_=self.knopContainer)

            self.graphFrame = tk.Frame(self.graphContainer)
            self.graphFrame.grid(column=0, row=0)
            self.grafiek = Lijngrafiek(self.graphFrame)