from lista_encadeada import *

class TableE:
    m = 0
    table = []

    #criar
    def __init__(self,m):
        self.m = m
        self.table = [None]*m

    def hash(self,x):
        return x % self.m

    #inserir
    def inserir(self,x):
        h = self.hash(x)
        if self.table[h] == None:
            self.table[h] = Lista_Encadeada()
        self.table[h].inserirF(x)

    #remover
    def remover(self,x):
        h = self.hash(x)
        if self.table[h] == None:
            print('nao existe')''
        else:
            self.table[h].remover(x)

    #imprimir
    def imprimir(self):
        for i in range(self.m):
            print(i,' ',end='')
            if self.table[i]!= None:
                self.table[i].imprimir()
            print('')
        print('---')

tabela = TableE(8)
tabela.imprimir()
tabela.inserir(16)
tabela.inserir(23)
tabela.inserir(41)
tabela.inserir(25)
tabela.inserir(39)
tabela.imprimir()












# from lista_encadeada import *

# class HashTableLista:
#     tabela = []
#     m = 0

#     def __init__(self,m):
#         tabela = self.tabela = [None]*m
#         self.m = m

#     def hash(self,x):
#         return x%self.m

#     def inserir(self,x):
#         h = self.hash(x)
#         if self.tabela[h] == None:
#             self.tabela[h] = Lista_Encadeada()
#         self.tabela[h].inserirF(x)

#     def remover(self,x):
#         h = self.hash(x)
#         i = 0
#         while i < self.tabela[h].tamanho and x != 


#     def imprimir(self):
#         for i in range(self.m):
#             if self.tabela[i] != None:
#                 print(i,end=' ')
#                 self.tabela[i].imprimir()
#             else:
#                 print(i,None)
#         print('---')

# ht = HashTableLista(8)
# ht.inserir(16)
# ht.inserir(23)
# ht.inserir(41)
# ht.inserir(25)
# ht.inserir(39)
# ht.imprimir()

# # lista = Lista_Encadeada()
# # lista.inserirF(1)
# # lista.inserirF(2)
# # lista.inserirF(3)
# # lista.inserirF(4)
# # lista.inserirF(5)
# # lista.imprimir()