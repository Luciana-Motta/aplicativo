from projeto import Projeto

class Professor:
    
    lista_professores = []

    def __init__(self,  nome, email, matricula, senha):
        self._nome = nome
        self._email = email
        self._matricula = matricula
        self._senha = senha
        self._logado = True
        self.lista_projetos = []
        self.lista_professores.append(self)
 
    def setNome(self,nome):
        self._nome = nome

    def getNome(self):
        return self._nome

    def setEmail(self,email):
        self._email = email

    def getEmail(self):
        return self._email

    def setSenha(self,senha):
        self._senha = senha

    def getSenha(self):
        return self._senha

    def setMatricula(self, matricula):
        self._matricula = matricula

    def getMatricula(self):
        return self._matricula

    def setLogado(self, logado):
        self._logado = logado

    def getLogado(self):
        return self._logado

    @staticmethod
    def procuraCadastro(matricula):
        for o in Professor.lista_professores: 
            if o.getMatricula() == matricula:
                return o

    @staticmethod
    def verificaLogado():
        for o in Professor.lista_professores: 
            if o.getLogado() == True:
                return o

    @staticmethod
    def removerCadastro(matricula):
        for o in Professor.lista_professores: 
            if o.getMatricula() == matricula:
                Professor.lista.remove(o)   
    
    def add_projeto(self):
        pass
        
