
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

