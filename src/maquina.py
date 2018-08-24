import estado
import transicao
import fita

class Maquina:
	""""""
	def __init__(self, result, entrada):
        
        self.__alfabeto = result['alfabeto_entrada']
        self.__entrada = entrada
        
        self.__listaEstados = [ Estado(i) for i in result['estados'] ]


        estado = Estado(result['estado_inicial'])
        estado.setInicial()
    
        self.estadoAtual = estado
        self.__listaEstados.append(estado)

        for finais in result['estados_finais']:
            for estado in self.__listaEstados:
                if estado.getNome() == finais:
                    estado.setFinal()


        self.__transicoes = []

        for transicoes in result['transicoes']:
            for estado in self.__listaEstados:
                if transicoes['estado_atual'] == estado.getNome():
                    cur_state = estado

            for estado in self.__listaEstados:
                if transicoes['estado_destino'] == estado.getNome():
                    nex_state = estado

            self.__transicoes.append(Transicao(cur_state, nex_state, result['simbolo_atual'], result['novo_simbolo'], result['movimento']))
        

		self.__fita = Fita(self.__alfabetoFita, self.__blank, self.__entrada)
		self.__blank = result['simbolo_espaco']
		self.__alfabetoFita = result['alfabeto_fita']


	def __isFinal__(self):
        if self.__estadoAtual.isFinal():
            print("Entrada Aceita = \"%s\"" %(self.__entrada))
            exit(0)

	def __getTransitions__(self):
		transitions = []

        for transition in self.__transicoes:
            if transition.getEstadoAtual() == self.estadoAtual:
                transitions.append(transition)

		if len(transitions) == 0:
			print("Computação interrompida, sem transições")
			return False

		return transitions


	def __mostraFita__(self):
		self.__fita.mostraFita()
		print("\nEstado Atual: %c" %(self.__estadoAtual.getNome()))

	def run(self):

		last_state = -1
		state_counter = 0

		while True:
			self.__mostraFita__()

			self.__isFinal__()

			transitions = self.__getTransitions__()

            if transitions == False:
                return 1

			pos = self.__fita.getPos()
			a = 0

			for transit in transitions:
					if transit.getSimboloAtual() == pos:
						a = 1

						print(self.__estadoAtual.getNome(), last_state)
						

						if self.__estadoAtual.getNome() == last_state:
							state_counter += 1

							if state_counter == 1000:
								print('Loop detectado')
								return 1

						else:
							
							state_counter = 0
							last_state = self.__estadoAtual

						self.__estadoAtual = transit.getNovoEstado()

						novoSimbolo = transit.getNovoSimbolo()
						self.__fita.setPos( novoSimbolo )
						
						print("Instrução a ser executada:", transit.getEstadoAtual().getNome(),"-->", transit.getNovoEstado().getNome(), ",", transit.getSimboloAtual(),"-->", transit.getNovoSimbolo(), ",", transit.getMovimento(), "\n")

						movimento = transit.getMovimento()
						if movimento == 'R':
							self.__fita.setRight()
						elif movimento == 'L':
							self.__fita.setLeft()

			if a == 0:
				print("Computação interrompida, entrada recusada = \"%s\"" %(self.__entrada))
				return 0
			

			input()
			# time.sleep(3)
