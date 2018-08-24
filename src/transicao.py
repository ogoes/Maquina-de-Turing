class Transicao:
    def __init__(self, estadoAtual, novoEstado, *dados):
        self.estadoAtual = estadoAtual
        self.novoEstado = novoEstado
        self.simboloAtual = dados[0] 
        self.novoSimbolo = dados[1] 
        self.movimento = dados[2] 


    def getSimboloAtual(self):
        return self.simboloAtual

    def getNovoSimbolo(self):
        return self.novoSimbolo

    def getEstadoAtual(self):
        return self.estadoAtual

    def getNovoEstado(self):
        return self.novoEstado

    def getMovimento(self):
        return self.movimento