# RELACIONADO CON EL CSV
import csv 

# Pasa el csv a un diccionario y lo guarda en la lista
def cargar_paises():
    paises = []

    try:

        with open("datos/archivo_paises.csv", "r", encoding="utf-8") as archivo:
            # Lee filas de texto y las convierte directamente en diccionarios
            lector = csv.DictReader(archivo)

            for fila in lector:

                try:
                    
                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]
                    }

                    paises.append(pais)

                except (ValueError, KeyError):

                    print(  "-----------------------------------------------------------\n"
                            "ERROR CSV\n"
                            "Se encontró una fila con formato incorrecto y será ignorada\n"
                            "-----------------------------------------------------------")

    except FileNotFoundError:
        print(  "-------------------------------\n"
                "ERROR CSV\n"
                "No se encontró el archivo CSV\n"
                "-------------------------------")

    return paises

# Guarda la lista de paises en el csv
def guardar_paises(paises):

    # Verificar que la lista no esté vacía
    if not paises:
        print("No hay países para guardar.")
        return

    # Campos del archivo csv
    campos = ["nombre", "poblacion", "superficie", "continente"]

    # Verificar que cada país tenga las claves necesarias
    for pais in paises:

        for campo in campos:
            # Evita sobrescribir el CSV con una lista vacía.
            if campo not in pais:

                print(f"Error: falta la clave '{campo}' en uno de los países.")
                return

    try:

        with open("datos/archivo_paises.csv", "w", newline="", encoding="utf-8") as archivo:

            # Campos del archivo csv
            campos = ["nombre", "poblacion", "superficie", "continente"]

            # Permite escribir datos directamente desde diccionarios a un archivo. 
            # Mapea automáticamente las claves del diccionario a las columnas correspondientes del archivo
            escritor = csv.DictWriter(archivo, fieldnames=campos)

            escritor.writeheader()

            escritor.writerows(paises)

            print(  "-----------------------------\n"
                    "¡País guardado correctamente!\n" 
                    "-----------------------------")

    except PermissionError:
        print(  "--------------------------------------------------------\n"
                "ERROR CSV\n"
                "El archivo CSV está siendo utilizado por otro programa\n"
                "--------------------------------------------------------")
        
    except OSError:
        print(  "-----------------------------\n"
                "ERROR CSV\n"
                "Error al guardar el archivo\n"
                "-----------------------------")