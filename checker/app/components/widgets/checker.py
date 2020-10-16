""" Checker is the main widger, that do it all the interaction."""
import csv
from datetime import datetime
from os import path
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from android.storage import primary_external_storage_path
from kivy.uix.popup import Popup

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
        self.counter_text = 0
        self.asistance = self._asistance_dict()
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
    
    def _asistance_dict(self):
        dictionary = {}
        for i in range(0, 10000):
            dictionary[i] = False
        return dictionary

    def get_check(self, *args, **kwargs):
        asistance = self.asistance
        try:
            text = self.text_input.ids.text_label.text
            register = Register()
            register.ids.register_label.text = text
            register_id = register.ids.register_label.data_id = text
            register.ids.delete_register.bind(on_press=self.delete_register)
            if asistance[int(text)]:
                pass
            else:
                if len(self.checks.children) >= 4:
                    first_child = self.checks.children[3]
                    self.checks.remove_widget(first_child)
                self.checks.add_widget(register)
                self.asistance[int(text)] = True
                self._update_counter()
            self.text_input.ids.text_label.text = ""
        except ValueError:
            print("Bad register")

    def _update_counter(self, delete=False):
        if delete:
            self.counter_text -= 1
        else:
            self.counter_text += 1
        self.counter.ids.counter.text = str(self.counter_text)

    def _app_dir(self):
        return primary_external_storage_path()
    
    def transform_data_dict(self, data_dict):
        array_data = []
        for key, value in data_dict.items():
            if value:
                array_data.append(key)
        return array_data

    def export_data(self, *args, **kwargs):
        data_dict = self.asistance
        data = self.transform_data_dict(data_dict)
        data.sort()
        today = datetime.now()
        export_dir = self._app_dir()
        string_today = today.strftime("%d_%m_%y_%X")
        outfile = open(f"{export_dir}/download/asistance{string_today}.csv", "w", newline="")
        writer = csv.writer(outfile)
        writer.writerows(map(lambda x: [x], data))
        outfile.close()
        box = BoxLayout(orientation='vertical')
        box.add_widget(Label(
            text=f"""Tu archivo se encuentra en 
                    {export_dir}/download
                """
            )
        )
        popup = Popup(auto_dismiss=True, content=box)
        popup.title = "Exportación correcta"
        popup.size_hint = (.8, 0.2)
        popup.open()

    def delete_register(self, obj):   
        number = obj.parent.ids.register_label.text
        delete_popup = DeletePopUp(checker=self, 
            asistance=self.asistance, 
            register=obj.parent, 
            auto_dismiss=False
        )
        delete_popup.title = "Borrar registro"
        delete_popup.size_hint = (.9, .2)
        delete_popup.open()
