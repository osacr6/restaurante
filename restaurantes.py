import os
from archivos import lector, escritor

def obtenerMenus(restaurantes, folderMenus):
  menus = []
  for i in range(len(restaurantes)):
    fila = restaurantes[i]
    if i != 0 and isinstance(fila, list) and len(fila) == 5 and len(fila[4]) > 0:
      # leer archivo comidas de cada restaurante
      archivoMenu = os.path.join(folderMenus, fila[4])
      menu = lector(archivoMenu)
      for j in range(len(menu)):
        if(j != 0):
          receta = menu[j]
          menus.append(receta)
  return menus
