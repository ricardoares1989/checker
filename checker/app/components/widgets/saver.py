"""Saver component class."""
from kivy.uix.floatlayout import FloatLayout

class Saver(FloatLayout):
    """Class to save the data in registers."""
    def __init__(self, *args, **kwargs):
        super(Saver, self).__init__(*args, **kwargs)
