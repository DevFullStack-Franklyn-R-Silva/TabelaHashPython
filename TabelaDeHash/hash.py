class Table:
    table = []
    m = 0
    tamanho = 0

    #criar
    def __init__(self, m):
        self.table = [('L','')]*m
        self.m = m
        
    #verificar se esta cheia
    def estaCheia(self):
        return self.tamanho == self.m

    def estaVazia(self):
        return self.tamanho == 0

    def hash(self,x):
        return x % self.m

    #inserir
    def inserir(self,x):
        if not self.estaCheia():
            h = self.hash(x)
            if self.table[h][0] != 'O':
                self.table[h] = ('O',x)
                self.tamanho +=1
            else:
                j = 1
                while self.table[self.hash(h+j)][0] == 'O':
                    j +=1
                self.table[self.hash(h+j)] = ('O',x)
                self.tamanho +=1

    #retirar
    def remover(self,x):
        if not self.estaVazia():
            h = self.hash(x)
            if self.table[h][1] == x:
                self.table[h] = ('R','')
                self.tamanho -=1
            else:
                j = 1
                while j < self.m and self.table[self.hash(h+j)][0]!='L' and self.table[self.hash(h+j)][1]!=x:
                    j+=1
                if j == self.m or self.table[self.hash(h+j)][0]=='L':
                    print('elemento nao existe')
                else:
                    self.table[self.hash(h+j)] = ('R','')
                    self.tamanho -=1

    #imprimir
    def imprimir(self):
        for i in range(self.m):
            print(i,'|',self.table[i][0],'|',self.table[i][1])
        print('---')

tabela = Table(8)
tabela.imprimir()
tabela.inserir(16)
tabela.inserir(23)
tabela.inserir(41)
tabela.inserir(25)
tabela.inserir(39)
tabela.imprimir()
tabela.remover(41)
tabela.remover(23)
tabela.remover(62)
tabela.remover(25)
tabela.remover(39)
tabela.imprimir()










# class HashTable:
#     table = None
#     m = None

#     def __init__(self, m):
#         self.table = [('L','')] * m
#         self.m = m

#     def imprimir(self):
#         for i in range(self.m):
#             print(i,'|',self.table[i][0],'|',self.table[i][1])
#         print('------')

#     def hash(self,x):
#         return x % self.m

#     def inserir(self,x):
#         h = self.hash(x)
#         if self.table[h][0] == 'L':
#             self.table[h] = ('O',x)
#         else:
#             j = 0
#             while j<self.m and self.table[(h+j)%self.m][0]!='L':
#                 j+=1
#             if j==self.m:
#                 print('tabela cheia')
#             else:
#                 self.table[(h+j)%self.m] = ('O',x)
        
#     def remover(self,x):
#         h = self.hash(x)
#         if self.table[h][1] == x:
#             self.table[h] = ('R','')
#         else:
#             j = 0
#             while j<self.m and self.table[(h+j)%self.m][0] != 'L' and self.table[(h+j)%self.m][1] != x:
#                 print(self.table[(h+j)%self.m])
#                 j+=1
#             if self.table[(h+j)%self.m][1] == x:
#                 self.table[(h+j)%self.m] = ('R','')
#             else:
#                 print('elemento não existe')


# hash = HashTable(8)
# hash.imprimir()
# hash.inserir(16)
# hash.inserir(23)
# hash.inserir(41)
# hash.inserir(25)
# hash.inserir(39)
# # hash.inserir(22)
# # hash.inserir(55)
# # hash.inserir(44)
# # hash.inserir(7)
# hash.imprimir()
# hash.remover(41)
# hash.remover(23)
# hash.remover(25)
# hash.inserir(34)
# hash.imprimir()










































# # class HashTable:
# #     tabela = []
# #     m = 0

# #     def __init__(self,m):
# #         self.tabela = [('L',None)]*m
# #         self.m = m

# #     def hash(self,x):
# #         return x%self.m

# #     def inserir(self,x):
# #         h = self.hash(x)
# #         if self.tabela[h][0] != 'O':
# #             self.tabela[h] = ('O',x)
# #         elif self.tabela[h][0] == 'O':
# #             j = 0
# #             while self.tabela[(h+j)%self.m][0] == 'O' and j <= self.m:
# #                 j+=1
# #             if self.tabela[(h+j)%self.m][0] != 'O':
# #                 self.tabela[(h+j)%self.m] = ('O',x)
# #             else:
# #                 print('tabela cheia')
                
# #     def remover(self,x):
# #         h = self.hash(x)
# #         if self.tabela[h][1] == x:
# #             self.tabela[h] = ('R',None)
# #         else:
# #             j = 0
# #             while self.tabela[(h+j)%self.m][0] != 'L' and x !=  self.tabela[(h+j)%self.m][1]:
# #                 j+=1
# #             if x == self.tabela[(h+j)%self.m][1]:
# #                 self.tabela[(h+j)%self.m] = ('R',None)
# #             else:
# #                 print('valor não existe')

# #     def imprimir(self):
# #         for i in range(self.m):
# #             print(self.tabela[i][0],self.tabela[i][1])
# #         print('---')


# # ht = HashTable(8)
# # ht.inserir(16)
# # ht.inserir(23)
# # ht.inserir(41)
# # ht.inserir(25)
# # ht.inserir(39)
# # ht.imprimir()
# # ht.remover(41)
# # ht.remover(23)
# # ht.remover(25)
# # ht.imprimir()
# # ht.inserir(34)
# # ht.imprimir()
