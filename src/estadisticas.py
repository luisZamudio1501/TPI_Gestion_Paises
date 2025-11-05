# ESTADÍSTICAS

# Cada país es un diccionario con claves:
# nombre (str)
# poblacion (int)
# superficie (int)
# continente (str)

# Esta función devuelve el país con mayor población 
def pais_mayor_poblacion(paises):

    if not paises:
        return {}
    mayor = paises[0]
    i = 1
    while i < len(paises):
        if paises[i]["poblacion"] > mayor["poblacion"]:
            mayor = paises[i]
        i += 1
    return mayor


# Devuelve el país con menor población
def pais_menor_poblacion(paises):
    
    if not paises:
        return {}
    menor = paises[0]
    i = 1
    while i < len(paises):
        if paises[i]["poblacion"] < menor["poblacion"]:
            menor = paises[i]
        i += 1
    return menor

# Devuelve el promedio de población 
def promedio_poblacion(paises):

    if not paises:
        return 0.0
    total = 0
    for p in paises:
        total += p["poblacion"]
    return total / len(paises)

# Devuelve el promedio de superficie
def promedio_superficie(paises):

    if not paises:
        return 0.0
    total = 0
    for p in paises:
        total += p