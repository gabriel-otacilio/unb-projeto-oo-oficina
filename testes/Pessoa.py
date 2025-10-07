class Pessoa:
    def __init__(self,nome,idade):
        self.nome= nome
        self.idade=idade

    def comer(self,comida):      
        print(self.nome+' está comendo:'+comida)
