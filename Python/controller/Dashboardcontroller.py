from view import Dashboardview
from controller import *
from model import *

class Dashboardcontroller:
    def __init__(self, leider):
        self.leider = leider
        Dashboardview(self)

    def ga_naar_paneel(self):
        """


        """
