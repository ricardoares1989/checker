""" Checker is the main widger, that do it all the interaction."""
import csv
from datetime import date

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from .inputregister import InputRegister
from .saver import Saver
from .counter import Counter
from .checks import Checks, Register
from .deletepopup import DeletePopUp

class Checker(FloatLayout):
    """ this class has the input register widget counter and
        and the last 4 checks, and manage all the data."""
    
    def __init__(self, *args, **kwargs):
        super(Checker, self).__init__(*args, **kwargs)
        text_input = InputRegister()
        save_export = Saver()
        counter = Counter()
        checks = Checks()
        self.asistance = []
        self.add_widget(text_input)
        self.add_widget(save_export)
        self.add_widget(counter)
        self.add_widget(checks)
        self.text_input = self.children[3]
        self.save_export = self.children[2]
        self.counter = self.children[1]
        self.checks = self.children[0]
        self.save_export.ids.save.bind(on_press=self.get_check)
        self.save_export.ids.export.bind(on_press=self.export_data)

    def get_check(self, *args, **kwargs):
        try:
            text = self.text_input.text
            register = Register()
            register.ids.register_label.text = text
            register_id = register.ids.register_label.data_id = text
            register.ids.delete_register.bind(on_press=self.delete_register)
            if int(text) in self.asistance:
                pass
            else:
                if len(self.checks.children) >= 4:
                    first_child = self.checks.children[3]
                    self.checks.remove_widget(first_child)
                self.checks.add_widget(register)
                self.asistance.append(int(text))
            self.text_input.text = ""
            self._update_counter()
        except ValueError:
            print("Bad register")

    def _update_counter(self):
        self.counter.ids.counter.text = str(len(self.asistance))

    def export_data(self, *args, **kwargs):
        data = self.asistance
        data.sort()
        today = date.today()
        string_today = today.strftime("%d%B%Y")
        outfile = open(f"asistance{string_today}.csv", "w", newline="")
        writer = csv.writer(outfile)
        writer.writerows(map(lambda x: [x], data))
        outfile.close()

    def delete_register(self, obj):   
        number = obj.parent.ids.register_label.text
        delete_popup = DeletePopUp(checker=self, asistance=self.asistance, register=obj.parent, auto_dismiss=False)
        delete_popup.title = "Borrar registro"
        delete_popup.size_hint = (None, None)
        delete_popup.size = (300, 300)
        delete_popup.open()
