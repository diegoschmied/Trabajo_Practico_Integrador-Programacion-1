# ORDENAR PAIS
from funciones.menus import menu_ordenamiento


# Devuelve el nombre del país (usado para ordenar)
def obtener_nombre(pais):
    return pais["nombre"]


# Devuelve la población del país
def obtener_poblacion(pais):
    return pais["poblacion"]


# Devuelve la superficie del país
def obtener_superficie(pais):
    return pais["superficie"]


# Muestra la lista de países en pantalla
def mostrar_lista(paises):
    for p in paises:
        print(f"{p['nombre']} | {p['poblacion']} | {p['superficie']} | {p['continente']}")


# Función principal de ordenamientos
def ejecutar_ordenamientos(paises):

    if len(paises) == 0:
        print("No hay países cargados")
        return paises

    while True:

        opcion = menu_ordenamiento()

        if opcion == 1:
            paises = sorted(paises, key=obtener_nombre)
            print("\nOrdenados por nombre")
            mostrar_lista(paises)

        elif opcion == 2:
            paises = sorted(paises, key=obtener_poblacion)
            print("\nOrdenados por población (asc)")
            mostrar_lista(paises)

        elif opcion == 3:
            paises = sorted(paises, key=obtener_poblacion, reverse=True)
            print("\nOrdenados por población (desc)")
            mostrar_lista(paises)

        elif opcion == 4:
            paises = sorted(paises, key=obtener_superficie)
            print("\nOrdenados por superficie (asc)")
            mostrar_lista(paises)

        elif opcion == 5:
            paises = sorted(paises, key=obtener_superficie, reverse=True)
            print("\nOrdenados por superficie (desc)")
            mostrar_lista(paises)

        elif opcion == 6:
            return paises

        else:
            print("Opción inválida")