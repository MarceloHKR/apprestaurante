from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class PrimeiroGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(PrimeiroGridLayout, self).__init__(**kwargs)
        
        self.primeiro_grid = GridLayout()
        self.primeiro_grid.add_widget(Button(text='Botão 1'))

class SegundoGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(SegundoGridLayout, self).__init__(**kwargs)

        self.segundo_grid = GridLayout(cols=1)
        self.segundo_grid.add_widget(Button(text='Botão 2'))
        self.segundo_grid.add_widget(Button(text='Botão 3'))
        self.segundo_grid.add_widget(Button(text='Botão 4'))

class TerceiroGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(TerceiroGridLayout, self).__init__(**kwargs)

        self.terceiro_grid = GridLayout(cols=2)
        self.terceiro_grid.add_widget(Button(text='Botão 5'))
        self.terceiro_grid.add_widget(Button(text='Botão 6'))
        self.terceiro_grid.add_widget(Button(text='Botão 7'))
        self.terceiro_grid.add_widget(Button(text='Botão 8'))

class QuartoGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(QuartoGridLayout, self).__init__(**kwargs)

        self.quarto_grid = GridLayout(cols=3)
        self.quarto_grid.add_widget(Button(text='Botão 9'))
        self.quarto_grid.add_widget(Button(text='Botão 10'))
        self.quarto_grid.add_widget(Button(text='Botão 11'))


class MainLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(PrimeiroGridLayout)
        self.add_widget(SegundoGridLayout)
        self.add_widget(TerceiroGridLayout)
        self.add_widget(QuartoGridLayout)



class GradesApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    GradesApp().run()