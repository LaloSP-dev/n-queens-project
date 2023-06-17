from tkinter import *
import tkinter as tk

class TableroAjedrez(tk.Frame):

    def __init__(self, parent, n):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.n = n
        self.casillas = []

        self.crear_tablero()
    
    def crear_tablero(self):
        for i in range(self.n):
            fila = []
            for j in range(self.n):
                color = "white" if (i+j) % 2 == 0 else "brown"
                casilla = tk.Label(self, width=4, height=2, bg=color)
                casilla.grid(row=i, column=j)
                fila.append(casilla)
            self.casillas.append(fila)


def mostrar_tablero():
    n = int(entry.get())  # Obtener el tamaño del tablero desde la entrada
    tablero = TableroAjedrez(tablero_frame, n)
    tablero.crear_tablero()
    tablero.pack(expand=True, fill="both")

def cerrar_aplicacion():
    root.destroy()

def minimizar_ventana():
    root.iconify()


root = tk.Tk()
root.geometry("500x500")  # Tamaño inicial de la ventana
root.title("Tablero de Ajedrez")

frame = tk.Frame(root)
frame.pack(expand=True)

label = tk.Label(frame, text="Ingrese el tamaño del tablero (n):")
label.pack()

entry = tk.Entry(frame)
entry.pack()

button = tk.Button(frame, text="Mostrar tablero", command=mostrar_tablero)
button.pack()

# Centrar el tablero en el frame
tablero_frame = tk.Frame(frame)
tablero_frame.pack(expand=True)
tablero_frame.grid_rowconfigure(0, weight=1)
tablero_frame.grid_columnconfigure(0, weight=1)

# Agregar botones estáticos con separación
button1 = tk.Button(frame, text="Cerrar", command=cerrar_aplicacion)
button1.pack(side=tk.LEFT, padx=10)

button2 = tk.Button(frame, text="Minimizar", command=minimizar_ventana)
button2.pack(side=tk.LEFT, padx=10)


root.mainloop()
