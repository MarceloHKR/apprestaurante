from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MainLayout(GridLayout):
    pass

class exercicio2App(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    exercicio2App().run()