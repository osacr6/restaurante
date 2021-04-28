import os
import sys
import time
from archivos import lector, escritor
from utilidades import *
from menus import *

# constantes
restautantes = []
menus = []
caritoDecompras = []
esAdmin = False
nombreUsuario = 'Consumidor';
dirname = os.path.dirname(__file__)
archivoRestaurantes = os.path.join(dirname, 'datos/restaurantes')
folderMenus = os.path.join(dirname, 'datos/menus')

# mode admin
for arg in sys.argv:
  if str(arg) == 'admin':
    print('Iniciando modo Administrador ...')
    print()
    esAdmin = True

# leer archivo restaurantes
restaurantes = lector(archivoRestaurantes)
#menus = obtenerMenus(restaurantes, folderMenus)

# hacer copia de archivo restaurantes
#escritor(archivoRestaurantes+'2', restautantes)

# limpiar consola windows
#limpiar(1)

# optener datos de restaurantes
print('Datos del archivo' , archivoRestaurantes)
menus = obtenerMenus(restaurantes, folderMenus)

# limpiar consola windows
limpiar(0)

# iniciar programa
if esAdmin:
  nombreUsuario = 'admin'
else:
  nombreUsuario = obtenerNombre()


def primeraPregunta(esAdmin, nombre):
    # limpiar consola windows
    limpiar()
    listarCarrito(caritoDecompras)
    # preguntar
    intro = introduccion(esAdmin, nombre)
    numero = uptenerSeleccion(intro)

    #VALIDACIÓN DE OPCIONES
    if numero == 1:
        print("Promociones")
        menuPromos(intro, esAdmin, nombre)
        #buscar = buscarProducto(intro)
        #print(buscar)
    elif numero == 2:
        print("Desayunos")
        #buscar = buscarProducto(intro)
        #print(buscar)
    elif numero == 3:
        print("Almuerzos")
        #buscar = buscarProducto(intro)
        #print(buscar)
    elif numero == 4:
        print("Cena")
        #buscar = buscarProducto(intro)
        #print(buscar)
    elif numero == 5:
        print("Antojitos")
        #buscar = buscarProducto(intro)
        #print(buscar)
    elif numero == 6:
        if esAdmin:
            print("Configuracion para el Administrador")
            return 'admin'
        #admin = menuAdmin(intro)
        #print(admin)
        else:
            return primeraPregunta(esAdmin, nombre)
    else:
        return primeraPregunta(esAdmin, nombre)

def menuPromos(intro, esAdmin, nombre):
    global caritoDecompras
    limpiar()
    promos = listarPromos(menus)
    print("***", nombre, "estas son nuestras promos actuales ***")
    for i in range(len(promos)):
      if i < 10:
        print('{0}) {1} de {2} a tan solo ₡{3}'.format(i+1, promos[i][1], promos[i][0], promos[i][4]))
    print("0) volver al menú principal")
    print()
    pregunta = str(input("Digite su opcion: "))
    numero = uptenerSeleccion(pregunta)
    print(numero)

    if numero == 0:
        return primeraPregunta(esAdmin, nombre)

    if numero > 0 and numero <= 10:
        caritoDecompras = generarPedido(promos[numero-1], caritoDecompras)
        return primeraPregunta(esAdmin, nombre)
    else:
        return menuPromos(intro, esAdmin, nombre)

# ejecutar primera pregunta
opcion_1 = primeraPregunta(esAdmin, nombreUsuario)
print(opcion_1)
# buscar opcion 1