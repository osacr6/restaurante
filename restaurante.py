import os
import sys
import time
from archivos import lector, escritor
from utilidades import *
from def_restaurantes import *
from def_menus import *

# constantes
restautantes = []
menus = []
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
restautantes = lector(archivoRestaurantes)

# hacer copia de archivo restaurantes
#escritor(archivoRestaurantes+'2', restautantes)

# limpiar consola windows
#limpiar(1)

# optener datos de restaurantes
print('Datos del archivo' , archivoRestaurantes)
menus = optenerMenus(restautantes, folderMenus)

# limpiar consola windows
limpiar(0)

# iniciar programa
if esAdmin:
  nombreUsuario = 'admin'
else:
  nombreUsuario = optenerNombre()

# ejecutar primera pregunta
opcion_1 = primeraPregunta(esAdmin, nombreUsuario)
print(opcion_1)
# buscar opcion 1
