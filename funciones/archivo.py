# RELACIONADO CON EL CSV
import csv 

# Pasa el csv a un diccionario y lo guarda en la lista
def cargar_paises():
    paises = []

    with open("datos/paisesprueba.csv", "r", encoding="utf-8") as archivo:
        # Lee filas de texto y las convierte directamente en diccionarios
        lector = csv.DictReader(archivo)

        for fila in lector:
            pais = {
                "nombre": fila["nombre"],
                "poblacion": int(fila["poblacion"]),
                "superficie": int(fila["superficie"]),
                "continente": fila["continente"]
            }

            paises.append(pais)

    return paises

# Guarda la lista de paises en el csv
def guardar_paises(paises):

    with open("datos/paisesprueba.csv", "w", newline="", encoding="utf-8") as archivo:

        # Campos del archivo csv
        campos = ["nombre", "poblacion", "superficie", "continente"]

        # Permite escribir datos directamente desde diccionarios a un archivo. 
        # Mapea automáticamente las claves del diccionario a las columnas correspondientes del archivo
        escritor = csv.DictWriter(archivo, fieldnames=campos)

        escritor.writeheader()

        escritor.writerows(paises)


# Muestra todos los paises juntos
def mostrar_todos_los_paises(paises):
        for linea in paises:
            linea_limpia = linea.strip()
            nombre, poblacion, superficie, continente = linea_limpia.split(",")
            print(f"Pais: {nombre} | Población: {poblacion} Habitantes | Superficie: {superficie} km² | Continente: {continente}\n")