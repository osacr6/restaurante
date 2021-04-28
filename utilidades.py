import os
import sys
import time
import platform
from archivos import lector, escritor
from restaurantes import *
from menus import *


def limpiar(segundos = 0):
    #SE UTILIZA platform PARA VALIDAR EL S.O DEL USUARIO
    sistema = platform.system()
    #print("Estamos en {}".format(sistema))
    time.sleep(segundos)
    if sistema == "Windows":
        os.system('cls')
    elif sistema == "Darwin":
        os.system('clear')


def uptenerSeleccion(entrada):
    # opcion no es un numero
    if not entrada.isnumeric():
        if entrada == '':
            return 0
        else:
            return 0
    else:
        return int(entrada)


def obtenerNombre():
    print('***** Bienvenido a nuestro Sistema Restaurantes *****')
    print()
    return str(input( "Ingrese su nombre: " ))


def introduccion(esAdmin, nombre):
    print('*****', nombre, 'Bienvenido al Sistema Restaurante *****')
    print()
    print('1) Promociones')
    print('2) Desayunos')
    print('3) Almuerzos')
    print('4) Cena')
    print('5) Antojitos')
    print('6) Finalizar orden')
    print('7) Salir del sistema')
    if esAdmin:
        print('8) Configuracion')
    print()
    return str(input( "Ingrese una opcion: " ))


def listarRestaurantes(restautantes):
    print('***** Administracion de Restaurante *****')
    for i in range(len(restautantes)):
        if i > 0:
            print('{0}) {1}'.format(i, restautantes[i][0]))
    print()
    return uptenerSeleccion(str(input( "Ingrese el Restaurante a modificar: " )))


def opcionesAdmin(restautantes, index):
    print('***** Administracion de Restaurante *****')
    print('{0}'.format(restautantes[index][0]))
    print("----")
    for col in range(len(restautantes[0])):
        print('{0}) Editar {1}'.format(col+1, restautantes[0][col]))
    print('{0}) Eliminar {1}'.format(len(restautantes[0])+1, restautantes[index][0]))
    print()
    opcion = uptenerSeleccion(str(input( "Ingrese una opcion: " )))
    if opcion == len(restautantes[0])+1:
        del restautantes[index]
        return restautantes
    else:
        print('{0}: {1}'.format(restautantes[0][opcion-1], restautantes[index][opcion-1]))
        nuevoDato = str(input( "Ingrese Nuevo dato: " ))
        restautantes[index][opcion-1] = nuevoDato
        print('{0} {1}: {2}'.format(restautantes[index][0], restautantes[0][opcion-1], restautantes[index][opcion-1]))
        return restautantes


def generarPedido(orden, lista):
    lista.append([orden[0], orden[1], orden[4]])
    return lista


def listarCarrito(lista=[]):
    total = float(0)
    if len(lista) == 0:
        return
    else:
        print("***** Orden de Compra Actual *****")
        for x in lista:
            print('{0} de {1} ...... ₡{2}'.format(x[1], x[0], x[2]))
            precio = float(x[2])
            total = total+precio
        print('Total Acumulado: ₡{0}'.format(total))
        print()


def like():
    print("..... (¯`v´¯)♥")
    print(".......•.¸.•´")
    print("....¸.•´")
    print("... (")
    print("☻/")
    print("/▌♥♥")
    print("/ \ ♥♥")