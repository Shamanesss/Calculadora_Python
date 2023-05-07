from tkinter import *

root = Tk()
root.title("calculadora")
root.iconbitmap(".\luna.ico")
root.resizable(0, 0)


miframe = Frame(root)
miframe.config(bg="Indigo")


miframe.pack()

operacion = ""
resultado = 0
# ------------pantalla---------------
numPantalla = StringVar()

pantalla = Entry(miframe, textvariable=numPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="#7B68EE", fg="#FFEFD5", justify="right", width=28)


# ----funciones para pulsar los numero
def numPulsado(num):
    global operacion
    if operacion != '':
        numPantalla.set(num)
        operacion = ''
    else:
        numPantalla.set(numPantalla.get() + num)

# -------funciones----------------------


def suma(num):
    global operacion
    global resultado
    resultado += int(num)
    operacion = "suma"
    numPantalla.set(resultado)


def pulsarIgual():
    global resultado
    numPantalla.set(resultado+int(numPantalla.get()))
    resultado = 0


# ----------fila 1 7-8-9-X----------
boton7 = Button(miframe, text="7", width=3, pady=10, padx=10,
                bg="#7B68EE", command=lambda: numPulsado("7"))
boton7.grid(row=2, column=1)
boton8 = Button(miframe, text="8", width=3, pady=10, padx=10,
                bg="#7B68EE", command=lambda: numPulsado("8"))
boton8.grid(row=2, column=2)
boton9 = Button(miframe, text="9", width=3, pady=10, padx=10,
                bg="#7B68EE", command=lambda: numPulsado("9"))
boton9.grid(row=2, column=3)
botondiv = Button(miframe, text="/", width=3, pady=10, padx=10,
                  bg="#7B68EE", command=lambda: numPulsado("/"))
botondiv.grid(row=2, column=4)


# -----------fila 3 4-5-6-X-------------------

boton4 = Button(miframe, text="4", width=3, pady=10,
                padx=10, bg="#7B68EE", command=lambda: numPulsado("4"))
boton4.grid(row=3, column=1)
boton5 = Button(miframe, text="5", width=3, pady=10, padx=10,
                bg="#7B68EE", command=lambda: numPulsado("5"))
boton5.grid(row=3, column=2)
boton6 = Button(miframe, text="6", width=3, pady=10, padx=10,
                bg="#7B68EE", command=lambda: numPulsado("6"))
boton6.grid(row=3, column=3)
botonmult = Button(miframe, text="X", width=3, pady=10, padx=10,
                   bg="#7B68EE", command=lambda: numPulsado("X"))
botonmult.grid(row=3, column=4)


# -----------fila 3 1-2-3- resta ------------------

boton1 = Button(miframe, text="1", width=3, pady=10, padx=10,
                bg="#7B68EE", command=lambda: numPulsado("1"))
boton1.grid(row=4, column=1)
boton2 = Button(miframe, text="2", width=3, pady=10, padx=10,
                bg="#7B68EE", command=lambda: numPulsado("2"))
boton2.grid(row=4, column=2)
boton3 = Button(miframe, text="3", width=3, pady=10, padx=10,
                bg="#7B68EE", command=lambda: numPulsado("3"))
boton3.grid(row=4, column=3)
botonresta = Button(miframe, text="-", width=3, pady=10,
                    padx=10, bg="#7B68EE", command=lambda: numPulsado("-"))
botonresta.grid(row=4, column=4)

# -----------fila 4 sumar e igual y 0-------------------

botonmas = Button(miframe, text="+", width=3, pady=10, padx=10,
                  bg="#7B68EE", command=lambda: suma(numPantalla.get()))
botonmas.grid(row=5, column=4)
boton0 = Button(miframe, text="0", width=3, pady=10, padx=10,
                bg="#7B68EE", command=lambda: numPulsado("0"))
boton0.grid(row=5, column=2)
botonpunto = Button(miframe, text=",", width=3, pady=10,
                    padx=10, bg="#7B68EE", command=lambda: numPulsado("."))
botonpunto.grid(row=5, column=1)
botonigual = Button(miframe, text="=", width=3, pady=10,
                    padx=10, bg="#7B68EE", command=lambda: pulsarIgual())
botonigual.grid(row=5, column=3)


root.mainloop()
