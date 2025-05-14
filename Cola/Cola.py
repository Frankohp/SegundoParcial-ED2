class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None  # Nodo al frente de la cola
        self.final = None   # Nodo al final de la cola
        self.longitud = 0

    def esta_vacia(self):
        return self.frente is None

    def encolar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        self.longitud += 1

    def desencolar(self):
        if self.esta_vacia():
            print("Error: Cola vacía")
            return None
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:  # Si la cola queda vacía
            self.final = None
        self.longitud -= 1
        return valor

    def ver_frente(self):
        if self.esta_vacia():
            print("Error: Cola vacía")
            return None
        return self.frente.valor

    def obtener_longitud(self):
        return self.longitud

    def mostrar_cola(self):
        print("\nEstado actual de la cola:")
        actual = self.frente
        if not actual:
            print("|   |")
            print("------")
        else:
            while actual:
                print(f"| {actual.valor} |")
                actual = actual.siguiente
            print("------")

