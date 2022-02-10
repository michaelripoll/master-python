"""
Calculadora:
- Dos campos de texto
- 4 botones para las operaciones
- Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.geometry("400x400")
ventana.config(bd=25)

def getSuma():
    resultado.set(float(primer_dato.get()) + float(segundo_dato.get()))
    mostrarResultado()

def getResta():
    resultado.set(float(primer_dato.get()) - float(segundo_dato.get()))
    mostrarResultado()

def getMult():
    resultado.set(float(primer_dato.get()) * float(segundo_dato.get()))
    mostrarResultado()

def getDiv():
    resultado.set(float(primer_dato.get()) / float(segundo_dato.get()))
    mostrarResultado()

def mostrarResultado():
    MessageBox.showinfo("Resultado", f"El resultado es: {resultado.get()}")

primer_dato = StringVar()
segundo_dato = StringVar()
resultado = StringVar()

# Frame
marco = Frame(ventana, width=300, height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

# Campo label
encabezado = Label(marco, text="Calculadora")
encabezado.pack()

# Campo Text
primer_label = Label(marco, text="Ingrese primer valor: ").pack()
primer_campo = Entry(marco, textvariable=primer_dato, justify="center").pack()

segundo_label = Label(marco, text="Ingrese segundo valor: ").pack()
segundo_campo = Entry(marco, textvariable=segundo_dato, justify="center").pack()

Label(marco).pack()

# Botones
Button(marco, text="Suma", command=getSuma).pack(side="left", fill=X, expand=YES)
Button(marco, text="Resta", command=getResta).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicación", command=getMult).pack(side="left", fill=X, expand=YES)
Button(marco, text="División", command=getDiv).pack(side="left", fill=X, expand=YES)

ventana.mainloop()