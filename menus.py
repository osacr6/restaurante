from restaurantes import *

def listarProductos(menus, palabra):
    lista = []
    for receta in menus:
        for col  in receta:
            if col == palabra:
            #if col == 'descuento':
                lista.append(receta)
    return lista
