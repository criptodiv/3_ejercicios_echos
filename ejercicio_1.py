import os
import csv
def limpiar_pantalla():
    os.system("clear")

def nombre_mas_largo(p_lista):
    for x in range(3):
        if x == 0:
            nombre_mas_largo = p_lista[0]
        else:
            if len(p_lista[x]) > len(nombre_mas_largo):
                nombre_mas_largo = p_lista[x]
    print("EL nombre más largo es: ",nombre_mas_largo)

nombres = []

with open("nombres.csv","w",newline="") as ar:
    escritor = csv.writer(ar)
    for x in range(3):
        limpiar_pantalla()
        nombre = input("ingrese nombre: ")
        nombres.append(nombre)
    escritor.writerow(nombres)

nombre = nombre_mas_largo(nombres)