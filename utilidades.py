import os
import sys
import time
import platform
from archivos import lector, escritor
from restaurantes import *
from menus import *

total = float(0)

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
            return 'Buscar'
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
    print('6) Pagar orden')
    print('7) Salir del sistema')
    if esAdmin:
        print('8) Configuracion')
    print()
    return str(input( "Ingrese una opcion: " ))

def generarPedido(orden, lista):
    lista.append(orden)
    print("Pedido Agregado a la Orden:")
    for x in lista:
        print('{0} de {1} ...... ₡{2}'.format(x[1], x[0], x[4]))
    return lista

def listarCarrito(lista=[]):
    global total
    if len(lista) == 0:
        return
    else:
        print("***** Orden de Compra Actual *****")
        for x in lista:
            print('{0} de {1} ...... ₡{2}'.format(x[1], x[0], x[4]))
            #precio = float(x[4])
            #total = total+precio
        print("Total Acumulado: ", total)
        print()
