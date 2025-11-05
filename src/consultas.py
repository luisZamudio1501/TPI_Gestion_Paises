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

# Devuelve países con población entre mínimo y máximo ingresado
def filtrar_por_rango_poblacion(paises, minimo=0, maximo=None):
    resultados = []
    for p in paises:
        poblacion = p["poblacion"]
        if maximo is None and poblacion >= minimo:
            resultados.append(p)
        elif maximo is not None and minimo <= poblacion <= maximo:
            resultados.append(p)
    return resultados

# Devuelve países con superficie entre mínimo y máximo ingresado
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

# Esta función ordena la lista de países por un campo específico (nombre, poblacion o superficie)
# 
def ordenar_paises(paises, por="nombre", descendente=False):
    
    if por not in ("nombre", "poblacion", "superficie"):
        print("ERROR: campo de ordenamiento inválido")
        return paises

    lista_ordenada = sorted(paises, key=lambda p: p[por], reverse=descendente)
    return lista_ordenada