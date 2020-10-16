"""Saver component class."""
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class KeyboardButton(Button):
    def __init__(self, *args, **kwargs):
        super(KeyboardButton, self).__init__()

class Saver(FloatLayout):
    """Class to save the data in registers."""
    def __init__(self, *args, **kwargs):
        super(Saver, self).__init__()
        self.grid = self.ids.grid
        self.buttons = self.grid.children
        self.keyboard = [button for button in self.buttons if isinstance(button, KeyboardButton)]
        for button in self.keyboard:
            button.bind(on_press=self.get_text)

    def get_text(self, value):
        checker = self.parent
        input_wid = checker.text_input.ids.text_label
        if len(input_wid.text) < 4:
            input_wid.text += value.text