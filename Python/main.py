# importeer hier alle mappen en andere dingen die nodig zijn
from tkinter import *
from view import *
from model import *
from controller import *

class main(Tk):
    def __init__(self):
        super.__init__()
        self.title("jelambo")

    def restart(self):
        self.title('jelambo')


run = main()
run.mainloop()