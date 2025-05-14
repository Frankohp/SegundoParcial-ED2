class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def __str__(self):
        return str(self.valor)

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
            return
        nodo_anterior = self.cabeza
        while nodo_anterior.siguiente != self.cabeza:
            nodo_anterior = nodo_anterior.siguiente
        nodo_anterior.siguiente = nuevo_nodo
        nuevo_nodo.siguiente = self.cabeza

    def eliminar(self, valor):
        if not self.cabeza:
            return None
        nodo_actual = self.cabeza
        nodo_anterior = None
        while True:
            if nodo_actual.valor == valor:
                if nodo_anterior:
                    nodo_anterior.siguiente = nodo_actual.siguiente
                else:
                    if nodo_actual.siguiente == self.cabeza:
                        self.cabeza = None
                    else:
                        nodo_anterior = self.cabeza
                        while nodo_anterior.siguiente != self.cabeza:
                            nodo_anterior = nodo_anterior.siguiente
                        nodo_anterior.siguiente = nodo_actual.siguiente
                        self.cabeza = nodo_actual.siguiente
                return valor
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.cabeza:
                break
        return None

    def buscar(self, valor):
        if not self.cabeza:
            return None
        nodo_actual = self.cabeza
        while True:
            if nodo_actual.valor == valor:
                return nodo_actual
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.cabeza:
                break
        return None

    def mostrar(self):
        if not self.cabeza:
            print("Lista vacía")
            return
        nodo_actual = self.cabeza
        print("Lista Circular: ", end="")
        while True:
            print(nodo_actual.valor, end=" -> ")
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.cabeza:
                break
        print("(cabeza)")


