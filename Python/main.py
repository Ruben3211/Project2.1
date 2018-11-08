# importeer hier alle mappen en andere dingen die nodig zijn
from model.eenheid import eenheid
from controller import *
from controller.Dashboardcontroller import Dashboardcontroller
from tkinter import *
import matplotlib.animation as animation
from controller.meet_controller import meetController


class main(Tk):
    def __init__(self):
        super().__init__()
        self.title("jelambo")
        self.controller = Dashboardcontroller(self)
        self.meter = meetController()
        self.ga_lopen()

    def ga_lopen(self):
        while True:
            self.meter.sla_waarde_op()

    def restart(self):
        self.title('jelambo')


run = main()
grafiek1 = animation.FuncAnimation(run.controller.dashboard.temperatuursensor.grafiek.fig, run.controller.dashboard.temperatuursensor.grafiek.animate, interval=1000, blit=False)
grafiek2 = animation.FuncAnimation(run.controller.dashboard.lichtsensor.grafiek.fig, run.controller.dashboard.lichtsensor.grafiek.animate, interval=1000, blit=False)
run.controller.dashboard.win.mainloop()