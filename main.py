from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinout import TextInput


class MainCalc(App):
    def build(self):
        self.operators = ["/", "*", "-", "+"]


if __name__ == "__main__":
    app = MainCalc()
    app.run()
