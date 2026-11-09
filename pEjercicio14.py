#Menú que se repite

opcion = ""

while opcion != "salir":
    opcion = input("Escribe 'hola' o 'salir': ")
    if opcion == "hola":
        print("¡Hola, ten un buen día!")
    elif opcion == "salir":
        print("Hasta luego")
    else:
        print("Oh, opción no válida, intente nuevamente.")        