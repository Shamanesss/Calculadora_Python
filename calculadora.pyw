from tkinter import *

root = Tk()
root.title("calculadora")
root.iconbitmap(".\luna.ico")
root.resizable(0, 0)


miframe = Frame(root)
miframe.config(bg="Indigo")


miframe.pack()

operacion = ""
reset_Pantalla = False
resultado = 0
# ------------pantalla---------------
numPantalla = StringVar()

pantalla = Entry(miframe, textvariable=numPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(bg="#7B68EE", fg="#FFEFD5", justify="right", width=28)


# ----funciones para pulsar los numero
def numPulsado(num):
    global operacion
    global reset_Pantalla
    if reset_Pantalla != False:
        numPantalla.set(num)
        reset_Pantalla = False
    else:
        numPantalla.set(numPantalla.get() + num)

# -------funciones----------------------


def suma(num):
    global operacion
    global resultado
    global reset_Pantalla
    resultado += int(num)
    operacion = "suma"
    reset_Pantalla = True
    numPantalla.set(resultado)


# def pulsarIgual():
#     global resultado
#     numPantalla.set(resultado+int(numPantalla.get()))
#     resultado = 0


num1 = 0

contador_resta = 0


def resta(num):
    global operacion
    global resultado
    global num1
    global contador_resta
    global reset_pantalla

    if contador_resta == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contador_resta == 1:
            resultado = num1-int(num)
        else:
            resultado = int(resultado)-int(num)
        numPantalla.set(resultado)
        resultado = numPantalla.get()
    contador_resta = contador_resta+1
    operacion = "resta"
    reset_pantalla = True


contador_divi = 0


def divide(num):
    global operacion
    global resultado
    global num1
    global contador_divi
    global reset_pantalla
    if contador_divi == 0:
        num1 = float(num)
        resultado = num1
    else:
        if contador_divi == 1:
            resultado = num1/float(num)
        else:
            resultado = float(resultado)/float(num)
        numPantalla.set(resultado)
        resultado = numPantalla.get()
    contador_divi = contador_divi+1
    operacion = "division"
    reset_pantalla = True


contador_multi = 0


def multiplica(num):
    global operacion
    global resultado
    global num1
    global contador_multi
    global reset_pantalla
    if contador_multi == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contador_multi == 1:
            resultado = num1*int(num)
        else:
            resultado = int(resultado)*int(num)
        numPantalla.set(resultado)
        resultado = numPantalla.get()
    contador_multi = contador_multi+1
    operacion = "multiplicacion"
    reset_pantalla = True


def pulsar_igual():
    global resultado
    global operacion
    global contador_resta
    global contador_multi
    global contador_divi
    if operacion == "suma":
        numPantalla.set(resultado+int(numPantalla.get()))
        resultado = 0
    elif operacion == "resta":
        numPantalla.set(int(resultado)-int(numPantalla.get()))
        resultado = 0
        contador_resta = 0
    elif operacion == "multiplicacion":
        numPantalla.set(int(resultado)*int(numPantalla.get()))
        resultado = 0
        contador_multi = 0
    elif operacion == "division":
        numPantalla.set(int(resultado)/int(numPantalla.get()))
        resultado = 0
        contador_divi = 0


# ----------fila 1 7-8-9-/----------
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
                  bg="#7B68EE", command=lambda: divide(numPantalla.get()))
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
                   bg="#7B68EE", command=lambda: divide(numPantalla()))
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
                    padx=10, bg="#7B68EE", command=lambda: resta(numPantalla.get()))
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
                    padx=10, bg="#7B68EE", command=lambda: pulsar_igual())
botonigual.grid(row=5, column=3)


root.mainloop()
