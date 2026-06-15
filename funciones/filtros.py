# FILTRAR PAISES
from funciones.menus import menu_filtro
from funciones.validaciones import *

def filtrar_continente(paises):
    encontrado = False

    continente_filtro = input("< Ingrese el continente a filtrar: ").lower()

    continente_filtro = validacion_letras(continente_filtro)

    for pais in paises:
        if continente_filtro in pais["continente"].lower():

            encontrado = True

            print(f"\nPais: {pais["nombre"]} | Población: {pais["poblacion"]} Habitantes | Superficie: {pais["superficie"]} km² | Continente: {pais["continente"]}")

    if not encontrado:
        print("No hay coincidencias")


def filtrar_poblacion(paises):
    encontrado = False

    poblacion_rango_minimo = input("< Ingrese el rango mínimo: ")
    poblacion_rango_minimo = validacion_numeros(poblacion_rango_minimo)

    poblacion_rango_maximo = input("< Ingrese el rango máximo: ")
    poblacion_rango_maximo = validacion_numeros(poblacion_rango_maximo)


    for poblacion in paises:
        if  poblacion["poblacion"] >= poblacion_rango_minimo and  poblacion["poblacion"] <= poblacion_rango_maximo:

            encontrado = True

            print(f"\nPais: {poblacion['nombre']} | Población: {poblacion['poblacion']} Habitantes | Superficie: {poblacion['superficie']} km² | Continente: {poblacion['continente']}")

    if not encontrado:

        print("No hay coincidencias")


def filtrar_superficie(paises):
    encontrado = False

    superficie_rango_minimo = input("< Ingrese el rango mínimo: ")
    superficie_rango_minimo = validacion_numeros(superficie_rango_minimo)

    superficie_rango_maximo = input("< Ingrese el rango máximo: ")
    superficie_rango_maximo = validacion_numeros(superficie_rango_maximo)


    for superficie in paises:
        if  superficie["superficie"] >= superficie_rango_minimo and  superficie["superficie"] <= superficie_rango_maximo:

            encontrado = True

            print(f"\nPais: {superficie["nombre"]} | Población: {superficie["poblacion"]} Habitantes | Superficie: {superficie["superficie"]} km² | Continente: {superficie["continente"]}")

    if not encontrado:

        print("No hay coincidencias")




def ejecutar_filtros(paises):

    while True:

        opcion = menu_filtro()

        if opcion == 1:
            filtrar_continente(paises)

        elif opcion == 2:
            filtrar_poblacion(paises)

        elif opcion == 3:
            filtrar_superficie(paises)

        elif opcion == 4:
            break

        else:
            print("Opción inválida")