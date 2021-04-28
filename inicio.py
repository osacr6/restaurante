import os
import sys
import time
from datetime import datetime
from archivos import lector, escritor
from utilidades import *
from menus import *

# constantes
restaurantes = []
menus = []
caritoDecompras = []
esAdmin = False
nombreUsuario = 'Consumidor';
dirname = os.path.dirname(__file__)
archivoRestaurantes = os.path.join(dirname, 'datos/restaurantes')
folderMenus = os.path.join(dirname, 'datos/menus')
folderOrdenes = os.path.join(dirname, 'datos/ordenes')

# mode admin
for arg in sys.argv:
  if str(arg) == 'admin':
    esAdmin = True

# leer archivo restaurantes
restaurantes = lector(archivoRestaurantes)

# optener datos de restaurantes
menus = obtenerMenus(restaurantes, folderMenus)

# iniciar programa
limpiar()
if esAdmin:
  nombreUsuario = 'admin'
else:
  nombreUsuario = obtenerNombre()


def primeraPregunta(esAdmin, nombre):
    global restaurantes
    global caritoDecompras
    # limpiar consola windows
    limpiar()
    listarCarrito(caritoDecompras)
    # preguntar
    intro = introduccion(esAdmin, nombre)
    numero = uptenerSeleccion(intro)

    #VALIDACIÓN DE OPCIONES
    if numero == 1:
        menuPromos(intro, esAdmin, nombre)
    elif numero == 2:
        menuDesayunos(intro, esAdmin, nombre)
    elif numero == 3:
        menuAlmuerzos(intro, esAdmin, nombre)
    elif numero == 4:
        menuCenas(intro, esAdmin, nombre)
    elif numero == 5:
        menuAntojitos(intro, esAdmin, nombre)
    elif numero == 6:
        limpiar()
        print("****", nombre, "Gracias por utilizar nuestra APP ****")
        listarCarrito(caritoDecompras)
        now = datetime.now()
        timestamp = str(datetime.timestamp(now))
        escritor(folderOrdenes+"/orden-"+timestamp, caritoDecompras)
        print('Orden #{0} Ingresada ....'.format(timestamp))
        like()
        caritoDecompras = []
        input("")
        return primeraPregunta(esAdmin, nombre)
    elif numero == 7:
        if len(caritoDecompras) == 0:
            print("****", nombre, "Gracias por utilizar nuestra APP ****")
            return 0
        else:
            print("Antes de salir debe pagar la orden realizada")
            limpiar(3)
            return primeraPregunta(esAdmin, nombre)
    elif numero == 8:
        if esAdmin:
            limpiar()
            r = listarRestaurantes(restaurantes)
            if r and numero > 0:
                limpiar()
                restaurantes = opcionesAdmin(restaurantes, r)
                escritor(archivoRestaurantes, restaurantes)
                return primeraPregunta(esAdmin, nombre)
        else:
            return primeraPregunta(esAdmin, nombre)
    else:
        return primeraPregunta(esAdmin, nombre)


def menuPromos(intro, esAdmin, nombre):
    global caritoDecompras
    limpiar()
    palabra = "descuento"
    productos = listarProductos(menus, palabra)
    print("***", nombre, "estas son nuestras Promos actuales ***")
    for i in range(len(productos)):
      if i < 10:
        print('{0}) {1} de {2} a tan solo ₡{3}'.format(i+1, productos[i][1], productos[i][0], productos[i][4]))
    print("----")
    print("0) Volver al menú principal")
    print()
    pregunta = str(input("Digite su opción: "))
    numero = uptenerSeleccion(pregunta)
    print(numero)
    if numero == 0:
        return primeraPregunta(esAdmin, nombre)
    if numero > 0 and numero <= 10 and len(productos) > numero-1:
        caritoDecompras = generarPedido(productos[numero-1], caritoDecompras)
        return primeraPregunta(esAdmin, nombre)
    else:
        return menuPromos(intro, esAdmin, nombre)


