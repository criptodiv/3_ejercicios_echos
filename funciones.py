import os
import csv

def limpiar_pantalla ():
    os.system("clear")

def nombre_mas_largo(p_lista):
    for x in range(3):
        if x == 0:
            nombre_mas_largo = p_lista[0]
        else:
            if len(p_lista[x]) > len(nombre_mas_largo):
                nombre_mas_largo = p_lista[x]
    print("EL nombre más largo es: ",nombre_mas_largo)

def almacenar_datos (p_personas):
    with open("nombre_apellido.csv","w",newline="") as arc:
        escritor = csv.writer(arc)
        escritor.writerows(p_personas)

def almacenar_datos_3 (p_personas):
    with open("nombre_apellido_edad.csv","w",newline="") as arc:
        escritor = csv.writer(arc)
        escritor.writerows(p_personas)