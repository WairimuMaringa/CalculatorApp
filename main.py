from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinout import TextInput


class MainCalc(App):
    def build(self):
        self.operators = ["/", "*", "-", "+"]
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout(orientation = "vertical")

        self.solution = TextInput(background_color = "black", foreground_color = "white")

        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"],
        ]

        for row in buttons:


if __name__ == "__main__":
    app = MainCalc()
    app.run()
