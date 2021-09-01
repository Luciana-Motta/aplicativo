from kivy.app import App
from kivy.metrics import sp
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import ScreenManager , Screen , NoTransition
from professor import Professor
from projeto import Projeto
import csv


class Gerenciador(ScreenManager):
    def __init__(self , **kwargs): 
        super().__init__(**kwargs)
        self.transition = NoTransition()
        Clock.schedule_interval(self.update, 2.0) 
    
    def update(self,*kwargs):
        if self.current == 'apresentacao':
            self.current = 'inicio'
    

class Apresentacao(Screen):
    pass

class Inicio(Screen):
    pass

class Login(Screen):
    def __init__(self , **kwargs): 
        super().__init__(**kwargs)
    
    def fazer_login(self, loginText, passwordText):
        p = Professor.procuraCadastro(loginText)
        if p == None: 
            print("login errado")
        elif p.getSenha() != passwordText:
            print("senha errada")
        else: 
            p.setLogado(True)
            self.manager.current = 'perfil'
                
       
class Cadastro(Screen):
    def __init__(self , **kwargs): 
        super().__init__(**kwargs)

    #def verificar_email(self, email):

    def fazer_cadastro(self, nomeText, emailText, matriculaText, senhaText, confirmaText): 
        if senhaText == confirmaText:
            professor = Professor(nomeText, emailText, matriculaText, senhaText)
            App.get_running_app().setProfessor(nomeText)
            self.manager.current = 'perfil'    
        else:
            print("A senha digitada na confirmação não corresponde a senha")
    
            

class Perfil(Screen):
    def __init__(self , **kwargs): 
        super().__init__(**kwargs)
        self.aux = True
        Clock.schedule_interval(self.update, 0.1) 


    
    def update(self, *args):
        if App.get_running_app().root.current == 'perfil' and self.aux:
            self.aux = False
            self.box = BoxLayout(size=(100, 100), pos_hint = {'x' : -0.2 , 'y': .38})
            self.label = Label(text = '', font_size = 14 , color = (0,0,0,1))
            self.label.text = App.get_running_app().getProfessor()
            self.box.add_widget(self.label)
            self.add_widget(self.box)
    
    def add_botaoSaude(self , texto):
        self.box_aux = BoxLayout(size_hint_y = None , height = 40, padding = 5)
        self.botao = BotaoSaudeProjeto(text = texto, size_hint = (0.8 , 1))
        self.botao.on_release = self.mudarTela(texto)
        self.box_aux.add_widget(self.botao)
        self.ids.box.add_widget(self.box_aux)
        App.get_running_app().root.get_screen('saude').add_botaoSaude(texto)

    def add_botaoCultura(self , texto):
        self.box_aux = BoxLayout(size_hint_y = None , height = 40, padding = 5)
        self.botao = BotaoCultProjeto(text = texto, size_hint = (0.8 , 1))
        self.botao.on_release = self.mudarTela(texto)
        self.box_aux.add_widget(self.botao)
        self.ids.box.add_widget(self.box_aux)
        App.get_running_app().root.get_screen('cultura').add_botaoCultura(texto)
    
    def add_botaoNegocios(self , texto):
        self.box_aux = BoxLayout(size_hint_y = None , height = 40, padding = 5)
        self.botao = BotaoNegociosProjeto(text = texto, size_hint = (0.8 , 1))
        self.botao.on_release = self.mudarTela(texto)
        self.box_aux.add_widget(self.botao)
        self.ids.box.add_widget(self.box_aux)
        App.get_running_app().root.get_screen('negocios').add_botaoNegocios(texto)

    def add_botaoEducacao(self , texto):
        self.box_aux = BoxLayout(size_hint_y = None , height = 40, padding = 5)
        self.botao = BotaoEduProjeto(text = texto, size_hint = (0.8 , 1))
        self.botao.on_release = self.mudarTela(texto)
        self.box_aux.add_widget(self.botao)
        self.ids.box.add_widget(self.box_aux)
        App.get_running_app().root.get_screen('educacao').add_botaoEducacao(texto)

    def mudarTela(self, texto):
        App.get_running_app().root.get_screen('projeto').add_labels(texto)
        Clock.schedule_once(self.teste, 0.1)

    def teste(self, *args):
        self.manager.current = 'perfil'


class CadastroProjeto(Screen):
    def __init__(self , **kwargs): 
        super().__init__(**kwargs)

    #def verificar_email(self, email):

    def cadastrarProjeto(self, nome_projeto, resumo, serv_oferecidos, para_quem, como_utilizar, telefone, telefone_seg, email, site, local_ufjf, area_projeto): 
        projeto = Projeto(nome_projeto, resumo, serv_oferecidos, para_quem, como_utilizar, telefone, telefone_seg, email, site, local_ufjf, area_projeto)
        if area_projeto == 'saude' or area_projeto == 'saúde':
            App.get_running_app().root.get_screen('perfil').add_botaoSaude(nome_projeto)
        elif area_projeto == 'cultura':
            App.get_running_app().root.get_screen('perfil').add_botaoCultura(nome_projeto)
        elif area_projeto == 'negocios' or area_projeto == 'negócios':
            App.get_running_app().root.get_screen('perfil').add_botaoNegocios(nome_projeto)
        elif area_projeto == 'educação' or area_projeto == 'educacao':
            App.get_running_app().root.get_screen('perfil').add_botaoEducacao(nome_projeto)
        else: 
            print('area do projeto inexistente')

        self.manager.current = 'perfil'

