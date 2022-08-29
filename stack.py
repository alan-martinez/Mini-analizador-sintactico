import tipos
class Stack:
    items = []
    def __init__(self):
        self.items = []
        self.push(tipos.SIGNOPESOS)
        self.push(tipos.IDENTIFICADOR)

    def vacio(self):
        return self.items == []

    def push(self, item):
        self.items.insert(len(self.items),item)

    def mostrarPila(self):
        for dato in self.items:
            print(str(dato), end=" ")
        print()

    def clear(self):
        self.items.clear()