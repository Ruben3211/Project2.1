import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import random
import time



class DynamicUpdate():
    # Begin afstand van de grafiek
    min_x = 0
    max_x = 60
    plt.ion()

    # Tekent de grafiek
    def setup(self):
            # Maak een plot aan
            self.figure, self.ax = plt.subplots()
            self.lines, = self.ax.plot([],[], 'b-') # Grote van het venster en het soort grafiek b- voor lijn

            # Autoscaler voor de punten die hij nog niet heeft doorgekregen
            self.ax.set_autoscaley_on(True) # Autoscale is waar
            self.ax.set_xlim(self.min_x, self.max_x) # Minimale en maximale waarden van x-as worden geset
            self.ax.grid() # Hiermee zet je een standaard raster voor de grafiek


    def bezig(self, xdata, ydata):
        # Update de grafiek met de nieuwe en oude gegevens
        self.lines.set_xdata(xdata)
        self.lines.set_ydata(ydata)

        # Rescalen van de grafiek
        self.ax.relim()
        self.ax.autoscale_view()

        # Haalt de grafiek weg en tekent hem daarna weer(update)
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    # Main van tekenen grafiek
    def __call__(self):

        # Tekent het begin van de grafiek
        self.setup()

        # Maak 2 arrays aan voor de x- en y-as
        xdata = []
        ydata = []

        # @Param voor oneindige loop
        a = 0

        # @param voor de x-as
        x = 0

        # @param voor het meegaan van de grafiek
        max_b = 0

        while a == 0:

            # Random int voor de verschillende data(moet vervangen worden door de temperatuur)
            y = random.randint(0, 10)

            # Voegt x toe aan de xdata array en voegt y toe aan de ydata array
            xdata.append(x)
            ydata.append(y)

            # Stuurt begin data door naar bezig
            self.bezig(xdata, ydata)

            # Zet de beginwaarden voor de x-as
            self.ax.set_xlim(self.min_x, self.max_x)

            # If statement voor het meegaan in de grafiek
            if(max_b >= 35):
                self.min_x += 1
                self.max_x += 1

            # Pauze van een seconde
            time.sleep(0.25)
            max_b += 1
            x += 1

        return xdata, ydata

d = DynamicUpdate()
d()