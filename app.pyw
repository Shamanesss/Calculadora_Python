from tkinter import *
from math import *


root = Tk()
root.title("calculadora")
root.iconbitmap(".\luna.ico")
root.resizable(0, 0)
root.geometry("360x325")


miframe = Frame(root)
miframe.config(bg="Indigo")
miframe.pack()


# ------------pantalla---------------

numPantalla = StringVar()
pantalla = Entry(miframe, textvariable=numPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bd=10, bg="#7B68EE",
                fg="#FFEFD5", justify="right", width=52)


# ---------------funciones-------------------------------------

operador = ""
# Esta funcion acumulara los numeros y las funciones(mediante global y  la variable operador) cada vez que le demos un click


def pulsarBoton(num):
    global operador
    operador = operador+str(num)
    numPantalla.set(operador)

# creamos un sistemas de funciones en las que se llaman unas a otras con la funcion "eval"
# creamos la funcion operacion mediante la funcion eval, para que realica las operaciones establecidas con la funcion anterior
# la funcion boton_total toma la cadena operador la cual cacularesmos mediante eval para almacenar el resultado en la variable operar
# finalmente usamos numPantalla para visualizar lo almacenado en operar


def boton_total():
    global operador
    try:
        operar = eval(operador)
    except:
        clear()
        operar = ("ERROR")
    numPantalla.set(operar)


# para limpiar la pantalla
def clear():
    global operador
    operador = ("")
    numPantalla.set("0")


# ----------fila 1 (-)-exp-C----------
boton7 = Button(miframe, text="(", width=7, pady=10, padx=10,
                bg="#7B68EE", command=lambda: pulsarBoton("("))
boton7.grid(row=2, column=1)
boton8 = Button(miframe, text=")", width=7, pady=10, padx=10,
                bg="#7B68EE", command=lambda: pulsarBoton(")"))
boton8.grid(row=2, column=2)
boton9 = Button(miframe, text="EXP", width=7, pady=10, padx=10,
                bg="#7B68EE", command=lambda: pulsarBoton("**"))
boton9.grid(row=2, column=3)
botondiv = Button(miframe, text="C", width=7, pady=10, padx=10,
                  bg="#7B68EE", command=clear)
botondiv.grid(row=2, column=4)


# -----------fila % ln ------------------

boton4 = Button(miframe, text="%", width=7, pady=10,
                padx=10, bg="#7B68EE", command=lambda: pulsarBoton("%"))
boton4.grid(row=3, column=1)
boton5 = Button(miframe, text="\u221A", width=7, pady=10, padx=10,
                bg="#7B68EE", command=lambda: pulsarBoton("sqrt("))
boton5.grid(row=3, column=2)
boton6 = Button(miframe, text="\u03C0", width=7, pady=10, padx=10,
                bg="#7B68EE", command=lambda: pulsarBoton("\u03C0"))
boton6.grid(row=3, column=3)
botonmult = Button(miframe, text="/", width=7, pady=10, padx=10,
                   bg="#7B68EE", command=lambda: pulsarBoton("/"))
botonmult.grid(row=3, column=4)


# -----------fila 7-8-9- x ------------------

boton1 = Button(miframe, text="7", width=7, pady=10, padx=10,
                bg="#7B68EE", command=lambda: pulsarBoton("7"))
boton1.grid(row=4, column=1)
boton2 = Button(miframe, text="8", width=7, pady=10, padx=10,
                bg="#7B68EE", command=lambda: pulsarBoton("8"))
boton2.grid(row=4, column=2)
boton3 = Button(miframe, text="9", width=7, pady=10, padx=10,
                bg="#7B68EE", command=lambda: pulsarBoton("9"))
boton3.grid(row=4, column=3)
botonresta = Button(miframe, text="*", width=7, pady=10,
                    padx=10, bg="#7B68EE", command=lambda: pulsarBoton("*"))
botonresta.grid(row=4, column=4)

# -----------fila 4-5-6- resta-------------------

botonmas = Button(miframe, text="4", width=7, pady=10, padx=10,
                  bg="#7B68EE", command=lambda: pulsarBoton("4"))
botonmas.grid(row=5, column=1)
boton0 = Button(miframe, text="5", width=7, pady=10, padx=10,
                bg="#7B68EE", command=lambda: pulsarBoton("5"))
boton0.grid(row=5, column=2)
botonpunto = Button(miframe, text="6", width=7, pady=10,
                    padx=10, bg="#7B68EE", command=lambda: pulsarBoton("6"))
botonpunto.grid(row=5, column=3)
botonigual = Button(miframe, text="-", width=7, pady=10,
                    padx=10, bg="#7B68EE", command=lambda: pulsarBoton("-"))
botonigual.grid(row=5, column=4)

# -----------fila 1-2-3-suma-------------------

botonmas = Button(miframe, text="1", width=7, pady=10, padx=10,
                  bg="#7B68EE", command=lambda: pulsarBoton("1"))
botonmas.grid(row=6, column=1)
boton0 = Button(miframe, text="2", width=7, pady=10, padx=10,
                bg="#7B68EE", command=lambda: pulsarBoton("2"))
boton0.grid(row=6, column=2)
botonpunto = Button(miframe, text="3", width=7, pady=10,
                    padx=10, bg="#7B68EE", command=lambda: pulsarBoton("3"))
botonpunto.grid(row=6, column=3)
botonigual = Button(miframe, text="+", width=7, pady=10,
                    padx=10, bg="#7B68EE", command=lambda: pulsarBoton("+"))
botonigual.grid(row=6, column=4)

# -----------fila 4-5-6- resta-------------------

botonmas = Button(miframe, text="Ln", width=7, pady=10, padx=10,
                  bg="#7B68EE", command=lambda: pulsarBoton("log("))
botonmas.grid(row=7, column=1)
boton0 = Button(miframe, text="0", width=7, pady=10, padx=10,
                bg="#7B68EE", command=lambda: pulsarBoton("0"))
boton0.grid(row=7, column=2)
botonpunto = Button(miframe, text=",", width=7, pady=10,
                    padx=10, bg="#7B68EE", command=lambda: pulsarBoton("."))
botonpunto.grid(row=7, column=3)
botonigual = Button(miframe, text="=", width=7, pady=10,
                    padx=10, bg="#7B68EE", command=boton_total)
botonigual.grid(row=7, column=4)


root.mainloop()
