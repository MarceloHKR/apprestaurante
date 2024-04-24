from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MainLayoutGrid(GridLayout):
    pass

class MyLayoutApp(App):
    def build(self):
        return MainLayoutGrid()
if __name__ == "__main__":
    MyLayoutApp().run()