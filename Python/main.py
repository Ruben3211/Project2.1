# importeer hier alle mappen en andere dingen die nodig zijn
from model.eenheid import eenheid
from controller import *
from controller.meet_controller import meetController
from tkinter import *
import matplotlib.animation as animation


class main(Tk):
    def __init__(self):
        super().__init__()
        self.title("jelambo")
        self.meter = meetController(self)


    def restart(self):
        self.title('jelambo')


run = main()
grafiek1 = animation.FuncAnimation(run.meter.dashboard.temperatuursensor.grafiek.fig, run.meter.dashboard.temperatuursensor.grafiek.animate, interval=5000, blit=False)
grafiek2 = animation.FuncAnimation(run.meter.dashboard.lichtsensor.grafiek.fig, run.meter.dashboard.lichtsensor.grafiek.animate, interval=5000, blit=False)
run.meter.dashboard.win.mainloop()