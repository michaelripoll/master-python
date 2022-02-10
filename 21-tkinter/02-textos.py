from tkinter import *
from tkinter import font

ventana = Tk()
ventana.geometry("700x500")

texto = Label(ventana, text="Bienvenido a mi programa")
texto.config(
        fg="white",
        bg="black",
        padx="20",
        pady="20",
        font=("Arial", 30)
    )
texto.pack()

texto = Label(ventana, text="Soy Michael Ripoll")
texto.config(
        height=3,
        bg="orange",
        font=("Arial", 18),
        padx="10",
        pady="20",
        cursor="circle"
    )
texto.pack(anchor=E)

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais}"

texto = Label(ventana, text=pruebas(pais="Colombia", apellidos="Ripoll Puche", nombre="Michael Alexander"))
texto.config(
        height=5,
        bg="green",
        font=("Arial", 18),
        padx="10",
        pady="20",
        cursor="circle"
    )
texto.pack(anchor=NW)

ventana.mainloop()