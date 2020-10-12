"""Input Register component class."""
from kivy.uix.textinput import TextInput

class InputRegister(TextInput):
    max_characters = 5
    def insert_text(self, substring, from_undo=False):
        if len(self.text) > self.max_characters:
            substring =""
        TextInput.insert_text(self, substring, from_undo)