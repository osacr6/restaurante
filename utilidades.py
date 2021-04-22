import os
import time
import platform
from def_restaurantes import *

def limpiar(segundos = 0):
    #SE UTILIZA platform PARA VALIDAR EL S.O DEL USUARIO
    sistema = platform.system()
    #print("Estamos en {}".format(sistema))
    time.sleep(segundos)
    if sistema == "Windows":
        os.system('cls')
    elif sistema == "Darwin":
        os.system('clear')

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
    if esAdmin:
        print('6) Configuracion')
    print()
    return str(input( "Ingrese una opcion: " ))

def primeraPregunta(esAdmin, nombre):

    # limpiar consola windows
    limpiar()
    # preguntar
    intro = introduccion(esAdmin, nombre)
    # opcion no es un numero
    if not intro.isnumeric():
        if intro == '':
            return primeraPregunta(esAdmin, nombre)
        else:
            #opciones = buscarCategoria(intro)
            #print(opciones)
            return print('Buscando ....', intro)
    else:
        intro = int(intro)

#VALIDACIÓN DE OPCIONES
    if intro == 1:
        print("Promociones")
#        buscar = buscarProducto(intro)
#        print(buscar)
    elif intro == 2:
        print("Desayunos")
#        buscar = buscarProducto(intro)
#        print(buscar)
    elif intro == 3:
        print("Almuerzos")
#        buscar = buscarProducto(intro)
#        print(buscar)
    elif intro == 4:
        print("Cena")
#        buscar = buscarProducto(intro)
#        print(buscar)
    elif intro == 5:
        print("Antojitos")
#        buscar = buscarProducto(intro)
#        print(buscar)
    elif intro == 6:
        if esAdmin:
            print("Configuracion para el Administrador")
            return 'admin'
#        admin = menuAdmin(intro)
#        print(admin)
        else:
            return primeraPregunta(esAdmin, nombre)
    else:
        return primeraPregunta(esAdmin, nombre)



#*********Codigo Anterior*********
    # opcion invalida
#    if intro == 0 or intro > 6:
#        return primeraPregunta(esAdmin, nombre)


#if intro == 1:
#    return 'Promociones'
#if intro == 2:
#    return 'Desayunos'
#if intro == 3:
#    return 'Almuersos'
#if intro == 4:
#    return 'Cena'
#if intro == 5:
#    return 'Antojitos'''

  # es admin
#    if intro == 6:
#        if esAdmin:
#            print( '*Confiracion para el Administrador*' )
#            return 'admin'
#        else:
#            return primeraPregunta(esAdmin, nombre)
#*********Codigo Anterior*********
