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

        self.finais = result["estados_finais"]

        for i, estado in enumerate(self.listaEstados):
            if estado.getNome() == result['estado_inicial']:
                self.listaEstados[i].setInicial()
                self.estadoAtual = self.listaEstados[i]


        self.execucoes.append({'exec': Algoz(self.qtde_execucoes,
                                self.fita,
                                self.estadoAtual)})
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
        transitions = [t for t in self.transicoes 
                        if estado.getNome() == t.getEstadoAtual().getNome() and t.getSimboloAtual() == simbolo]
        return transitions

    def run(self):

        retorno_exec = []

        transicoes = self.get_transicoes(self.execucoes[0]['exec'].get_estado(), self.execucoes[0]['exec'].get_simbolo())
        self.execucoes[0]['transicoes'] = transicoes

        while True:
            print("---------------------------------------------------------------------")

            i = 0

            aux_execs = []
            for ex in self.execucoes:
                

                if len(ex['transicoes']) == 1:
                    ex['transicoes'] = ex['transicoes'][0]
                    aux_execs.append(ex)
                elif len(ex['transicoes']) > 1:
                    aux_trans = ex['transicoes']
                    ex['transicoes'] = aux_trans[0]
                    aux_execs.append(ex)

                    for trans in aux_trans[1:]:
                        self.qtde_execucoes += 1
                        aux = Algoz(self.qtde_execucoes, ex['exec'].get_fita(), ex['exec'].get_estado())
                        aux_execs.append({'exec': aux,
                                            'transicoes': trans})

            self.execucoes = aux_execs

            trans = []
            for execs in self.execucoes:
                execs['exec'].execute(execs['transicoes'])
                execs['transicoes'] = self.get_transicoes(execs['exec'].get_estado(), execs['exec'].get_simbolo())
                trans += execs['transicoes']
                if execs['exec'].is_final(self.entrada) == 0:
                    return 0

            if len(self.execucoes) == 0:
                print("Entrada Recusada: \"%s\"" %(self.entrada))
                return 1

            print("---------------------------------------------------------------------")
            input()


