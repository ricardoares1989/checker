""" Screen model widget."""

#Layouts
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from android.permissions import request_permissions, Permission
#components
from app.components.widgets.checker import Checker

class Header(FloatLayout):
    pass


class ScreenModel(Screen):
    """ Screen Model that content all the boxlayouts
    to give a model for all the screens."""

    def __init__(self, *args, **kwargs):
        super(ScreenModel, self).__init__()
        request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
        self.checker = Checker()
        self.header = Header()
        self.add_widget(self.checker)
        self.add_widget(self.header)
