from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MainLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        #cria duas colunas
        self.cols = 2

        #adiciona o botão na coluna 1
        self.add_widget(Button(text='Button 1'))

        #cria o segundo grid na coluna dois do layout 
        self.second_grid = GridLayout(cols =1)

        #adiciona os botões no segundo grid
        self.second_grid.add_widget(Button(text='Button 2'))
        self.second_grid.add_widget(Button(text='Button 3'))
        self.second_grid.add_widget(Button(text='Button 4'))
        
        #adiciona o segundo grid
        self.add_widget(self.second_grid)

class LanchoneteApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    LanchoneteApp().run()