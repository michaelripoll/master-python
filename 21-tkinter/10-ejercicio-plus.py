"""
Calculadora:
- Dos campos de texto
- 4 botones para las operaciones
- Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox

class Calculadora:

    def __init__(self, alertas):
        self.primer_dato = StringVar()
        self.segundo_dato = StringVar()
        self.resultado = StringVar()
        self.alertas = alertas

    def getSuma(self):
        try:
            self.resultado.set(float(self.primer_dato.get()) + float(self.segundo_dato.get()))
            self.mostrarResultado()
        except:
            self.alertas.showerror("Error", "Introduce bien los datos")

    def getResta(self):
        try:
            self.resultado.set(float(self.primer_dato.get()) - float(self.segundo_dato.get()))
            self.mostrarResultado()
        except:
            self.alertas.showerror("Error", "Introduce bien los datos")

    def getMult(self):
        try:
            self.resultado.set(float(self.primer_dato.get()) * float(self.segundo_dato.get()))
            self.mostrarResultado()
        except:
            self.alertas.showerror("Error", "Introduce bien los datos")

    def getDiv(self):
        try:
            self.resultado.set(float(self.primer_dato.get()) / float(self.segundo_dato.get()))
            self.mostrarResultado()
        except:
            self.alertas.showerror("Error", "Introduce bien los datos")

    def mostrarResultado(self):
        self.alertas.showinfo("Resultado", f"El resultado es: {self.resultado.get()}")

ventana = Tk()
ventana.geometry("400x400")
ventana.config(bd=25)

calculadora = Calculadora(messagebox)

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
primer_campo = Entry(marco, textvariable=calculadora.primer_dato, justify="center").pack()

segundo_label = Label(marco, text="Ingrese segundo valor: ").pack()
segundo_campo = Entry(marco, textvariable=calculadora.segundo_dato, justify="center").pack()

Label(marco).pack()

# Botones
Button(marco, text="Suma", command=calculadora.getSuma).pack(side="left", fill=X, expand=YES)
Button(marco, text="Resta", command=calculadora.getResta).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicación", command=calculadora.getMult).pack(side="left", fill=X, expand=YES)
Button(marco, text="División", command=calculadora.getDiv).pack(side="left", fill=X, expand=YES)

ventana.mainloop()