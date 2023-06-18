# Bibliotecas
from tkinter import *
import tkinter as ttk

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