""" Checker is the main widger, that do it all the interaction."""
import csv
from datetime import datetime
from os import path
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from android.storage import primary_external_storage_path, app_storage_path
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
        self.add_widget(text_input)
        self.add_widget(save_export)
        self.add_widget(counter)
        self.add_widget(checks)
        self.text_input = self.children[3]
        self.save_export = self.children[2]
        self.counter = self.children[1]
        self.checks = self.children[0]
        self.asistance = self._asistance_dict()
        self.save_export.ids.save.bind(on_press=self.get_check)
        self.save_export.ids.export.bind(on_press=self.export_data)
        self.registers = self._create_register_widgets()

    def _asistance_dict(self):
        dictionary = {}
        try:
            today = datetime.now()
            save_dir = self._app_dir()
            string_today = today.strftime("%d_%m_%y")
            inputfile = open(f"{save_dir}/download/auto_save_asistance{string_today}.csv", newline="")
            reader = csv.reader(inputfile)
            state_data = {int(number[0]): True for number in reader}
            inputfile.close()
            save_registers = 0
            for i in range(0, 10000):
                try:
                    if state_data[i] == True:
                        save_registers += 1
                        dictionary[i] = True
                except KeyError:
                    dictionary[i] = False
            self._update_counter(save_registers=save_registers, initialize=True)
        except FileNotFoundError:
            for i in range(0, 10000):
                dictionary[i] = False
        return dictionary

    def _create_register_widgets(self):
        register_array = []
        for element in range(0,4):
            element = Register()
            element.ids.delete_register.bind(on_press=self.delete_register)
            register_array.append(element)
        return register_array

    def _last_register_child(self):
        try:
            last_child = self.checks.children[-1]
        except IndexError:
            last_child = False
        return last_child
    
    def _usable_register(self):
        for element in self.registers:
            if element in self.checks.children:
                pass
            else:
                return element
        element = self._last_register_child()
        return element

    def get_check(self, *args, **kwargs):
        asistance = self.asistance
        register = self._usable_register()
        try:
            text = self.text_input.ids.text_label.text
            if asistance[int(text)]:
                pass
            else:
                register.ids.register_label.text = text
                if len(self.checks.children) >= 4:
                    first_child = self._last_register_child()
                    self.checks.remove_widget(first_child)
                self.checks.add_widget(register)
                self.asistance[int(text)] = True
                self._update_counter()
            self.text_input.ids.text_label.text = ""
        except ValueError:
            pass

    def _auto_save(self):
        data_dict = self.asistance
        data = self.transform_data_dict(data_dict)
        data.sort()
        today = datetime.now()
        export_dir = self._app_dir()
        string_today = today.strftime("%d_%m_%y")
        outfile = open(f"{export_dir}/download/auto_save_asistance{string_today}.csv", "w", newline="")
        writer = csv.writer(outfile)
        writer.writerows(map(lambda x: [x], data))
        outfile.close()

    def _update_counter(self, delete=False, save_registers=0, initialize=False):
        if save_registers > 0 and initialize == True:
            self.counter_text = save_registers
        elif delete:
            self.counter_text -= 1
        else:
            self.counter_text += 1
        if int(self.counter.ids.counter.text) % 20 == 0 and initialize == False:
            self._auto_save()
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
