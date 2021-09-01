class Projeto:
    
    lista_projetos = []

    def __init__(self, nomeProjeto, resumo, servicosOferecidos, paraQuem, comoUtilizar, telefone, telefoneSegundario, emailContato, site, localUFJF, areaProjeto):
        self._nomeProjeto = nomeProjeto
        self._resumo = resumo
        self._servicosOferecidos = servicosOferecidos
        self._paraQuem = paraQuem
        self._comoUtilizar = comoUtilizar
        self._telefone = telefone
        self._telefoneSegundario = telefoneSegundario
        self._emailContato = emailContato 
        self._site = site 
        self._localUFJF = localUFJF
        self._areaProjeto = areaProjeto
        self.lista_projetos.append(self)


    def setNomeProjeto(self,nomeProjeto):
        self._nomeProjeto = nomeProjeto

    def getNomeProjeto(self):
        return self._nomeProjeto

    def setResumol(self,resumo):
        self._resumo = resumo

    def getResumo(self):
        return self._resumo

    def setServicosOferecidos(self,servicosOferecidos):
        self._servicosOferecidos = servicosOferecidos

    def getServicosOferecidos(self):
        return self._servicosOferecidos

    def setParaQuem(self, paraQuem):
        self._paraQuem = paraQuem

    def getParaQuem(self):
        return self._paraQuem

    def setComoUtilizar(self, paraQuem):
        self._comoUtilizar = comoUtilizar

    def getComoUtilizar(self):
        return self._comoUtilizar

    def setTelefone(self,telefone):
        self._telefone = telefone

    def getTelefone(self):
        return self._telefone

    def setTelefoneSegundario(self,telefoneSegundario):
        self._telefoneSegundario = telefoneSegundario

    def getTelefoneSegundario(self):
        return self._telefoneSegundario

    def setEmailContato(self,emailContato):
        self._emailContato = emailContato

    def getEmailContato(self):
        return self._emailContato

    def setSite(self,site):
        self._site = site

    def getSite(self):
        return self._site

    def setLocalUFJF(self, localUFJF):
        self._localUFJF = localUFJF

    def getlocalUFJFa(self):
        return self._localUFJF

    def setAreaProjeto(self, areaProjeto):
        self._areaProjeto = areaProjeto

    def getAreaProjeto(self):
        return self._areaProjeto

    def retornaInformacoes(self):
        lista = []
        lista.append(self._nomeProjeto)
        lista.append(self._resumo)
        lista.append(self._servicosOferecidos)
        lista.append(self._paraQuem)
        lista.append(self._comoUtilizar)
        lista.append(self._telefone)
        lista.append(self._telefoneSegundario)
        lista.append(self._emailContato)
        lista.append(self._site)
        lista.append(self._localUFJF)
        lista.append(self._areaProjeto)
        return lista 

    @staticmethod
    def add_projeto(projeto):
        Projeto.lista_projetos.append(projeto)


    @staticmethod
    def procurar_projeto(nomeProjeto):
        for o in Projeto.lista_projetos:
            if o.getNomeProjeto() == nomeProjeto:
                return o
