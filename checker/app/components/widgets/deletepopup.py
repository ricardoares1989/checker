""" Component to delete a register. """

from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class DeletePopUp(Popup):
    """ Class to manage the Popup."""
    def __init__(self, checker, asistance, register, *args, **kwargs):
        super(DeletePopUp, self).__init__()
        self.register = register
        number = self.register.ids.register_label.text
        self.content = BoxLayout(orientation="vertical")
        self.content.add_widget(Label(text=f"¿Quieres borrar el numero {number}?", size_hint=(1,0.8)))
        btn = Button(text='Aceptar',size_hint=(1,0.2))
        btn.bind(on_press=self.delete_data)
        self.content.add_widget(btn)
        self.asistance = asistance
        self.checker = checker
    
    def delete_data(self, obj):
        checks = self.register.parent
        number = int(self.register.ids.register_label.text)
        index = self.asistance.index(number)
        self.asistance.pop(index)
        checks.remove_widget(self.register)
        self.checker._update_counter()
        self.dismiss()