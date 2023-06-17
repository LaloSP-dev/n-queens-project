from tkinter import *
import tkinter as tk
from tkinter import messagebox

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
                casilla.update()  # Actualizar la casilla para obtener su tamaño
                fila.append(casilla)
            self.casillas.append(fila)

    def agregar_reina(self, fila, columna):
        imagen_path = "Imagenes/reina.png"
        imagen = tk.PhotoImage(file=imagen_path)

        # Ajustar el tamaño de la imagen al tamaño de la casilla
        ancho_casilla = self.casillas[0][0].winfo_width()
        alto_casilla = self.casillas[0][0].winfo_height()
        imagen = imagen.subsample(ancho_casilla // 2, alto_casilla // 2)

        imagen_label = tk.Label(self, image=imagen)
        imagen_label.image = imagen
        imagen_label.grid(row=fila, column=columna)



def mostrar_tablero():
    n = int(entry.get())  # Obtener el tamaño del tablero desde la entrada
    if n < 4:
        messagebox.showerror("Error", "El tamaño mínimo del tablero es 4.")
    elif n > 15:
        messagebox.showerror("Error", "El tamaño máximo del tablero es 15.")
    else:
        # Limpiar el contenido del marco del tablero
        for widget in tablero_frame.winfo_children():
            widget.destroy()
        
        tablero = TableroAjedrez(tablero_frame, n)
        tablero.crear_tablero()
        tablero.agregar_reina(0, 0)  # Agregar la reina en la casilla (0, 0)
        tablero.agregar_reina(1, 1)
        tablero.agregar_reina(2, 2)
        tablero.agregar_reina(3, 3)
        tablero.pack(expand=True, fill="both")

def cerrar_aplicacion():
    root.destroy()

def minimizar_ventana():
    root.iconify()

root = tk.Tk()
root.geometry("500x500")  # Tamaño inicial de la ventana
root.title("Problema de las N Reinas")

frame = tk.Frame(root)
frame.pack(expand=True)

label = tk.Label(frame, text="Ingrese el número de Reinas:")
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

# Cargar la imagen
imagen_path = "Imagenes/chees.png"
imagen = tk.PhotoImage(file=imagen_path)

# Ajustar el tamaño de la imagen
imagen = imagen.subsample(8)  # Dividir el tamaño de la imagen por 2

# Mostrar la imagen en el Label
imagen_label = tk.Label(tablero_frame, image=imagen)
imagen_label.pack(pady=10)

# Agregar un frame para los botones
botones_frame = tk.Frame(frame)
botones_frame.pack()

# Se ponen los botones en estatico
button1 = tk.Button(botones_frame, text="Cerrar", command=cerrar_aplicacion)
button1.pack(side=tk.LEFT, padx=10)

button2 = tk.Button(botones_frame, text="Minimizar", command=minimizar_ventana)
button2.pack(side=tk.LEFT, padx=10)

root.mainloop()
