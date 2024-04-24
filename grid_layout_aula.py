from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MaingridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MaingridLayout, self).__init__(**kwargs)
        #define o número de colunas
        self.cols = 2
        #Define o espaçamento entre os widgets
        self.spacing = 10
        #Define o padding do GridLayout
        self.padding = 30
        #Define a altura padrão das linhas (como se fosse a altura mínima)
        self.row_default_height = 100
        #Define a largura padrão das colunas(como se fosse a largura mínima)
        self.col_default_widht = 200
        #Força a altura maxima das linhas
        self.row_force_default = True
        #Força a largura maxima das colunas
        self.col_force_default = True




class GradesApp(App):
    def build(self):
        return MaingridLayout()

if __name__ == '__main__':
    GradesApp().run()