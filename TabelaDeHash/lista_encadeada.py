class Celula:
	item = None
	proximo = None

	def __init__(self,item):
		self.item = item

class Lista_Encadeada:
	inicio = None
	tamanho = 0

	def __init__(self):
		self.inicio = Celula(None)

	#verificar se tá vazia
	def estaVazia(self):
		return self.tamanho == 0

	#inserir
	def inserir(self,item,pos):
		if pos <= self.tamanho:
			p = self.inicio
			for i in range(pos):
				p = p.proximo
			aux = Celula(item)
			aux.proximo = p.proximo
			p.proximo = aux
			self.tamanho+=1
		else:
			print('operacao invalida')
	
	def inserirF(self,item):
		p = self.inicio
		for i in range(self.tamanho):
			p = p.proximo
		p.proximo = Celula(item)
		self.tamanho+=1

	#remover
	def remover(self,pos):
		if not self.estaVazia() and pos<self.tamanho:
			p = self.inicio
			for i in range(pos):
				p = p.proximo
			aux = p.proximo
			p.proximo = aux.proximo
			item = aux.item
			del aux
			self.tamanho -=1
			return item
		else:
			print('operacao invalida')

	#imprimir
	def imprimir(self):
		p = self.inicio
		for i in range(self.tamanho):
			p = p.proximo
			print(p.item, end = ' ')
		print('')




























