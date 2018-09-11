class Transicao:
    def __init__(self, estadoAtual, novoEstado, *dados):
        self.estadoAtual = estadoAtual
        self.novoEstado = novoEstado
        self.simboloAtual = dados[0] 
        self.novoSimbolo = dados[1] 
        self.movimento = dados[2] 


    def get_simbolo_atual(self):
        return self.simboloAtual

    def get_novo_simbolo(self):
        return self.novoSimbolo

    def get_estado_atual(self):
        return self.estadoAtual

    def get_novo_estado(self):
        return self.novoEstado

    def get_movimento(self):
        return self.movimento