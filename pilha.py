class Pilha():
    
    __elementos = []
    __tamanho = 0

    def __init__(self):

        self.__elementos = []
    
    def get_tamanho(self):
        return self.__tamanho
    
    def set_tamanho(self, novoTamanho):
        self.__tamanho = novoTamanho

    def empilha(self, novoElemento):
        self.__elementos.append(novoElemento)

        self.set_tamanho(self.get_tamanho() + 1)
        
        return print(f"novo elemento: >> {novoElemento} << adicionado")
    
    def desempilha(self):
        head = self.__elementos[-1]
        
        del self.__elementos[-1]
        self.set_tamanho(self.get_tamanho() - 1)

        return print(f"elemento >> {head} << removido")
    
    def espia(self):
        if self.__tamanho > 0:
            return print(f">> {self.__elementos[-1]} << esta no topo da pilha")
        else:
            return print("nada no topo")
    
    def showPilha(self):

        n = self.__tamanho

        if n > 0:
            print(20*"=")

            for i in range(n-1, -1, -1):
                print(self.__elementos[i])

            print(20*"=")

    def esta_vazia(self):
        if self.__tamanho == 0:
            return print("a pilha esta vazia")
        else:
            return print("a pilha nao esta vazia")
        
p1 = Pilha()

p1.empilha("primeiro elemento")
p1.empilha("segundo elemento")
p1.empilha("terceiro elemento")
print(f"temos {p1.get_tamanho()} elementos na pilha")
p1.espia()
p1.showPilha()
p1.desempilha()
p1.showPilha()
p1.esta_vazia()