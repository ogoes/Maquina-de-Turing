from estado import *
from transicao import *
from fita import *

class Maquina:
	""""""
	def __init__(self, result, entrada):

		self.alfabeto = result['alfabeto_entrada']
		self.entrada = entrada

		self.listaEstados = [ Estado(i) for i in result['estados'] ]


		estado = Estado(result['estado_inicial'])
		estado.setInicial()

		self.estadoAtual = estado
		self.listaEstados.append(estado)

		for finais in result['estados_finais']:
			for estado in self.listaEstados:
				if estado.getNome() == finais:
					estado.setFinal()


		self.transicoes = []


		for transicoes in result['transicoes']:
			for estado in self.listaEstados:
				if transicoes['estado_atual'] == estado.getNome():
					cur_state = estado
				if transicoes['estado_destino'] == estado.getNome():
					nex_state = estado

			self.transicoes.append(Transicao(cur_state, nex_state, transicoes['fita']['simbolo_atual'], transicoes['fita']['novo_simbolo'], transicoes['fita']['movimento']))

		self.alfabetoFita = result['alfabeto_fita']
		self.__blank = result['simbolo_espaco']
		self.fita = Fita(self.alfabetoFita, self.__blank, self.entrada)


	def __isFinal__(self):
		if self.estadoAtual.isFinal():
			print("Entrada Aceita = \"%s\"" %(self.entrada))
			exit(0)

	def __getTransitions__(self):
		transitions = []

		for transition in self.transicoes:
			if transition.getEstadoAtual() == self.estadoAtual:
				transitions.append(transition)

		if len(transitions) == 0:
			print("Computação interrompida, sem transições")

			return False

		return transitions


	def __mostraFita__(self):
		self.fita.mostraFita()
		print("\nEstado Atual: %s" %(self.estadoAtual.getNome()))

	def run(self):

		last_state = self.listaEstados[-1]
		state_counter = 0

		while True:
			self.__mostraFita__()

			self.__isFinal__()

			transitions = self.__getTransitions__()

			if transitions == False:
				return 1

			pos = self.fita.getPos()
			a = 0

			for transit in transitions:
				if transit.getSimboloAtual() == pos:
					a = 1

					print(self.estadoAtual.getNome(), last_state.getNome())
					

					if self.estadoAtual.getNome() == last_state:
						state_counter += 1

						if state_counter == 1000:
							print('Loop detectado')
							return 1

					else:
						
						state_counter = 0
						last_state = self.estadoAtual

					self.estadoAtual = transit.getNovoEstado()

					novoSimbolo = transit.getNovoSimbolo()
					self.fita.setPos( novoSimbolo )
					
					print("Instrução a ser executada:", transit.getEstadoAtual().getNome(),"-->", transit.getNovoEstado().getNome(), ",", transit.getSimboloAtual(),"-->", transit.getNovoSimbolo(), ",", transit.getMovimento(), "\n")

					movimento = transit.getMovimento()
					if movimento == 'R':
						self.fita.setRight()
					elif movimento == 'L':
						self.fita.setLeft()

			if a == 0:
				print("Computação interrompida, entrada recusada = \"%s\"" %(self.entrada))
				return 0
			

			input()
			# time.sleep(3)