def menuDesayunos(intro, esAdmin, nombre):
    global caritoDecompras
    limpiar()
    palabra = "desayuno"
    productos = listarProductos(menus, palabra)
    print("***", nombre, "estos son nuestros Desayunos actuales ***")
    for i in range(len(productos)):
      if i < 10:
        print('{0}) {1} de {2} a tan solo ₡{3}'.format(i+1, productos[i][1], productos[i][0], productos[i][4]))
    print("----")
    print("0) Volver al menú principal")
    print()
    pregunta = str(input("Digite su opción: "))
    numero = uptenerSeleccion(pregunta)
    print(numero)
    if numero == 0:
        return primeraPregunta(esAdmin, nombre)
    if numero > 0 and numero <= 10 and len(productos) > numero-1:
        caritoDecompras = generarPedido(productos[numero-1], caritoDecompras)
        return primeraPregunta(esAdmin, nombre)
    else:
        return menuPromos(intro, esAdmin, nombre)


def menuAlmuerzos(intro, esAdmin, nombre):
    global caritoDecompras
    limpiar()
    palabra = "almuerzo"
    productos = listarProductos(menus, palabra)
    print("***", nombre, "estos son nuestros Almuerzos actuales ***")
    for i in range(len(productos)):
      if i < 10:
        print('{0}) {1} de {2} a tan solo ₡{3}'.format(i+1, productos[i][1], productos[i][0], productos[i][4]))
    print("----")
    print("0) Volver al menú principal")
    print()
    pregunta = str(input("Digite su opción: "))
    numero = uptenerSeleccion(pregunta)
    print(numero)
    if numero == 0:
        return primeraPregunta(esAdmin, nombre)
    if numero > 0 and numero <= 10 and len(productos) > numero-1:
        caritoDecompras = generarPedido(productos[numero-1], caritoDecompras)
        return primeraPregunta(esAdmin, nombre)
    else:
        return menuPromos(intro, esAdmin, nombre)


def menuCenas(intro, esAdmin, nombre):
    global caritoDecompras
    limpiar()
    palabra = "cena"
    productos = listarProductos(menus, palabra)
    print("***", nombre, "estas son nuestras Cenas actuales ***")
    for i in range(len(productos)):
      if i < 10:
        print('{0}) {1} de {2} a tan solo ₡{3}'.format(i+1, productos[i][1], productos[i][0], productos[i][4]))
    print("----")
    print("0) Volver al menú principal")
    print()
    pregunta = str(input("Digite su opción: "))
    numero = uptenerSeleccion(pregunta)
    print(numero)
    if numero == 0:
        return primeraPregunta(esAdmin, nombre)
    if numero > 0 and numero <= 10 and len(productos) > numero-1:
        caritoDecompras = generarPedido(productos[numero-1], caritoDecompras)
        return primeraPregunta(esAdmin, nombre)
    else:
        return menuPromos(intro, esAdmin, nombre)


def menuAntojitos(intro, esAdmin, nombre):
    global caritoDecompras
    limpiar()
    palabra = "antojo"
    productos = listarProductos(menus, palabra)
    print("***", nombre, "estos son nuestros Antojitos actuales ***")
    for i in range(len(productos)):
      if i < 10:
        print('{0}) {1} de {2} a tan solo ₡{3}'.format(i+1, productos[i][1], productos[i][0], productos[i][4]))
    print("----")
    print("0) Volver al menú principal")
    print()
    pregunta = str(input("Digite su opción: "))
    numero = uptenerSeleccion(pregunta)
    print(numero)
    if numero == 0:
        return primeraPregunta(esAdmin, nombre)
    if numero > 0 and numero <= 10 and len(productos) > numero-1:
        caritoDecompras = generarPedido(productos[numero-1], caritoDecompras)
        return primeraPregunta(esAdmin, nombre)
    else:
        return menuPromos(intro, esAdmin, nombre)


# ejecutar primera pregunta
opcion_1 = primeraPregunta(esAdmin, nombreUsuario)
print(opcion_1)
