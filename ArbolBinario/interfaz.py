import tkinter as tk
from tkinter import messagebox

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

    def buscar_con_padre(self, valor):
        def _buscar(nodo, padre, valor):
            if nodo is None:
                return None, None
            if nodo.valor == valor:
                return nodo, padre
            elif valor < nodo.valor:
                return _buscar(nodo.izquierda, nodo, valor)
            else:
                return _buscar(nodo.derecha, nodo, valor)

        return _buscar(self.raiz, None, valor)

    def tio(self, t, s):
        nodo_s, padre_s = self.buscar_con_padre(s)
        if not nodo_s or not padre_s:
            return False  # s no existe o no tiene padre

        nodo_t, _ = self.buscar_con_padre(t)
        if not nodo_t:
            return False  # t no existe

        abuelo, _ = self.buscar_con_padre(padre_s.valor)
        if not abuelo:
            return False  # No hay abuelo, por lo que no hay tío

        return (abuelo.izquierda == padre_s and abuelo.derecha == nodo_t) or \
               (abuelo.derecha == padre_s and abuelo.izquierda == nodo_t)

    def inorden(self):
        def _inorden(nodo):
            return _inorden(nodo.izquierda) + [nodo.valor] + _inorden(nodo.derecha) if nodo else []
        return _inorden(self.raiz)

class AppArbol:
    def __init__(self, root):
        self.root = root
        self.root.title("Árbol Binario")
        self.arbol = ArbolBinario()

        self.entrada = tk.Entry(root)
        self.entrada.pack(pady=5)

        botones = tk.Frame(root)
        botones.pack()

        tk.Button(botones, text="Insertar", command=self.insertar).pack(side=tk.LEFT, padx=5)
        tk.Button(botones, text="Buscar", command=self.buscar).pack(side=tk.LEFT, padx=5)
        tk.Button(botones, text="Eliminar", command=self.eliminar).pack(side=tk.LEFT, padx=5)
        tk.Button(botones, text="Mostrar Inorden", command=self.mostrar_inorden).pack(side=tk.LEFT, padx=5)
        tk.Button(botones, text="Verificar Tío", command=self.verificar_tio).pack(side=tk.LEFT, padx=5)

        self.entrada_tio = tk.Entry(root)
        self.entrada_tio.pack(pady=5)
        self.entrada_sobrino = tk.Entry(root)
        self.entrada_sobrino.pack(pady=5)

        tk.Label(root, text="Ingrese el valor de T:").pack()
        self.entrada_tio = tk.Entry(root)
        self.entrada_tio.pack(pady=5)

        tk.Label(root, text="Ingrese el valor de S:").pack()
        self.entrada_sobrino = tk.Entry(root)
        self.entrada_sobrino.pack(pady=5)

        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack(pady=10)

    def insertar(self):
        valor = self.obtener_valor()
        if valor is not None:
            self.arbol.insertar(valor)
            self.redibujar()

    def buscar(self):
        valor = self.obtener_valor()
        if valor is not None:
            encontrado = self.arbol.buscar(valor)
            msg = f"El valor {valor} {'fue encontrado' if encontrado else 'no se encuentra'} en el árbol."
            messagebox.showinfo("Buscar", msg)

    def eliminar(self):
        valor = self.obtener_valor()
        if valor is not None:
            self.arbol.eliminar(valor)
            self.redibujar()

    def mostrar_inorden(self):
        valores = self.arbol.inorden()
        messagebox.showinfo("Recorrido Inorden", " -> ".join(map(str, valores)))

    def verificar_tio(self):
        try:
            t = int(self.entrada_tio.get())
            s = int(self.entrada_sobrino.get())
            es_tio = self.arbol.tio(t, s)
            msg = f"{t} {'es' if es_tio else 'no es'} tío de {s}."
            messagebox.showinfo("Verificación de Tío", msg)
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce números enteros.")

    def obtener_valor(self):
        try:
            return int(self.entrada.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un número entero.")
            return None

    def redibujar(self):
        self.canvas.delete("all")
        if self.arbol.raiz:
            self.dibujar_nodo(self.arbol.raiz, 300, 30, 150)

    def dibujar_nodo(self, nodo, x, y, espaciado):
        if nodo is None:
            return

        radio = 20
        self.canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="lightblue")
        self.canvas.create_text(x, y, text=str(nodo.valor), font=("Arial", 10, "bold"))

        if nodo.izquierda:
            x_izq = x - espaciado
            y_izq = y + 60
            self.canvas.create_line(x, y + radio, x_izq, y_izq - radio)
            self.dibujar_nodo(nodo.izquierda, x_izq, y_izq, espaciado // 2)

        if nodo.derecha:
            x_der = x + espaciado
            y_der = y + 60
            self.canvas.create_line(x, y + radio, x_der, y_der - radio)
            self.dibujar_nodo(nodo.derecha, x_der, y_der, espaciado // 2)

def iniciar_interfaz():
    root = tk.Tk()
    app = AppArbol(root)
    root.mainloop()

if __name__ == "__main__":
    iniciar_interfaz()


