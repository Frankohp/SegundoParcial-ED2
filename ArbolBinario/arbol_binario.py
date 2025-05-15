class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        def _insertar(nodo, valor):
            if nodo is None:
                return Nodo(valor)
            if valor < nodo.valor:
                nodo.izquierda = _insertar(nodo.izquierda, valor)
            else:
                nodo.derecha = _insertar(nodo.derecha, valor)
            return nodo

        self.raiz = _insertar(self.raiz, valor)

    def buscar(self, valor):
        def _buscar(nodo, valor):
            if nodo is None:
                return False
            if nodo.valor == valor:
                return True
            elif valor < nodo.valor:
                return _buscar(nodo.izquierda, valor)
            else:
                return _buscar(nodo.derecha, valor)
        return _buscar(self.raiz, valor)

    def eliminar(self, valor):
        def _eliminar(nodo, valor):
            if nodo is None:
                return None
            if valor < nodo.valor:
                nodo.izquierda = _eliminar(nodo.izquierda, valor)
            elif valor > nodo.valor:
                nodo.derecha = _eliminar(nodo.derecha, valor)
            else:
                if nodo.izquierda is None:
                    return nodo.derecha
                elif nodo.derecha is None:
                    return nodo.izquierda
                temp = nodo.derecha
                while temp.izquierda:
                    temp = temp.izquierda
                nodo.valor = temp.valor
                nodo.derecha = _eliminar(nodo.derecha, temp.valor)
            return nodo
        self.raiz = _eliminar(self.raiz, valor)

    def inorden(self):
        def _inorden(nodo):
            return _inorden(nodo.izquierda) + [nodo.valor] + _inorden(nodo.derecha) if nodo else []
        return _inorden(self.raiz)
    
    def tio(self, t, s):
        nodo_s, padre_s = self.buscar_con_padre(s)
        if not nodo_s or not padre_s:
            return False 

        nodo_t, _ = self.buscar_con_padre(t)
        if not nodo_t:
            return False 

        abuelo, _ = self.buscar_con_padre(padre_s.valor)
        if not abuelo:
            return False 

        return (abuelo.izquierda == padre_s and abuelo.derecha == nodo_t) or \
               (abuelo.derecha == padre_s and abuelo.izquierda == nodo_t)
    

