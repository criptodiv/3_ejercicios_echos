from funciones import *

nombres = []

with open("nombres.csv","w",newline="") as ar:
    escritor = csv.writer(ar)
    for x in range(3):
        limpiar_pantalla()
        nombre = input("ingrese nombre: ")
        nombres.append(nombre)
    escritor.writerow(nombres)

nombre = nombre_mas_largo(nombres)