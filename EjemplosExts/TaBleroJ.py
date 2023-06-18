# Bibliotecas
from tkinter import *
import tkinter as ttk

# Crea ventana raiz
raiz = Tk()
raiz.geometry("1200x720")

# Crea una forma
frm = ttk.Frame(raiz)
frm.grid(columnspan=3,rowspan=3)
#########################################Jose###################
casillas = []

def dibujar_tablero(num):
    # Definir dimensiones del tablero
    #dimension = 9
    casilla_size = 70

    # Crea una matriz para representar el tablero
    #tablero = [[None] * dimension for _ in range(dimension)]
    tablero = [[None] * num for _ in range(num)]

    # Colores para las casillas
    color1 = "red"
    color2 = "black"

    # Dibuja el tablero
    for fila in range(num):
        for columna in range(num):
            # Alterna los colores de las casillas
            if (fila + columna) % 2 == 0:
                color = color1
            else:
                color = color2

            # Crea una casilla como un marco
            casilla = ttk.Frame(frm, width=casilla_size, height=casilla_size, background=color)
            casillas.append(casilla)
            casilla.grid(row=fila+8, column=columna+8)

            # Agrega la casilla al tablero
            tablero[fila][columna] = casilla
   
    # Pon una imagen en una casilla específica (fila, columna)
    def colocar_imagen(fila, columna):
        ttk.Label(tablero[fila][columna], image=img).pack()

    # Ejemplo: Coloca una imagen en la casilla (0, 0)
    colocar_imagen(0, 0)
    colocar_imagen(1, 1)
    colocar_imagen(2, 2)
    colocar_imagen(3, 3)


#############################################################################

# Lee imagen
img=PhotoImage(file='Imagenes/reina.png')
img=img.subsample(9)



# Pon cosas en forma
ttk.Label(frm, text='Ingresa el numero de reinas').grid(column=0, row=0)

ttk.Button(frm,text='Termina',command=raiz.destroy).grid(column=0, row=5)
ttk.Button(frm,text='Minimiza',command=raiz.iconify).grid(column=2, row=5)

#ttk.Label(frm,image=img).grid(column=1,row=0)
#ttk.Label(frm,image=img).grid(column=2,row=1)
#ttk.Label(frm,image=img).grid(column=3,row=2)
#ttk.Label(frm,image=img).grid(column=4,row=3)
#ttk.Label(frm,image=img).grid(column=1,row=4)

# Lee algo
var = IntVar()

num = ttk.Entry(frm,width=10,textvariable=var)
num.grid(column=2,row=0)


def imprime(x):
    print(x)
    print(num.get())

num.bind('<Key-Return>',imprime)

##############################################3
def limpiar_tablero():
    for casilla in casillas:
        casilla.destroy()
    casillas.clear()
###############################################3

# Comando
def comando():
    limpiar_tablero()
    valor = int(num.get())
    print(f"Se dio click, num vale '{num.get()}'")
    dibujar_tablero(valor)

ttk.Button(frm,text='Da click',command=comando).grid(column=5, row=6)

# Haz funcionar todo
raiz.mainloop()