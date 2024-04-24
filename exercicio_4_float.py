from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class MainWindow(FloatLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        #Botão inferior esquerdo
        self.btn1 = Button(
            text="Button1",
            size_hint=(0.2, 0.2),
            pos_hint={'left':0, 'y':0}
        )
        self.add_widget(self.btn1)

        #botão inferior direito
        self.btn2 = Button(
            text="Button2",
            size_hint=(0.2, 0.2),
            pos_hint={'right':1, 'y':0}
        )
        self.add_widget(self.btn2)

        #botão central
        self.btn3 = Button(
            text="Button3",
            #size_hint=(0.2, 0.2),
            size_hint=(None, None),
            size=(150,50),
            #pos_hint={'center_x':0.5, 'center_y':0.5}
            pos=(300, 300)
        )
        self.add_widget(self.btn3)

        #botão superior esquerdo
        self.btn4 = Button(
            text="Button4",
            size_hint=(0.2, 0.2),
            pos_hint={'left':0, 'top':1}
        )
        self.add_widget(self.btn4)

        #botão superior direito
        self.btn5 = Button(
            text="Button5",
            size_hint=(0.2, 0.2),
            pos_hint={'right':1, 'top':1}
        )
        self.add_widget(self.btn5)

class FloatApp(App):
    def build(self):
        return MainWindow()
if __name__ == "__main__":
    FloatApp().run()