class TelaSaude(Screen):
    def __init__(self , **kwargs): 
        super().__init__(**kwargs)

    def add_botaoSaude(self , texto):
        self.box_aux = BoxLayout(size_hint_y = None , height = 40, padding = 5)
        self.botao = BotaoSaudeProjeto(text = texto, size_hint = (0.8 , 1), on_release = self.mudarTela)
        self.box_aux.add_widget(self.botao)
        self.ids.box.add_widget(self.box_aux)

    def mudarTela(self, *args):
        self.manager.current = 'projeto'

class TelaCultura(Screen):
    def __init__(self , **kwargs): 
        super().__init__(**kwargs)

    def add_botaoCultura(self , texto):
        self.box_aux = BoxLayout(size_hint_y = None , height = 40, padding = 5)
        self.botao = BotaoCultProjeto(text = texto, size_hint = (0.8 , 1),on_release = self.mudarTela)
        self.box_aux.add_widget(self.botao)
        self.ids.box.add_widget(self.box_aux)

    def mudarTela(self, *args):
        self.manager.current = 'projeto'

class TelaNegocios(Screen):
    def __init__(self , **kwargs): 
        super().__init__(**kwargs)

    def add_botaoNegocios(self , texto):
        self.box_aux = BoxLayout(size_hint_y = None , height = 40, padding = 5)
        self.botao = BotaoNegociosProjeto(text = texto, size_hint = (0.8 , 1),on_release = self.mudarTela)
        self.box_aux.add_widget(self.botao)
        self.ids.box.add_widget(self.box_aux)

    def mudarTela(self, *args):
        self.manager.current = 'projeto'

class TelaEducacao(Screen):
    def __init__(self , **kwargs): 
        super().__init__(**kwargs)

    def add_botaoEducacao(self , texto):
        self.box_aux = BoxLayout(size_hint_y = None , height = 40, padding = 5)
        self.botao = BotaoEduProjeto(text = texto, size_hint = (0.8 , 1),on_release = self.mudarTela)
        self.box_aux.add_widget(self.botao)
        self.ids.box.add_widget(self.box_aux)

    def mudarTela(self, *args):
        self.manager.current = 'projeto'

class TelaProjeto(Screen):
    def __init__(self , **kwargs): 
        super().__init__(**kwargs)

    def add_labels(self , texto, *args):
        projeto = Projeto.procurar_projeto(texto)
        lista = projeto.retornaInformacoes()
        print(len(lista))

        for aux in lista:
            self.box_aux = BoxLayout( size_hint_y = None , height = 40, padding = 5)
            self.label = MeuLabel(text = '', font_size = 14 , color = (.37,.37,.37,1))
            self.label.text = aux
            self.box_aux.add_widget(self.label)
            self.ids.box.add_widget(self.box_aux)
        
    def remove_labels(self, *args):
        aux = self.ids.box
        aux.clear_widgets()
        self.manager.current  = 'inicio'

class TelaUFJF(Screen):
    def __init__(self , **kwargs): 
        super().__init__(**kwargs)
        self.aux = True
        Clock.schedule_interval(self.update, 0.1) 

    def update(self, *args):
        if App.get_running_app().root.current == 'ufjf' and self.aux:
            self.aux = False
            self.box = BoxLayout( orientation = 'vertical' , size=(300, 300), pos_hint = {'x' : 0.01 , 'y': .45})
            self.label1 = MeuLabel(text = '', font_size = 14 , color = (.37,.37,.37,1))
            self.label1.text = 'A UFJF contribui de diversas formas para a comunidade de Juiz de Fora.Sua contribuição mais famosa é a formação de profissionais qualificados para o mercado de trabalho, promovendo o desenvolvimento na cidade. Somado a isso, a UFJF conta com diversas outras contribuições diretas para quem mora na região. '
            self.box.add_widget(self.label1)
            self.label2 = MeuLabel(text = '', font_size = 14 , color = (.37,.37,.37,1))
            self.label2.text = 'Além do espaço físico que conta com áreas de lazer e de atividades físicas, há também uma grande variedade de projetos de extensão que oferecem serviços a socidade, muitos desses sem custos. '
            self.box.add_widget(self.label2)
            self.add_widget(self.box)


class BotaoMenu(Button):
    pass

class BotaoSaude(Button):
    pass

class BotaoSaudeProjeto(Button):
    pass

class BotaoCult(Button):
    pass

class BotaoCultProjeto(Button):
    pass

class BotaoNegocios(Button):
    pass

class BotaoNegociosProjeto(Button):
    pass

class BotaoEdu(Button):
    pass

class BotaoEduProjeto(Button):
    pass

class BotaoUFJF(Button):
    pass

class BotaoLogin(Button):
    pass

class MeuLabel(Label):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, None)
    
    def on_size(self,*args):
        # vamos colocar um espaço de 10 sp
        self.text_size = (self.width - sp(10), None)

    def on_texture_size(self,*args):
        self.size = self.texture_size
        # vamos colocar um espaço a mais de 20sp
        self.height += sp(20)


class Aplicativo(App): 
    def __init__(self , **kwargs): 
        super().__init__(**kwargs)
        self.matricula = ''

    def setProfessor(self, matricula):
        self.matricula = matricula 
    
    def getProfessor(self):
        print("a" + self.matricula + "a")
        return self.matricula

    def build(self):
        return Gerenciador()
    
    
    
Aplicativo().run()
