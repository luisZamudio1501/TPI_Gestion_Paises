"""
main.py — archivo principal del TPI

"""
#print("Hola Trabajo Integrador")

"""
# prueba consola
paises = [
    {"nombre": "Argentina", "poblacion": 1111111, "superficie": 2222222, "continente": "América"},
    {"nombre": "Brasil", "poblacion": 3333333, "superficie": 4444444, "continente": "América"},
    {"nombre": "Japón", "poblacion": 5555555, "superficie": 666666, "continente": "Asia"}
]

print("\nLista completa de países:")
for pais in paises:
    print(pais) 

print("\nSolo los nombres:")
for pais in paises:
    print(pais["nombre"])

print("\nNombre y población:")
for pais in paises:
    print(pais["nombre"], "->", pais["poblacion"], "habitantes")
    
"""

# ----------------- IMPORTACIONES -----------------

import os

from persistencia import leer_csv, guardar_csv

from consultas import (
    buscar_por_nombre,
    filtrar_por_continente,
    filtrar_por_rango_poblacion,
    filtrar_por_rango_superficie,
    ordenar_paises
)

from estadisticas import (
    pais_mayor_poblacion,
    pais_menor_poblacion,
    promedio_poblacion,
    promedio_superficie,
    cantidad_por_continente
)

from validaciones import (
    leer_entero_no_negativo,
    leer_entero_positivo,
    leer_texto_no_vacio,
    leer_opcion_menu
)

RUTA_CSV = "datos.csv"


# ----------------- FUNCIONES DE CONSOLA -----------------

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPRESIONE ENTER PARA CONTINUAR...")


# ----------------- FUNCIONES DEL MENÚ -----------------

def mostrar_menu():
    print("\n     === MENÚ PRINCIPAL ===")
    print("         Gestión de Países ")
    print("1)   Agregar país")
    print("2)   Actualizar país (población/superficie)")
    print("3)   Buscar país por nombre")
    print("4)   Filtrar países")
    print("5)   Ordenar países")
    print("6)   Estadísticas")
    print("7)   Salir")

# OPCIÓN 1
def opcion_agregar_paises(paises):
    
    limpiar_pantalla()
    print("\n— Agregar país —")
    nombre = " ".join(leer_texto_no_vacio("Nombre: ").strip().split()).title()
    continente = " ".join(leer_texto_no_vacio("Continente: ").strip().split()).capitalize()
    poblacion = leer_entero_positivo("Población (> 0): ")
    superficie = leer_entero_positivo("Superficie km² (> 0): ")

    # Este bloque evita duplicados (búsqueda exacta)
    if buscar_por_nombre(paises, nombre, "exacta"):
        print("ERROR: Ya existe un país con ese nombre")
        pausar()
        return

    paises.append({
        "nombre": nombre.strip(),
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente.strip()
    })

    guardar_csv(RUTA_CSV, paises)
    print("✔ País agregado y guardado en CSV")
    pausar()

# OPCIÓN 2
def opcion_actualizar_paises(paises):
    
    limpiar_pantalla()
    print("\n— Actualizar país —")
    nombre = leer_texto_no_vacio("Nombre a actualizar (coincidencia exacta): ")
    encontrados = buscar_por_nombre(paises, nombre, "exacta")

    if not encontrados:
        print("No se encontró país con ese nombre")
        pausar()
        return

    p = encontrados[0]
    print(f"Actual -> pob:{p['poblacion']} | sup:{p['superficie']}")
    p["poblacion"] = leer_entero_positivo("Nueva población: ")
    p["superficie"] = leer_entero_positivo("Nueva superficie: ")

    guardar_csv(RUTA_CSV, paises)
    print("✔ País actualizado y guardado en CSV")
    pausar()

# OPCIÓN 3
def opcion_buscar_paises(paises):
    
    limpiar_pantalla()
    print("\n— Buscar por nombre —")
    termino = leer_texto_no_vacio("Ingrese nombre o parte: ")
    resultados = buscar_por_nombre(paises, termino, "parcial")

    if not resultados:
        print("Sin resultados.")
    else:
        for r in resultados:
            print(f"- {r['nombre']} | pob:{r['poblacion']} | sup:{r['superficie']} | {r['continente']}")
    pausar()









# --------- FLUJO PRINCIPAL  ---------

paises = leer_csv(RUTA_CSV)
opcion = ""

while opcion not in ("7", "exit", "Exit", "EXIT", "salir", "SALIR"):
    
    limpiar_pantalla()
    mostrar_menu()
    opcion = input("Ingrese una opción: ").strip()

    if opcion.lower() in ("exit", "salir"):
        opcion = "7"

    match opcion:
        case "1":
            opcion_agregar_paises(paises)
        case "2":
            opcion_actualizar_paises(paises)
        case "3":
            opcion_buscar_paises(paises)
        case "4":
            opcion_filtrar_paises(paises)
        case "5":
            opcion_ordenar_paises(paises)
        case "6":
            opcion_estadisticas_paises(paises)
        case "7":
            limpiar_pantalla()
            print("FIN DE PROGRAMA\n")
            pausar()
        case _:
            print("Opción inválida. Ingrese un número del 1 al 7.")
            pausar()

