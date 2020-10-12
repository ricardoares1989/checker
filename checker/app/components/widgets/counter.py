""" Counter class to show all the registers."""

from kivy.uix.floatlayout import FloatLayout

class Counter(FloatLayout):
    def __init__(self, *args, **kwargs):
        super(Counter, self).__init__(*args, **kwargs)