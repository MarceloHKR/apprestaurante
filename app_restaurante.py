from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.config import Config

Config.set('graphics', 'reizable', '0')
Config.set('graphics', 'with', '360')
Config.set('graphics', 'height', '640')


class TelaPrincipal(Screen):
    pass
        
class TelaGarcom(Screen):
    pass

class GerenciadorTelas(ScreenManager):
    pass

kv = Builder.load_file('restaurante.kv')


class RestauranteApp(App):
    def build(self):
        return kv
    
if __name__ == "__main__":
    RestauranteApp().run()