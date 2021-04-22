import os
import time

def limpiar(segundos = 0):
  time.sleep(segundos)
  os.system('cls')
  os.system('clear')

def optenerNombre():
  print('***** Bienvenido a nuestro Sistema Restaurantes *****')
  print()
  return str(input( "Ingrese su nombre: " ))

def introduccion(esAdmin, nombre):
  print('*****', nombre, 'Bienvenido al Sistema Restaurante *****')
  print()
  print('1) Promociones')
  print('2) Desayunos')
  print('3) Almuersos')
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
      return print('Buscando ....', intro)
  else:
      intro = int(intro)
  # opcion invalida
  if intro == 0 or intro > 6:
    return primeraPregunta(esAdmin, nombre)

  if intro == 1:
    return 'Promociones'
  if intro == 2:
    return 'Desayunos'
  if intro == 3:
    return 'Almuersos'
  if intro == 4:
    return 'Cena'
  if intro == 5:
    return 'Antojitos'

  # es admin
  if intro == 6:
    if esAdmin:
      print( '*Confiracion para el Administrador*' )
      return 'admin'
    else:
      return primeraPregunta(esAdmin, nombre)
