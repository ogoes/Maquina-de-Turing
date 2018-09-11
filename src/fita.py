
class Fita:
	""""""
	def __init__(self, alfabeto, blank, entrada): ## classe, atributos e metodos de fita
		self.__alfabeto = alfabeto
		self.__blank = blank
		self.__fita = [blank, blank, blank]
		self.__posicao = 3

		self.__fita[ len(self.__fita): ] = [ent for ent in entrada]
		self.__fita[ len(self.__fita): ] = [blank, blank, blank]

	def set_pos(self, caractere): ## seta um caractere na posicao atual da cabeça de leitura
		if not any(caractere == carac for carac in self.__alfabeto):
			print("caractere inválido")
		else:
			self.__fita[self.__posicao] = caractere


	def get_pos(self): ## pega o caractere da posição onde a cabeça de leitura esta
		return self.__fita[self.__posicao]



	def set_right(self): ## move a cabeça de leitura para direita
		if self.__posicao == len(self.__fita)-1:
			self.__fita[ len(self.__fita): ] = [self.__blank, self.__blank, self.__blank]

		self.__posicao += 1


	def set_left(self): ## move a cabeça de leitura para esquerda
		if self.__posicao == 0:
			fitaAux = [self.__blank, self.__blank, self.__blank]
			fitaAux[ len(fitaAux): ] = self.__fita
			self.__fita = fitaAux
			self.__posicao = 3

		self.__posicao -= 1

	def mostra_fita(self): ## mostra a situação atual da fita

		print("··· ", end='')
		for i in range(len(self.__fita)):
			if i == self.__posicao:
				print("\033[40m", "\033[1m", "\033[36;2m", self.__fita[i], '\033[0;0m', end=' ', sep='')
			else:
				print(self.__fita[i], end=' ')
		print("···")

