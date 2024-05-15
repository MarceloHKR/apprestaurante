from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.config import Config
import requests
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from tkinter import Button
from kivy.uix.boxlayout import BoxLayout

class PopupErro(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Erro de autenticação'
        self.size_hint = (0.7, 0.4)
        self.auto_dismiss = False
        
        self.box = BoxLayout(orientation="vertical")
        self.add_widget(
            Label(
                text="Usuário ou senha invalidos",
            )
        )
        
        self.add_widget(
            Button(
                text="Fechar",
                on_press=self.dismiss
            )
        )

        self.add_widget(self.box)

Config.set('graphics', 'reizable', '0')
Config.set('graphics', 'with', '360')
Config.set('graphics', 'height', '640')


class TelaLogin(Screen):
    def autenticar(self):
        usuario = self.ids.txt_usuario.text
        senha = self.ids.txt_senha.text

        url = 'https://ae4c-170-231-200-76.ngrok-free.app/restaurante/autenticar'
        dados = {'usuario':usuario, "senha": senha}
        resposta = requests.post(url, json=dados)
        if resposta.status_code == 200:
            self.manager.current = "tela_principal"
        else:
            popup_erro = PopupErro()
            popup_erro.open()

class TelaPrincipal(Screen):
    pass
        
class TelaGarcom(Screen):
    pass

class TelaCaixa(Screen):
    pass

class GerenciadorTelas(ScreenManager):
    pass

kv = Builder.load_file('restaurante.kv')


class RestauranteApp(App):
    def build(self):
        return kv
    
if __name__ == "__main__":
    RestauranteApp().run()
