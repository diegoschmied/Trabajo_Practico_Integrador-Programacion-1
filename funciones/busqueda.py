# BUSCAR PAIS
from funciones.validaciones import validacion_letras

def buscar_pais(paises):

    encontrado = False

    pais_busqueda = input("< Ingrese el país a buscar: ").lower()

    pais_busqueda = validacion_letras(pais_busqueda)

    for pais in paises:
        if pais_busqueda in pais["nombre"].lower():

            encontrado = True

            print(f"\nPais: {pais["nombre"]} | Población: {pais["poblacion"]} Habitantes | Superficie: {pais["superficie"]} km² | Continente: {pais["continente"]}")

    if not encontrado:

        print("No hay coincidencias")