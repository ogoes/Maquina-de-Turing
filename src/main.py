#!/usr/bin/python3
import sys
import maquina

def read_lines(filename):
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

    for t in lines[7:]:
        split_tmp = t.split(' ')

        transition = {}
        transition['estado_atual'] = split_tmp[0]
        transition['estado_destino'] = split_tmp[1]
        transition['fita'] = {
                    'simbolo_atual': split_tmp[2],
                    'novo_simbolo': split_tmp[3],
                    'movimento': split_tmp[4]
        }

        result['transicoes'].append(transition)

    arq.close()
    return result


def main():
    lines = read_lines(sys.argv[1])

    machine = Maquina(lines, sys.argv[2].strip('"'))
    machine.run()
    

if __name__ == '__main__':
    main()