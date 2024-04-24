from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class MainLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)

        self.cols = 3

        self.add_widget(Button(text='Button 1'))
        self.add_widget(Widget())
        self.add_widget(Button(text='Button 2'))
        self.add_widget(Widget())
        self.add_widget(Button(text='Button 3'))
        self.add_widget(Widget())
        self.add_widget(Button(text='Button 4'))
        self.add_widget(Widget())
        self.add_widget(Button(text='Button 5'))



class LanchoneteApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    LanchoneteApp().run()