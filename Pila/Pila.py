class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cima = None
        self.longitud = 0

    def esta_vacia(self):
        return self.cima is None
    
    def apilar(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo
        self.longitud += 1

############PREGUNTA 2: Método desapilar ###############
    # Método para desapilar un elemento de la pila
    # Desapila el elemento en la cima de la pila y lo devuelve.
    # Si la pila está vacía, lanza una excepción.
    ######################################################










########################################################################
    def ver_cima(self):
        if not self.esta_vacia():
            print("Error: Pila vacía")
            return None
        return self.cima.valor

    def obtener_longitud(self):
        return self.longitud

    def mostrar_pila(self):
        print("\nEstado actual de la pila:")
        actual = self.cima
        if not actual:
            print("|   |")
            print("------")
        else:
            while actual:
                print(f"| {actual.valor} |")
                actual = actual.siguiente
            print("------")