from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
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
                fila.append(casilla)
            self.casillas.append(fila)


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
        
        # Destruir el widget de la imagen
        imagen_label.destroy()

        tablero = TableroAjedrez(tablero_frame, n)
        tablero.crear_tablero()
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

label = tk.Label(frame, text="Ingrese el numero de Reinas:")
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

# Cargar la imagen y ajustar su tamaño
imagen = Image.open("Imagenes/chees.png")
imagen = imagen.resize((400, 200), Image.ANTIALIAS)  # Ajustar el tamaño de la imagen
imagen = ImageTk.PhotoImage(imagen)

# Mostrar la imagen en el Label
imagen_label = tk.Label(frame, image=imagen)
imagen_label.pack(pady=10) 

# Agregar un marco para contener los botones
botones_frame = tk.Frame(frame)
botones_frame.pack()

# Agregar botones estáticos en el marco de los botones
button1 = tk.Button(botones_frame, text="Cerrar", command=cerrar_aplicacion)
button1.pack(side=tk.LEFT, padx=10)

button2 = tk.Button(botones_frame, text="Minimizar", command=minimizar_ventana)
button2.pack(side=tk.LEFT, padx=10)

root.mainloop()
