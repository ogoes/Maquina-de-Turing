from estado import *
from transicao import *
from fita import *
from execute import Algoz


class Maquina:
    """"""

    def __init__(self, result, entrada):
        if len(entrada) == 0:
            print("entrada vazia")
            exit(0)

        self.execucoes = []
        self.qtde_execucoes = 0
        self.alfabeto = result['alfabeto_entrada']
        self.entrada = entrada

        self.listaEstados = [Estado(i) for i in result['estados']]
        self.fita = Fita(result['alfabeto_fita'],
                         result['simbolo_espaco'], entrada)



        for i, estado in enumerate(self.listaEstados):
            if estado.getNome() == result['estado_inicial']:
                self.listaEstados[i].setInicial()
                self.estadoAtual = self.listaEstados[i]
                self.estado_inicial = self.estadoAtual


        self.execucoes.append(Algoz(self.qtde_execucoes,
                                self.fita,
                                self.estadoAtual))
        self.qtde_execucoes += 1


        for finais in result['estados_finais']:
            for i, estado in enumerate(self.listaEstados):
                if estado.getNome() == finais:
                    self.listaEstados[i].setFinal()

        self.transicoes = []
        for transicoes in result['transicoes']:
            for i, estado in enumerate(self.listaEstados):
                if transicoes['estado_atual'] == estado.getNome():
                    cur_state = self.listaEstados[i]
                if transicoes['estado_destino'] == estado.getNome():
                    nex_state = self.listaEstados[i]

            self.transicoes.append(Transicao(
                cur_state,
                nex_state,
                transicoes['simbolo_atual'],
                transicoes['novo_simbolo'],
                transicoes['movimento']))



    def get_transicoes(self, estado, simbolo):
        transitions = [t for t in self.transicoes if estado.getNome() == t.getEstadoAtual().getNome()]
        return [t for t in transitions if t.getSimboloAtual() == simbolo]



    def organiza(self, transicoes):

        trans_exec = []
        self.qtde_execucoes = 0
        execs_aux = []
        for execs in self.execucoes:

            aux_trans = []

            for t in transicoes:
                if t.getEstadoAtual().getNome() == execs.get_estado().getNome():
                    aux_trans.append(t)
                else:
                    break

            if len(aux_trans) > 0:
                transicoes.remove(aux_trans[0])
                execs_aux.append(execs)
                self.qtde_execucoes += 1
            for trans in aux_trans[1:]:
                transicoes.remove(trans)
                self.qtde_execucoes += 1
                execs_aux += execs.get_copias(1, self.qtde_execucoes)

            trans_exec += aux_trans

        self.execucoes = execs_aux
        return trans_exec


    def run(self):

        a = 0
        retorno_exec = []
        transicoes = []
        transicoes = self.get_transicoes(self.execucoes[0].get_estado(), self.execucoes[0].get_simbolo())
        while True:
            print("---------------------------------------------------------------------")

           
            aux_trans = []
            aux_execs = []
            for i, trans in enumerate(transicoes):
                retorno = self.execucoes[i].execute(transicoes[i])
                trans = self.get_transicoes(retorno['estado'], retorno['simbolo'])
                for t in trans:
                    aux_execs += self.execucoes[i].get_copias(1, self.qtde_execucoes)
                    self.qtde_execucoes += 1

                aux_trans += trans

            for finais in self.execucoes:
                finais.is_final(self.entrada)

            transicoes = aux_trans
            self.execucoes = aux_execs
            self.qtde_execucoes = 0


            if len(transicoes) == 0:
                print("entrada recusada:", self.entrada)
                exit(0)

            
                


            print("---------------------------------------------------------------------")
            input() 


