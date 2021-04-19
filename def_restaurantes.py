import os
from archivos import lector, escritor

def agregaRestautantes(menus):
  print('agregarMenu ...')
  return menus;

def editaRestautantes(menus):
  print('editarMenu ...')
  return menus;

def eliminaRestautantes(menus):
  print('EliminarMenu ...')
  return menus;

def optenerMenus(restautantes, folderMenus):
  menus = []
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
  return menus