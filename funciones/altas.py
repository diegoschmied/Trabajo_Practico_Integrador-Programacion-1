# AGREGAR PAIS Y ACTUALIZAR DATOS DE UN PAIS
from funciones.archivo import guardar_paises
from funciones.validaciones import *

# Permite agregar paises al csv mediante diccionarios añadiendolos a la lista paises 
# y con la función guardar_paises() con la lista de paises como parámetro
def agregar_pais(paises):

        print("Agregue un nuevo país")
        print("---------------------")

        nombre = input("< Ingrese el nombre del país: ").capitalize()
        nombre = validacion_letras(nombre)


        for pais in paises:
                if pais['nombre'] == nombre:
                        print(f"{nombre} ya está ingresado")
                        return

        poblacion = input("< Ingrese la cantidad de habitantes del país: ")
        poblacion = validacion_numeros(poblacion)

        superficie = input("< Ingrese la superficie del país: ")
        superficie = validacion_numeros(superficie)

        continente = input("< Ingrese a qué continente pertenece el país: ")
        continente = validacion_letras(continente)

        nuevo_pais = {
                "nombre": nombre.capitalize(),
                "poblacion": poblacion,
                "superficie": superficie,
                "continente": continente.capitalize()
        }

        paises.append(nuevo_pais)

        guardar_paises(paises)


# Actualiza los datos de población y superficie del país elegido
def actualizar_pais(paises):

        nombre = input("< Ingrese el nombre del país a actualizar: ").capitalize()
        nombre = validacion_letras(nombre)

        for pais in paises:

                if pais["nombre"] == nombre.capitalize():

                        nueva_poblacion = input("< Ingrese la nueva población: ")
                        nueva_poblacion = validacion_numeros(nueva_poblacion)

                        nueva_superficie = input("< Ingrese la nueva superficie: ")
                        nueva_superficie = validacion_numeros(nueva_superficie)

                        pais["poblacion"] = nueva_poblacion
                        pais["superficie"] = nueva_superficie

                        guardar_paises(paises)

                        return
        
        print("No se encontró el país")