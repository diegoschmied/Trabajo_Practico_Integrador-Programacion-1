# AGREGAR PAIS Y ACTUALIZAR DATOS DE UN PAIS
from funciones.archivo import guardar_paises

# Permite agregar paises al csv mediante diccionarios añadiendolos a la lista paises 
# y con la función guardar_paises() con la lista de paises como parámetro
def agregar_pais(paises):
        print("Agregue un nuevo país")
        print("---------------------")
        nombre = input("Ingrese el nombre del país: ")
        poblacion = int(input("Ingrese la cantidad de habitantes del país: "))
        superficie = int(input("Ingrese la superficie del país: "))
        continente = input("Ingrese a qué continente pertenece el país: ")

        nuevo_pais = {
                "nombre": nombre.capitalize(),
                "poblacion": poblacion,
                "superficie": superficie,
                "continente": continente
        }

        paises.append(nuevo_pais)

        guardar_paises(paises)

        print("¡País guardado correctamente!")


# Actualiza los datos de población y de superficie del país elegido
def actualizar_pais(paises):

    nombre = input("Ingrese el nombre del país a actualizar: ").capitalize()

    for pais in paises:

        if pais["nombre"] == nombre:
            nueva_poblacion = int(input("Ingrese la nueva población: "))
            nueva_superficie = int(input("Ingrese la nueva superficie: "))

            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie

            guardar_paises(paises)

            print("¡País actualizado correctamente!")

            return
    
    print("No se encontró el país")