class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

    def __str__(self):
        return str(self.valor)
    
class ListaSimple:
    def __init__(self):
        self.cabeza = None
        self.longitud = 0

    def esta_vacia(self):
        return self.cabeza == None

    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        self.longitud += 1

############PREGUNTA 1: Método insertar_final ###########
    # Método para insertar un nodo al final de la lista
def insertar_final(self, valor):
    nuevo_nodo = Nodo(valor)
    if self.esta_vacia():
        self.cabeza = nuevo_nodo
    else:
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo
    self.longitud += 1
########################################################
    def eliminar_inicio(self):
        if self.esta_vacia():
            raise ValueError("No se puede eliminar de una lista vacía")
        
        valor = self.cabeza.valor
        self.cabeza = self.cabeza.siguiente
        self.longitud -= 1
        return valor
    
    def eliminar_final(self):
        if self.esta_vacia():
            raise ValueError("No se puede eliminar de una lista vacía")
        
        if self.cabeza.siguiente is None:
            valor = self.cabeza.valor
            self.cabeza = None
            self.longitud -= 1
            return valor
        
        actual = self.cabeza
        while actual.siguiente.siguiente:
            actual = actual.siguiente
        
        valor = actual.siguiente.valor
        actual.siguiente = None
        self.longitud -= 1
        return valor
    
    def buscar(self, valor):
        """Busca un valor en la lista y devuelve su posición."""
        actual = self.cabeza
        posicion = 0
        
        while actual:
            if actual.valor == valor:
                return posicion
            actual = actual.siguiente
            posicion += 1
        
        return -1

    def obtener_longitud(self):
        return self.longitud

    def eliminar(self, valor):
        if self.esta_vacia():
            print("Advertencia: Lista vacía. No se puede eliminar.")
            return None
    # Caso especial: eliminar el primer nodo
        if self.cabeza.valor == valor:
            valor_eliminado = self.cabeza.valor
            self.cabeza = self.cabeza.siguiente
            self.longitud -= 1
            return valor_eliminado
    # Búsqueda del nodo a eliminar
        anterior = self.cabeza
        while anterior.siguiente is not None:
            if anterior.siguiente.valor == valor:
                valor_eliminado = anterior.siguiente.valor
                anterior.siguiente = anterior.siguiente.siguiente
                self.longitud -= 1
                return valor_eliminado
            anterior = anterior.siguiente
        print(f"Advertencia: El valor {valor} no existe en la lista.")
        return None
    
    def mostrar(self):
        if self.esta_vacia():
            print("Lista vacía -> None")
            return
        actual = self.cabeza

        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    def __str__(self):
        """Representación de cadena para la lista"""
        if self.esta_vacia():
            return "None"
            
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.valor))
            actual = actual.siguiente
        return " -> ".join(elementos) + " -> None"