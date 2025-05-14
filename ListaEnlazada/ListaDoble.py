class NodoDoble:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return str(self.valor)
    
class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.longitud = 0

    def insertar_inicio(self, valor):
        nuevo = NodoDoble(valor)
        if not self.cabeza:
            self.cabeza = self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        self.longitud += 1

    def insertar_final(self, valor):
        nuevo = NodoDoble(valor)
        if not self.cola:
            self.cabeza = self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo
        self.longitud += 1

    def eliminar_inicio(self):
        if not self.cabeza:
            return None
        valor = self.cabeza.valor
        self.cabeza = self.cabeza.siguiente
        if self.cabeza:
            self.cabeza.anterior = None
        else:
            self.cola = None
        self.longitud -= 1
        return valor
    
    def eliminar_final(self):
        if not self.cola:
            return None
        valor = self.cola.valor
        self.cola = self.cola.anterior
        if self.cola:
            self.cola.siguiente = None
        else:
            self.cabeza = None
        self.longitud -= 1
        return valor

    def eliminar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                if actual == self.cabeza:
                    self.cabeza = actual.siguiente
                if actual == self.cola:
                    self.cola = actual.anterior
                return
            actual = actual.siguiente
        return None

    def mostrar_inverso(self):
        actual = self.cola
        while actual:
            print(actual.valor, end=" ↔ ")
            actual = actual.anterior
        print("None")

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" ↔ ")
            actual = actual.siguiente
        print("None")
