from cgitb import text
from textwrap import shorten
from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(bd=70)

def sacarAlerta():
    MessageBox.showinfo("Alerta", "Hola, soy Michael Ripoll")

Button(ventana, text="Mostrar alerta!", command=sacarAlerta).pack()

def salir(nombre):
   resultado = MessageBox.askquestion("Salir", "¿Continuar ejecutando la aplicacion?")

   if resultado != "yes":
       MessageBox.showinfo("Chao!", f"Adios {nombre}")
       ventana.destroy()

Button(ventana, text="Salir", command=lambda: salir("Michael Ripoll")).pack()

ventana.mainloop()