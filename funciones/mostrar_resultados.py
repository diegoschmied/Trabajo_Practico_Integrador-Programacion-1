import csv

def mostrar_resultados():
    with open("datos/paisesprueba.csv", "r", encoding="utf-8") as datos_paises:
        for linea in datos_paises:
            linea_limpia = linea.strip()
            nombre, poblacion, superficie, continente = linea_limpia.split(",")
            print(f"Pais: {nombre} | Población: {poblacion} Habitantes | Superficie: {superficie} km²| Continente: {continente}\n")




