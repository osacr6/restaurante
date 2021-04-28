from restaurantes import *

def agregaReceta(restautante, menus):
  print('agregaReceta ...')
  return menus;

def editaReceta(restautante, menus):
  print('editaReceta ...')
  return menus;

def eliminaReceta(restautante, menus):
  print('EliminaReceta ...')
  return menus;

def listarPromos(menus):
    lista = []
    for receta in menus:
        for col  in receta:
            if col == 'descuento':
                lista.append(receta)
    return lista
