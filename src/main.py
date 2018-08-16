#!/usr/bin/python3
import sys
import classes

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
    result['qt_fitas'] = int(lines[6])
    result['transicoes'] = []

    for t in lines[7:]:
        split_tmp = t.split(' ')

        transition = {}
        transition['estado_atual'] = split_tmp[0]
        transition['estado_destino'] = split_tmp[1]
        transition['fitas'] = []

        for i in range(result['qt_fitas']):
            transition['fitas'].append(
                {
                    'simbolo_atual': split_tmp[i * 3 + 2],
                    'novo_simbolo': split_tmp[i * 3 + 3],
                    'movimento': split_tmp[i * 3 + 4]
                }
            )

        result['transicoes'].append(transition)

    arq.close()
    return result


def main():
    lines = read_lines(sys.argv[1])

    machine = classes.Machine(lines, sys.argv[2].strip('"'))
    machine.run()
    

if __name__ == '__main__':
    main()