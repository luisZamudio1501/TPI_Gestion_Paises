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
    cont = continente.strip().low