# Bibliotecas
from tkinter import *
import tkinter as ttk

"""
# Crea ventana raiz
raiz = Tk()

# Crea una forma
frm = ttk.Frame(raiz)
frm.grid(columnspan=5,rowspan=6)

# Lee imagen
img=PhotoImage(file='Imagenes/reina.png')
img=img.subsample(8)


# Pon cosas en forma
ttk.Label(frm, text='Hola Mundo!').grid(column=0, row=0)

ttk.Button(frm,text='Termina',command=raiz.destroy).grid(column=0, row=5)
ttk.Button(frm,text='Minimiza',command=raiz.iconify).grid(column=2, row=5)

ttk.Label(frm,image=img).grid(column=1,row=0)
ttk.Label(frm,image=img).grid(column=2,row=1)
ttk.Label(frm,image=img).grid(column=3,row=2)
ttk.Label(frm,image=img).grid(column=4,row=3)
ttk.Label(frm,image=img).grid(column=1,row=4)

# Lee algo
var = IntVar()

num = ttk.Entry(raiz,width=10,textvariable=var)
num.grid(column=2,row=0)


def imprime(x):
    print(x)
    print(num.get())

num.bind('<Key-Return>',imprime)

# Comando
def comando():
    print(f"Se dio click, num vale '{num.get()}'")

ttk.Button(frm,text='Da click',command=comando).grid(column=4, row=5)

# Haz funcionar todo
raiz.mainloop()

"""



############################################################################################

# Crea ventana raiz
raiz = Tk()

# Lee imagen
img=PhotoImage(file='Imagenes/reina.png')
img=img.subsample(4)

# Crea una forma
frm = ttk.Frame(raiz)

class TableroAjedrez(ttk.Frame):
    def __init__(self, parent, n):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.n = n
        self.casillas = []

        self.crear_tablero()
    
    def crear_tablero(self):
        for i in range(self.n):
            fila = []
            for j in range(self.n):
                color = "white" if (i+j) % 2 == 0 else "brown"
                casilla = ttk.Label(image=img, width=20, height=10, bg=color)
                casilla.grid(row=i, column=j)
                fila.append(casilla)   
            self.casillas.append(fila)
        #casilla1= ttk.Label(image=img).grid(row=1,column=0)
        #casilla.grid(casilla1)


def mostrar_tablero():
    n = int(entry.get())  # Obtener el tamaño del tablero desde la entrada
    tablero = TableroAjedrez(tablero_frame, n)
    tablero.crear_tablero()
    tablero.pack(expand=True, fill="both")




"""
casilla=ttk.Label(image=img).grid(column=1,row=0)
casilla=ttk.Label(image=img).grid(column=2,row=1)
casilla=ttk.Label(image=img).grid(column=3,row=2)
casilla=ttk.Label(image=img).grid(column=4,row=3)
casilla=ttk.Label(image=img).grid(column=1,row=4)
"""


root = ttk.Tk()
root.geometry("500x500")  # Tamaño inicial de la ventana
root.title("Tablero de Ajedrez")

frame = ttk.Frame(root)
frame.pack(expand=True)

label = ttk.Label(frame, text="Ingrese el tamaño del tablero (n):")
label.pack()

entry = ttk.Entry(frame)
entry.pack()

button = ttk.Button(frame, text="Mostrar tablero", command=mostrar_tablero)
button.pack()

# Centrar el tablero en el frame
tablero_frame = ttk.Frame(frame)
tablero_frame.pack(expand=True)
tablero_frame.grid_rowconfigure(0, weight=1)
tablero_frame.grid_columnconfigure(0, weight=1)

root.mainloop()
