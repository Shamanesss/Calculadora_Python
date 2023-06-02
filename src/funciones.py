operacion = ""
reset_Pantalla = False
resultado = 0


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
