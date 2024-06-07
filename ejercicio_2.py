from funciones import almacenar_datos,limpiar_pantalla

datos_de_personas = [["Nombre","Apellido"]]

for x in range (3):
    limpiar_pantalla()
    nombre = input("ingresar nombre: ")
    limpiar_pantalla()
    apellido = input("ingresar apellido: ")

    persona = []
    persona.append(nombre)
    persona.append(apellido)

    datos_de_personas.append(persona)

almacenar_datos(datos_de_personas)