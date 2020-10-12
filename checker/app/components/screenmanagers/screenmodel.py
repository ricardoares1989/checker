""" Screen model widget."""

#Layouts
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout

#components
from app.components.widgets.checker import Checker

class Header(FloatLayout):
    pass


class ScreenModel(Screen):
    """ Screen Model that content all the boxlayouts
    to give a model for all the screens."""

    def __init__(self, *args, **kwargs):
        super(ScreenModel, self).__init__()
        self.checker = Checker()
        self.header = Header()
        self.add_widget(self.checker)
        self.add_widget(self.header)
