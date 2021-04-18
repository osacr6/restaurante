import csv

# https://docs.python.org/3/library/csv.html
def lector(nombreArchivo):
  datos = []
  with open(nombreArchivo + '.csv') as csvArchivo:
    csvLector = csv.reader(csvArchivo, delimiter=',')
    for fila in csvLector:
      datos.append(fila)
    return datos

def escritor(nombreArchivo, datos):
  with open(nombreArchivo + '.csv', mode='w', newline='') as nuevoArchivo:
    csvEscritor = csv.writer(nuevoArchivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csvEscritor.writerows(datos)