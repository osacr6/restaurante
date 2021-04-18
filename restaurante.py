import os
import time
from archivos import lector, escritor
from utilidades import introduccion

# constantes
dirname = os.path.dirname(__file__)
archivoRestaurantes = os.path.join(dirname, 'datos\\restaurantes')
folderMenus = os.path.join(dirname, 'datos\\menus')
menus = []

# leer archivo restaurantes
restautantes = lector(archivoRestaurantes)

# hacer copia de archivo restaurantes
# escritor(archivoRestaurantes+'2', restautantes)

# limpiar consola windows
os.system('cls')

# imprimir datos de restaurantes
print('Datos del archivo' , archivoRestaurantes)
print()
for i in range(len(restautantes)):
  fila = restautantes[i]
  print(i, fila)
  if i != 0 and isinstance(fila, list) and len(fila) == 5 and len(fila[4]) > 0:
    # leer archivo comidas de cada restaurante
    archivoMenu = os.path.join(folderMenus, fila[4])
    menu = lector(archivoMenu)
    for j in range(len(menu)):
      if(j != 0):
        receta = menu[j]
        print(receta)
        menus.append(receta)

time.sleep(1)
os.system('cls')

# iniciar programa
def primeraPregunta():
  os.system('cls')
  intro = introduccion()
  # opcion no es un numero
  if not intro.isnumeric():
    print( 'Buscando ....', intro)
  else:
    intro = int(intro)

  if intro == 1:
    print( 'Promociones' )
  if intro == 2:
    print( 'Desayunos' )
  if intro == 3:
    print( 'Almuersos' )
  if intro == 4:
    print( 'Cena' )
  if intro == 5:
    print( 'Antojitos' )
  # opcion invalida
  if intro == 0 or intro > 5:
    primeraPregunta()

# ejecutar primera pregunta
primeraPregunta()





