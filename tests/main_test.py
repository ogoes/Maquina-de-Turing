import unittest
import sys

sys.path.insert(0, '../src')

import main


class TestInput(unittest.TestCase):
    def test_alfabeto_entrada(self):
        test1 = main.read_lines(
            '/home/fjorg/Projects/Maquina-de-Turing/tests/a.txt')

        self.assertEqual(test1['alfabeto_entrada'], ['X', 'a', 'b', 'c'])

        test2 = main.read_lines(
            '/home/fjorg/Projects/Maquina-de-Turing/tests/b.txt')

        self.assertEqual(test2['alfabeto_entrada'], ['a', 'b', 'c'])

        test3 = main.read_lines(
            '/home/fjorg/Projects/Maquina-de-Turing/tests/c.txt')

        self.assertEqual(test3['alfabeto_entrada'], ['0', '1', 'X'])

        test4 = main.read_lines(
            '/home/fjorg/Projects/Maquina-de-Turing/tests/d.txt')

        self.assertEqual(test4['alfabeto_entrada'], ['a', 'b'])

        test5 = main.read_lines(
            '/home/fjorg/Projects/Maquina-de-Turing/tests/e.txt')

        self.assertEqual(test5['alfabeto_entrada'], ['0', '1'])

    def test_alfabeto_fita(self):
        test1 = main.read_lines(
            '/home/fjorg/Projects/Maquina-de-Turing/tests/a.txt')

        self.assertEqual(test1['alfabeto_fita'], ['B', 'X', 'a', 'b', 'c'])

        test2 = main.read_lines(
            '/home/fjorg/Projects/Maquina-de-Turing/tests/b.txt')

        self.assertEqual(test2['alfabeto_fita'], ['B', 'a', 'b', 'c'])

        test3 = main.read_lines(
            '/home/fjorg/Projects/Maquina-de-Turing/tests/c.txt')

        self.assertEqual(test3['alfabeto_fita'], ['0', '1', 'B', 'X'])

        test4 = main.read_lines(
            '/home/fjorg/Projects/Maquina-de-Turing/tests/d.txt')

        self.assertEqual(test4['alfabeto_fita'], ['B', 'a', 'b'])

        test5 = main.read_lines(
            '/home/fjorg/Projects/Maquina-de-Turing/tests/e.txt')

        self.assertEqual(test5['alfabeto_fita'], ['0', '1', 'B'])

    def test_espaco_branco(self):
        test1 = main.read_lines(
            '/home/fjorg/Projects/Maquina-de-Turing/tests/a.txt')

        self.assertEqual(test1['simbolo_espaco'], 'B')

    def test_estados(self):
        test1 = main.read_lines(
            '/home/fjorg/Projects/Maquina-de-Turing/tests/a.txt')

        self.assertEqual(test1['estados'], ['0', '1', '2', '3', '6'])

        test2 = main.read_lines(
            '/home/fjorg/Projects/Maquina-de-Turing/tests/b.txt')

        self.assertEqual(test2['estados'], ['0', '1', '2', '3', '4'])

        test3 = main.read_lines(
            '/home/fjorg/Projects/Maquina-de-Turing/tests/c.txt')

        self.assertEqual(test3['estados'], ['0', '1', '2', '3', '4', '5', '6'])

        test4 = main.read_lines(
            '/home/fjorg/Projects/Maquina-de-Turing/tests/d.txt')

        self.assertEqual(test4['estados'], ['0', '1', '2', '3'])

        test5 = main.read_lines(
            '/home/fjorg/Projects/Maquina-de-Turing/tests/e.txt')

        self.assertEqual(test5['estados'], ['0', '1'])

    def test_estado_inicial(self):
        test1 = main.read_lines(
            '/home/fjorg/Projects/Maquina-de-Turing/tests/a.txt')

        self.assertEqual(test1['estado_inicial'], '0')

    def test_estados_finais(self):
        test1 = main.read_lines(
            '/home/fjorg/Projects/Maquina-de-Turing/tests/a.txt')

        self.assertEqual(test1['estados_finais'], ['6'])

    def test_qt_fitas(self):
        test1 = main.read_lines(
            '/home/fjorg/Projects/Maquina-de-Turing/tests/a.txt')

        self.assertEqual(test1['qt_fitas'], 1)

    def test_transicoes(self):
        test1 = main.read_lines(
            '/home/fjorg/Projects/Maquina-de-Turing/tests/a.txt')

        self.assertEqual(len(test1['transicoes']), 13)
        self.assertEqual(test1['transicoes'][0]['estado_atual'], '0')
        self.assertEqual(test1['transicoes'][0]['estado_destino'], '0')
        self.assertEqual(len(test1['transicoes'][0]['fitas']), 1)
        self.assertEqual(test1['transicoes'][0]['fitas']
                         [0]['simbolo_atual'], 'X')
        self.assertEqual(test1['transicoes'][0]['fitas']
                         [0]['novo_simbolo'], 'X')
        self.assertEqual(test1['transicoes'][0]['fitas'][0]['movimento'], 'R')

        self.assertEqual(test1['transicoes'][1]['estado_atual'], '0')
        self.assertEqual(test1['transicoes'][1]['estado_destino'], '1')
        self.assertEqual(len(test1['transicoes'][1]['fitas']), 1)
        self.assertEqual(test1['transicoes'][1]['fitas']
                         [0]['simbolo_atual'], 'a')
        self.assertEqual(test1['transicoes'][1]['fitas']
                         [0]['novo_simbolo'], 'X')
        self.assertEqual(test1['transicoes'][1]['fitas'][0]['movimento'], 'R')

        test2 = main.read_lines(
            '/home/fjorg/Projects/Maquina-de-Turing/tests/b.txt')

        self.assertEqual(len(test2['transicoes']), 8)
        self.assertEqual(test2['transicoes'][0]['estado_atual'], '0')
        self.assertEqual(test2['transicoes'][0]['estado_destino'], '0')
        self.assertEqual(len(test2['transicoes'][0]['fitas']), 3)

        self.assertEqual(test2['transicoes'][0]['fitas']
                         [0]['simbolo_atual'], 'a')
        self.assertEqual(test2['transicoes'][0]['fitas']
                         [0]['novo_simbolo'], 'a')
        self.assertEqual(test2['transicoes'][0]['fitas'][0]['movimento'], 'R')
        self.assertEqual(test2['transicoes'][0]['fitas']
                         [1]['simbolo_atual'], 'B')
        self.assertEqual(test2['transicoes'][0]['fitas']
                         [1]['novo_simbolo'], 'a')
        self.assertEqual(test2['transicoes'][0]['fitas'][1]['movimento'], 'R')
        self.assertEqual(test2['transicoes'][0]['fitas']
                         [2]['simbolo_atual'], 'B')
        self.assertEqual(test2['transicoes'][0]['fitas']
                         [2]['novo_simbolo'], 'B')
        self.assertEqual(test2['transicoes'][0]['fitas'][2]['movimento'], 'S')

        self.assertEqual(test2['transicoes'][1]['estado_atual'], '0')
        self.assertEqual(test2['transicoes'][1]['estado_destino'], '1')
        self.assertEqual(len(test2['transicoes'][1]['fitas']), 3)

        self.assertEqual(test2['transicoes'][1]['fitas']
                         [0]['simbolo_atual'], 'B')
        self.assertEqual(test2['transicoes'][1]['fitas']
                         [0]['novo_simbolo'], 'B')
        self.assertEqual(test2['transicoes'][1]['fitas'][0]['movimento'], 'S')
        self.assertEqual(test2['transicoes'][1]['fitas']
                         [1]['simbolo_atual'], 'B')
        self.assertEqual(test2['transicoes'][1]['fitas']
                         [1]['novo_simbolo'], 'B')
        self.assertEqual(test2['transicoes'][1]['fitas'][1]['movimento'], 'L')
        self.assertEqual(test2['transicoes'][1]['fitas']
                         [2]['simbolo_atual'], 'B')
        self.assertEqual(test2['transicoes'][1]['fitas']
                         [2]['novo_simbolo'], 'B')
        self.assertEqual(test2['transicoes'][1]['fitas'][2]['movimento'], 'S')


if __name__ == '__main__':
    unittest.main()
