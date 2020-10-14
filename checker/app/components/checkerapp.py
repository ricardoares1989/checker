""" Main app."""

#Kivy config

from kivy.uix.label import Label
from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from .screenmanagers.mainscreen import MainScreenWidget
# from .widgets.inputregister import InputRegister
from .widgets.checker import Checker

#Screen start config
Config.set("graphics", "height", "800")
Config.set("graphics", "width", "600")
Config.set("graphics", "minimum_width", "600")
Config.set("graphics", "minimum_height", "800")
Config.set('input', 'mouse', 'mouse.multitouch_on_demand')

Builder.load_file('./app/components/classes.kv')

class CheckerApp(App):
    """Class to implement the functionality of
    the weco App."""

    def open_settings(self, *args):
        """Function to avoid the debug settings."""
        pass

    def build(self):
        return MainScreenWidget()
