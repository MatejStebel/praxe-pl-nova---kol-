import sys
import kivy
from kivy.resources import resource_add_path

if getattr(sys, 'frozen', False):
    resource_add_path(sys._MEIPASS)
    
import os
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from tkinter import Tk, filedialog
import random
Builder.load_file("finder.kv")

class End(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.fullscreen = 'auto'
        self.image = self.ids.image


class Finder(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image_viewer = self.ids.image
        self.button = self.ids.button
        self.button.bind(on_press=self.load_image)
        self.status = self.ids.status
        self.name = self.ids.name
        self.age = self.ids.age
        self.country = self.ids.country
        self.city = self.ids.city
        self.hobbies = self.ids.hobbies
        self.name_y = False
        self.age_y = False
        self.country_y = False
        self.city_y = False
        self.hobbies_y = False
        self.image = False
        self.name.bind(on_text_validate=self.check_name)
        self.age.bind(on_text_validate=self.check_age)
        self.country.bind(on_text_validate=self.check_country)
        self.city.bind(on_text_validate=self.check_city)
        self.hobbies.bind(on_text_validate=self.check_hobbies)
        self.done = True
        self.button1 = self.ids.button1
        self.button1.bind(on_press=self.find)
        self.start = False
        self.bar = self.ids.bar
        self.status_label = self.ids.status_label
        self.number = 0

    def find(self, y):
        self.start = True
    
    def finding(self, dt):
        if self.start and self.bar.value <= 300 and self.name_y and self.age_y and self.country_y and self.city_y and self.hobbies_y and self.image:
            self.numberr = random.randint(100, 1000)
            self.number += self.numberr
            self.bar.value += 1
            self.status_label.text = f"Scanned {str(self.number)} people"
        if self.start and self.bar.value <= 500 and self.bar.value >= 300:
            self.bar.value += 1
            self.numberrr = random.randint(100, 1000)
            self.number -= self.numberrr
            self.status_label.text = f"Eliminating incompatible people: {str(self.number)}"
        if self.start and self.bar.value < 600 and self.bar.value >= 500:
            self.bar.value += 1
            self.number -= 500
            self.status_label.text = f"Eliminating incompatible people: {str(self.number)}"
        if (self.start and self.bar.value == 600) or self.number < 0:
            self.number = 0
            self.bar.value = 600
            self.status_label.text = f"Found compatible people: {str(self.number)}"
            self.start = False
            self.add_widget(End())
    def load_image(self, selection):
        # Open the standard OS system file dialog
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp")]
        )
        if file_path and os.path.exists(file_path):
            self.image_viewer.source = file_path
            self.image = True
    def update(self, dt):
        if self.name_y and self.age_y and self.country_y and self.city_y and self.hobbies_y and self.image :
            self.status.text = ""
            self.show_ready_message()
            self.done = False
        elif self.done:
            self.status.text = "Waiting for all data"
    def show_ready_message(self):
        self.status.text = "Ready for searching"
    def check_name(self, text):
        if text.text == "" or text.text.isdigit():
            self.name_y = False
        else:
            self.name_y = True
    def check_age(self, text):
        if text.text.isdigit():
            self.age_y = True
        else:
            self.age_y = False
    def check_country(self, text):
        if text.text == "" or text.text.isdigit():
            self.country_y = False
        else:
            self.country_y = True
    def check_city(self, text):
        if text.text == "" or text.text.isdigit():
            self.city_y = False
        else:
            self.city_y = True
    def check_hobbies(self, text):
        if text.text == "" or text.text.isdigit():
            self.hobbies_y = False
        else:
            self.hobbies_y = True

class FinderApp(App):
    def build(self):   
        app = Finder()
        Window.bind(on_key_down=self.on_key_down)
        Clock.schedule_interval(app.update, 1.0 / 60.0)
        Clock.schedule_interval(app.finding, 1.0 / 60.0)
        Window.fullscreen = 'auto'
        return app
    def on_key_down(self, window, key, scancode, codepoint, modifiers):
        # 27 is the specific integer code for the Escape key
        if key == 27:
            App.get_running_app().stop()

if __name__ == "__main__":
    FinderApp().run()