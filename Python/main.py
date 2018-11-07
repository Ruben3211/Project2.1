# importeer hier alle mappen en andere dingen die nodig zijn
from model import *
from controller import *
from controller import Dashboardcontroller
from tkinter import *

class main(Tk):
    def __init__(self):
        super().__init__()
        self.title("jelambo")
        # paneel_controller(self)
        Dashboardcontroller(self)

    def restart(self):
        self.title('jelambo')


run = main()
run.mainloop()