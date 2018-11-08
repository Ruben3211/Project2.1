from view.Dashboardview import Dashboardview
from controller.meet_controller import meetController


class Dashboardcontroller:
    def __init__(self, master):
        self.meter = meetController(master)

    def ga_naar_paneel(self):
        """


        """
