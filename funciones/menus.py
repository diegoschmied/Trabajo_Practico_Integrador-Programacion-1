# MENUS PRINCIPALES 
def menu_principal():

    while True:
        try:
            print("\n<===== MENÚ =====>\n")
            print(" 1 - AGREGAR PAIS")
            print(" 2 - ACTUALIZAR DATOS DE UN PAIS")
            print(" 3 - BUSCAR PAIS")
            print(" 4 - FILTRAR PAISES")
            print(" 5 - ORDENAR PAISES")
            print(" 6 - MOSTRAR ESTADISTICAS")
            print(" 7 - SALIR")

            opcion = int(input("Seleccione una opción: "))

            if 1 <= opcion <= 7:
                return opcion
            else:
                print("Opción fuera de rango")
        
        except ValueError:
            print("Error: debe ingresar un número")


def menu_filtro():

    while True:
        try:
            print("\n===== FILTROS =====")
            print("1 - Filtrar por continente")
            print("2 - Filtrar por población")
            print("3 - Filtrar por superficie")
            print("4 - Volver\n")

            opcion = int(input("Seleccione una opción: "))

            if 1 <= opcion <= 4:
                return opcion
            else:
                print("Opción fuera de rango")
        
        except ValueError:
            print("Error: debe ingresar un número")

def menu_ordenamiento():

    while True:
        try:
            print("\n===== ORDENAMIENTOS =====")
            print("1 - Ordenar por nombre")
            print("2 - Ordenar por población (asc)")
            print("3 - Ordenar por población (desc)")
            print("4 - Ordenar por superficie (asc)")
            print("5 - Ordenar por superficie (desc)")
            print("6 - Volver\n")

            opcion = int(input("Seleccione una opción: "))

            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Opción fuera de rango")

        except ValueError:
            print("Error: debe ingresar un número")