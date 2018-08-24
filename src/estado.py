class Estado:
    def __init__(self, nome):
        self.nome = nome
        self.inicial = False
        self.final = False

    def getNome(self):
        return self.nome

    def isFinal(self):
        return self.final

    def isInicial(self):
        return self.inicial

    def setInicial(self):
        self.inicial = True

    def setFinal(self):
        self.final = True
