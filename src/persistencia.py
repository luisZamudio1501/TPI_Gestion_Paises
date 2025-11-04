"""
persistencia.py — Lectura y escritura del CSV de países.
"""
import csv
import os

CAMPOS = ["nombre", "poblacion", "superficie", "continente"]

def _es_entero_no_negativo_txt(s: str) -> bool:
    return s.isdigit()

# Esta función lee los datos del CSV y devuele una lista de dicts (diccionarios) con claves: nombre(str), 
# poblacion(int), superficie(int), continente(srt)
def leer_csv(ruta: str) -> list[dict]:

    paises: list[dict] = []

    if not isinstance(ruta, str):
        return paises

    if not os.path.exists(ruta):
        return paises

    with open(ruta, "r", newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)

        # Se valida que existan todas las columnas requeridas
        if lector.fieldnames is None:
            return paises
        encabezados = [h.strip().lower() for h in lector.fieldnames]
        requeridos = set(CAMPOS)
        presentes = set(encabezados)
        if not requeridos.issubset(presentes):
            return paises
        
        # Obtener textos o vacío si falta la clave
        for fila in lector:
            nombre_txt = (fila.get("nombre") or "").strip()
            continente_txt = (fila.get("continente") or "").strip()
            poblacion_txt = (fila.get("poblacion") or "").strip()
            superficie_txt = (fila.get("superficie") or "").strip()

            # Validaciones
            if not nombre_txt or not continente_txt:
                continue
            if not _es_entero_no_negativo_txt(poblacion_txt):
                continue
            if not _es_entero_no_negativo_txt(superficie_txt):
                continue

            poblacion_val = int(poblacion_txt)
            superficie_val = int(superficie_txt)

            paises.append({
                "nombre": nombre_txt,
                "poblacion": poblacion_val,
                "superficie": superficie_val,
                "continente": continente_txt
            })

    return paises


# Esta función escribe el CSV con los campos definidos en CAMPOS
def guardar_csv(ruta: str, paises: list[dict]) -> None:
    
    if not isinstance(ruta, str):
        return
    if not isinstance(paises, list):
        return

    with open(ruta, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=CAMPOS)
        escritor.writeheader()
        for p in paises:

            # Validaciones 
            nombre = (str(p.get("nombre")) if p.get("nombre") is not None else "").strip()
            continente = (str(p.get("continente")) if p.get("continente") is not None else "").strip()
            poblacion = p.get("poblacion")
            superficie = p.get("superficie")

            if not nombre or not continente:
                continue
            if not isinstance(poblacion, int) or poblacion < 0:
                continue
            if not isinstance(superficie, int) or superficie < 0:
                continue

            escritor.writerow({
                "nombre": nombre,
                "poblacion": int(poblacion),
                "superficie": int(superficie),
                "continente": continente
            })
