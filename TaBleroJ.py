# Bibliotecas
from tkinter import *
import tkinter as ttk

# Crea ventana raiz
raiz = Tk()

# Crea una forma
frm = ttk.Frame(raiz)
frm.grid(columnspan=8,rowspan=8)
#########################################Jose###################33
# Definir dimensiones del tablero
dimension = 9
casilla_size = 70

# Crea una matriz para representar el tablero
tablero = [[None] * dimension for _ in range(dimension)]

# Colores para las casillas
color1 = "red"
color2 = "black"

# Dibuja el tablero
for fila in range(dimension):
    for columna in range(dimension):
        # Alterna los colores de las casillas
        if (fila + columna) % 2 == 0:
            color = color1
        else:
            color = color2

        # Crea una casilla como un marco
        casilla = ttk.Frame(frm, width=casilla_size, height=casilla_size, background=color)
        casilla.grid(row=fila, column=columna)

        # Agrega la casilla al tablero
        tablero[fila][columna] = casilla

#############################################################################

# Lee imagen
img=PhotoImage(file='Imagenes/reina.png')
img=img.subsample(8)



# Pon cosas en forma
ttk.Label(frm, text='Hola Mundo!').grid(column=0, row=0)

ttk.Button(frm,text='Termina',command=raiz.destroy).grid(column=0, row=5)
ttk.Button(frm,text='Minimiza',command=raiz.iconify).grid(column=2, row=5)

#ttk.Label(frm,image=img).grid(column=1,row=0)
#ttk.Label(frm,image=img).grid(column=2,row=1)
#ttk.Label(frm,image=img).grid(column=3,row=2)
#ttk.Label(frm,image=img).grid(column=4,row=3)
#ttk.Label(frm,image=img).grid(column=1,row=4)
##################################################################33
# Pon una imagen en una casilla específica (fila, columna)
def colocar_imagen(fila, columna):
    ttk.Label(tablero[fila][columna], image=img).pack()

# Ejemplo: Coloca una imagen en la casilla (0, 0)
colocar_imagen(1, 0)
colocar_imagen(2, 1)
colocar_imagen(3, 2)
#####################################################################
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