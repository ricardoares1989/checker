""" Screen Manager"""

from kivy.uix.screenmanager import ScreenManager
from .screenmodel import ScreenModel

class MainScreenWidget(ScreenManager):
    """ Class to return the function to return the app."""
    def __init__(self, *args, **kwargs):
        super(MainScreenWidget, self).__init__(*args, **kwargs)
        ScreenModelWidget = ScreenModel(name="start")
        self.add_widget(ScreenModelWidget)