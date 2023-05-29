class Fila():

    __elementos = []
    __tamanho = 0

    def __init__(self):
        self.__elementos = []

    def get_tamanho(self):
        return self.__tamanho
    
    def set_tamanho(self, novoTamanho):
        self.__tamanho = novoTamanho

    def enfileire(self, novoElemento):
        aux = [novoElemento]

        for el in self.__elementos:
            aux.append(el)

        self.__elementos = aux
        self.set_tamanho(self.get_tamanho() + 1)

    def desenfileire(self):
        tail = self.__elementos[-1]
        del self.__elementos[-1]

        self.set_tamanho(self.get_tamanho() - 1)

        return tail
    
    def showFila(self):

        print(80*"=")
        print(self.__elementos)
        print(80*"=")

    def espia(self):
        tail = self.__elementos[-1]

        return tail


f1 = Fila()

f1.enfileire("primeiro")
f1.enfileire("segundo")
f1.enfileire("terceiro")
primeiro_da_fila = f1.espia()

print(f"Primeiro elemento da fila: {primeiro_da_fila}", f"\nTamanho atual da fila: {f1.get_tamanho()}")

f1.showFila()




# OUTRO MODO DE FAZER O METODO showFila

'''     n = self.__tamanho

        print(80*"=")
        for i in range(n):
            print(self.__elementos[i], end= " ")
        print()
        print(80*"=")                               '''