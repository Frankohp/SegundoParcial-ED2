import tkinter as tk
from tkinter import messagebox
from .arbol_binario import ArbolBinario


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

