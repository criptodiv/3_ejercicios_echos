from funciones import *

datos_de_personas = [["Nombre","Apellido","Edad"]]

while True:
    limpiar_pantalla()
    resp = input("desea agregar a una persona? si o no? :").upper
    if resp == "Si":
        limpiar_pantalla()
        nombre = input("ingresar nombre: ")
        limpiar_pantalla()
        apellido = input("ingresar apellido: ")
        limpiar_pantalla()
        edad = int(input("ingresar su edad: "))

        persona = []
        persona.append(nombre)
        persona.append(apellido)
        persona.append(edad)

        datos_de_personas.append(persona)
    else:
        break

    

almacenar_datos_3(datos_de_personas)