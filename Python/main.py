# importeer hier alle mappen en andere dingen die nodig zijn
from model.eenheid import eenheid
from controller import *
from controller.Dashboardcontroller import Dashboardcontroller
from tkinter import *
import matplotlib.animation as animation


class main(Tk):
    def __init__(self):
        super().__init__()
        self.title("jelambo")
        self.controller = Dashboardcontroller(self)


    def restart(self):
        self.title('jelambo')


run = main()
grafiek1 = animation.FuncAnimation(run.controller.meter.dashboard.temperatuursensor.grafiek.fig, run.controller.meter.dashboard.temperatuursensor.grafiek.animate, interval=1000, blit=False)
grafiek2 = animation.FuncAnimation(run.controller.meter.dashboard.lichtsensor.grafiek.fig, run.controller.meter.dashboard.lichtsensor.grafiek.animate, interval=1000, blit=False)
run.controller.meter.dashboard.win.mainloop()