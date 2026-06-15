# MENUS PRINCIPALES 

def menu_filtro():

    print("===== FILTROS =====")
    print("1 - Filtrar por continente")
    print("2 - Filtrar por población")
    print("3 - Filtrar por superficie")
    print("4 - Volver")

    opcion = int(input("Seleccione una opción: "))

    return opcion

def menu_ordenamiento():

    while True:
        try:
            print("\n===== ORDENAMIENTOS =====")
            print("1 - Ordenar por nombre")
            print("2 - Ordenar por población (asc)")
            print("3 - Ordenar por población (desc)")
            print("4 - Ordenar por superficie (asc)")
            print("5 - Ordenar por superficie (desc)")
            print("6 - Volver")

            opcion = int(input("Seleccione una opción: "))

            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Opción fuera de rango")

        except ValueError:
            print("Error: debe ingresar un número")