from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class MainWindow(FloatLayout):
    pass

class FloatApp(App):
    def build(self):
        return MainWindow()
if __name__ == "__main__":
    FloatApp().run()