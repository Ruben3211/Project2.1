from view.Dashboardview import Dashboardview
from controller import *
from model import *



class Dashboardcontroller:
    def __init__(self, master):
        self.master = master
        self.dashboard = Dashboardview(self.master)



    # def get_temp_bovengrens(self):
    #     return self.dashboard.temperatuursensor.bovengrens

    def ga_naar_paneel(self):
        """


        """
