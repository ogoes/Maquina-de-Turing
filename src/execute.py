
from copy import deepcopy



class Algoz():
    """docstring for Algoz"""

    def __init__(self, execucao, fita, estado_inicial):

        self.execucao = execucao
        self.fita = fita
        self.estado_inicial = estado_inicial
        self.estado_atual = estado_inicial
        self.count = 0

    def get_estado(self):
        return self.estado_atual

    def get_simbolo(self):

        return self.fita.get_pos()

    def get_fita(self):

        return deepcopy(self.fita)

    def is_final(self, entrada):
        if self.estado_atual.is_final():
            print("Entrada Aceita: \"", "\033[1m", "\033[36;2m", "%s" %(entrada), "\033[0;0m", '"',sep='')
            return 0

    def get_copias(self, qtde, qtde_execucoes):
        aux = []
        if qtde < 0:
            qtde = 0
        for j in range(qtde):
            copia = Algoz(qtde_execucoes+j,
                        self.get_fita(),
                        self.estado_atual)
            aux.append(copia)

        return aux

    def parou(self):
        print("Execução finalizada")

    def mostra_fita(self):
        print("Estado Atual: %s" % (self.estado_atual.get_nome()))
        self.fita.mostra_fita()

    def execute(self, transicao):


        if self.count == 100:
            print("Loop identificado")
            return 0

        if self.estado_atual.get_nome() == transicao.get_novo_estado().get_nome():
            self.count += 1
        else:
            self.count = 0

        print("\nEXECUÇÂO: %i" % (self.execucao))

        self.mostra_fita()
        self.estado_atual = transicao.get_novo_estado()

        novoSimbolo = transicao.get_novo_simbolo()
        self.fita.set_pos(novoSimbolo)

        print("Instrução a ser executada:",
              transicao.get_estado_atual().get_nome(), "-->",
              transicao.get_novo_estado().get_nome(), ",",
              transicao.get_simbolo_atual(), "-->",
              transicao.get_novo_simbolo(), ",",
              transicao.get_movimento())



        movimento = transicao.get_movimento()
        if movimento == 'R':
            self.fita.set_right()
        elif movimento == 'L':
            self.fita.set_left()

        self.mostra_fita()
        print()
        return {
            "estado": self.estado_atual,
            "simbolo": self.fita.get_pos()
            }
