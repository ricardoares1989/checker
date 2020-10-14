"""Input Register component class."""
from kivy.uix.floatlayout import FloatLayout

class InputRegister(FloatLayout):
    
    def __init__(self, *args, **kwargs):
        super(InputRegister, self).__init__()
        self.delete = self.ids.undo
        self.input = self.ids.text_label
        self.delete.bind(on_press=self.delete_text)
    
    def delete_text(self, value):
        self.input.text = self.input.text[:-1]