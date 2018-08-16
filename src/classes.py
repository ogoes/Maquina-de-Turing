import time


class Machine:
	""""""
	def __init__(self, result, entrada):
		self.__alfabeto = result['alfabeto_entrada']
		self.__entrada = entrada
		
		self.__listaEstados = result['estados']
		self.__estadoInicial = result['estado_inicial']
		self.__estadoAtual = result['estado_inicial']
		self.__estadoFinal = result['estados_finais']
		self.__transicoes = result['transicoes']
		self.__estados = []

		self.__fitas = []
		self.__qtFitas = result['qt_fitas']
		self.__blank = result['simbolo_espaco']
		self.__alfabetoFita = result['alfabeto_fita']

		for i in range(self.__qtFitas):
			fitaAux = Fita(self.__alfabetoFita, self.__blank, self.__entrada)
			self.__fitas.append(fitaAux)


	def __isFinal__(self):
		for finals in self.__estadoFinal:
			if self.__estadoAtual == finals:
				print("Entrada Aceita = \"%s\"" %(self.__entrada))
				exit(0)

	def __getTransitions__(self):
		transitions = []

		for transi in self.__transicoes:
			if transi['estado_atual'] == self.__estadoAtual:
				transitions.append(transi)

		if len(transitions) == 0:
			print("Computação interrompida, sem transições")
			exit(1)

		return transitions


	def __mostraFitas__(self):
		for i in range(len(self.__fitas)):
			print("Fita [%i]" %(i), sep='', end='\t\t\t\t')
			self.__fitas[i].mostraFita()
			
		print("\nEstado Atual: %c" %(self.__estadoAtual))




	def run(self):


		while True:
			self.__mostraFitas__()

			self.__isFinal__()

			transitions = self.__getTransitions__()

			pos = []
			for fita in self.__fitas:
				pos.append(fita.getPos())

			a = 0



			for transit in transitions:
				for i in range( self.__qtFitas ):
					if transit['fitas'][i]['simbolo_atual'] == pos[i]:
						a = 1
						self.__estadoAtual = transit['estado_destino']

						novoSimbolo = transit['fitas'][i]['novo_simbolo']
						self.__fitas[i].setPos( novoSimbolo )
						print("Fita", i)
						print("Instrução a ser executada:", transit['estado_atual'],"-->", transit['estado_destino'], ",", transit['fitas'][i]['simbolo_atual'],"-->", transit['fitas'][i]['novo_simbolo'], ",", transit['fitas'][i]['movimento'], "\n")

						movimento = transit['fitas'][i]['movimento']
						if movimento == 'R':
							self.__fitas[i].setRight()
						elif movimento == 'L':
							self.__fitas[i].setLeft()

			if a == 0:
				print("Computação interrompida, entrada recusada = \"%s\"" %(self.__entrada))
				exit(1)
			

			input()
			# time.sleep(3)



class Fita:
	""""""
	def __init__(self, alfabeto, blank, entrada):
		self.__alfabeto = alfabeto
		self.__blank = blank
		self.__fita = [blank, blank, blank]
		self.__posicao = 3

		self.__fita[ len(self.__fita): ] = [ent for ent in entrada]
		self.__fita[ len(self.__fita): ] = [blank, blank, blank]

	def setPos(self, caractere):
		if not any(caractere == carac for carac in self.__alfabeto):
			print("caractere inválido")
		else:
			self.__fita[self.__posicao] = caractere


	def getPos(self):
		return self.__fita[self.__posicao]



	def setRight(self):
		if self.__posicao == len(self.__fita)-1:
			self.__fita[ len(self.__fita): ] = [self.__blank, self.__blank, self.__blank]

		self.__posicao += 1


	def setLeft(self):
		if self.__posicao == 0:
			fitaAux = [self.__blank, self.__blank, self.__blank]
			fitaAux[ len(fitaAux): ] = self.__fita
			self.__fita = fitaAux
			self.__posicao = 3

		self.__posicao -= 1

	def mostraFita(self):

		print("··· ", end='')
		for i in range(len(self.__fita)):
			if i == self.__posicao:
				print("\033[40m", "\033[1m", "\033[36;2m", self.__fita[i], '\033[0;0m', end=' ', sep='')
			else:
				print(self.__fita[i], end=' ')
		print("···")




if __name__ == "__main__":
	print("Arquivo principal: \"main.py\"")
