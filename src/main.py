#!/usr/bin/python3
import sys
from maquina import *

def read_lines(filename): ## faz a leitura das linhas do arquivo contendo as configurações da maquina
    arq = open(filename)

    lines = [line.strip() for line in arq.readlines()]

    result = {}
    result['alfabeto_entrada'] = lines[0].split(' ')
    result['alfabeto_fita'] = lines[1].split(' ')
    result['simbolo_espaco'] = lines[2]
    result['estados'] = lines[3].split(' ')
    result['estado_inicial'] = lines[4]
    result['estados_finais'] = lines[5].split(' ')
    result['transicoes'] = []

    for t in lines[7:]: ## a partir da linha 8 coleta os dados das transições
        split_tmp = t.split(' ')

        transition = {}
        transition['estado_atual'] = split_tmp[0]
        transition['estado_destino'] = split_tmp[1]
        transition['simbolo_atual'] = split_tmp[2]
        transition['novo_simbolo'] = split_tmp[3]
        transition['movimento'] = split_tmp[4]


        result['transicoes'].append(transition)

    arq.close()
    return result


def main():
    data = read_lines(sys.argv[1]) ## chamada da função de coleta dos dados a partir do arquivo

    if len(sys.argv) == 2:
        machine = Maquina(data, "")
    else:
        machine = Maquina(data, sys.argv[2].strip('"')) ## instanciação de uma maquina com os dados da maquina e entrada
    return machine.run() # inicio da execução dos dados
    

if __name__ == '__main__':
    main()