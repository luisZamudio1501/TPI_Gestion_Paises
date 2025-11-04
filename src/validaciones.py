def leer_texto_no_vacio(mensaje):
    dato = ""
    while dato == "":
        dato = input(mensaje).strip()
        if dato == "":
            print("ERROR: el campo no puede estar vacío")
    return dato


def leer_entero_no_negativo(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato.isdigit():
            return int(dato)
        print("ERROR: ingrese un número entero mayor o igual a 0")


def leer_entero_positivo(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato.isdigit() and int(dato) > 0:
            return int(dato)
        print("ERROR: ingrese un número entero mayor que 0")


def leer_opcion_menu(mensaje, opciones_validas):
    dato = input(mensaje).strip()
    if dato in opciones_validas:
        return dato
    else:
        print("Opción inválida. Intente nuevamente.")
        return ""