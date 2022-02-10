from tkinter import *

ventana = Tk()
ventana.title("Marcos | Master en python")
ventana.geometry("700x400")

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.pack(side=TOP, anchor=N, fill=X, expand=YES)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="blue",
    bd=5,
    relief="solid"
)

marco.pack(side=LEFT, anchor=NW)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="yellow",
    bd=5,
    relief="solid"
)

marco.pack(side=RIGHT, anchor=NE)

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="red",
    bd=5,
    relief="solid"
)

marco.pack(side=LEFT, anchor=SW)
marco.pack_propagate(False)

texto = Label(marco, text="Primer marco")
texto.config(
    bg="red",
    fg="white",
    font=("Arial", 20)
)
texto.pack(fill=Y, expand=YES)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="green",
    bd=5,
    relief="solid"
)

marco.pack(side=RIGHT, anchor=SE)

ventana.mainloop()