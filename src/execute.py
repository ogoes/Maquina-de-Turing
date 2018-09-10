
from copy import copy



class Algoz():
    """docstring for Algoz"""

    def __init__(self, execucao, fita, estado_inicial):

        self.execucao = execucao
        self.fita = fita
        self.estado_inicial = estado_inicial
        self.estado_atual = estado_inicial

    def get_estado(self):
        return self.estado_atual

    def get_simbolo(self):

        return self.fita.getPos()

    def get_fita(self):

        return copy(self.fita)

    def is_final(self, entrada):
        if self.estado_atual.isFinal():
            print("Entrada Aceita: \"%s\"" % (entrada))
            exit(0)

    def get_copias(self, qtde, qtde_execucoes):
        aux = []
        if qtde < 0:
            qtde = 0
        for j in range(qtde):
            copia = Algoz(qtde_execucoes,
                        self.get_fita(),
                        self.estado_atual)
            aux.append(copia)

        return aux

    def mostra_fita(self):
        print("\nEXECUÇÂO: %i" % (self.execucao))
        print("Estado Atual: %s" % (self.estado_atual.getNome()))
        self.fita.mostraFita()

    def execute(self, transicao):

        self.mostra_fita()
        self.estado_atual = transicao.getNovoEstado()

        novoSimbolo = transicao.getNovoSimbolo()
        self.fita.setPos(novoSimbolo)

        print("Instrução a ser executada:",
              transicao.getEstadoAtual().getNome(), "-->",
              transicao.getNovoEstado().getNome(), ",",
              transicao.getSimboloAtual(), "-->",
              transicao.getNovoSimbolo(), ",",
              transicao.getMovimento())



        movimento = transicao.getMovimento()
        if movimento == 'R':
            self.fita.setRight()
        elif movimento == 'L':
            self.fita.setLeft()

        self.fita.mostraFita()
        print()
        return {
            "estado": self.estado_atual,
            "simbolo": self.fita.getPos()
            }
