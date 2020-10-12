""" Checks class to show the last 4 registers."""

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

class Register(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(Register, self).__init__(*args, **kwargs)
        # self.checks_widget = checks_widget
class Checks(GridLayout):
    def __init__(self, *args, **kwargs):
        super(Checks, self).__init__(*args, **kwargs)