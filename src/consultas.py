# Búsquedas, filtros y ordenamientos de países

# BÚSQUEDA

# Esta función busca países por nombre dentro de una lista de países
# y devuelve una lista con los encontrados
def buscar_por_nombre(paises, texto_a_buscar, tipo_busqueda):
    
    resultados = []

    if texto_a_buscar.strip() == "":
        return resultados

    texto = texto_a_buscar.lower().strip()

    for pais in paises:
        nombre = pais["nombre"].lower()

        if tipo_busqueda == "parcial" and texto in nombre:
            resultados.append(pais)
        elif tipo_busqueda == "exacta" and texto == nombre:
            resultados.append(pais)

    return resultados


# FILTROS

# Esta función devuelve una lista con los países del continente indicado
def filtrar_por_continente(paises, continente):
    resultados = []
    cont = continente.strip().lower()
    for p in paises:
        if p["continente"].lower() == cont:
            resultados.append(p)
    return resultados

# Esta función devuelve países con población entre mínimo y máximo ingresado
def filtrar_por_rango_poblacion(paises, minimo=0, maximo=None):
    resultados = []
    for p in paises:
        poblacion = p["poblacion"]
        if maximo is None and poblacion >= minimo:
            resultados.append(p)
        elif maximo is not None and minimo <= poblacion <= maximo:
            resultados.append(p)
    return resultados

# Esta función devuelve países con superficie entre mínimo y máximo ingresado
def filtrar_por_rango_superficie(paises, minimo=0, maximo=None):
    resultados = []
    for p in paises:
        superficie = p["superficie"]
        if maximo is None and superficie >= minimo:
            resultados.append(p)
        elif maximo is not None and minimo <= superficie <= maximo:
            resultados.append(p)
    return resultados

# ORDENAMIENTO

def ordenar_paises(paises, campo_orden="nombre", descendente=False):
    # Bloque validar campo
    if campo_orden not in ("nombre", "poblacion", "superficie"):
        print("ERROR: campo de ordenamiento inválido")
        return paises

    # Se Crea una lista nueva con los países ordenados según el campo elegido
    lista_ordenada = []
    for p in paises:
        lista_ordenada.append(p)

    # Ordenamiento manual burbuja
    n = len(lista_ordenada)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            a = lista_ordenada[j][campo_orden]
            b = lista_ordenada[j + 1][campo_orden]
            if (not descendente and a > b) or (descendente and a < b):
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]

    return lista_ordenada

