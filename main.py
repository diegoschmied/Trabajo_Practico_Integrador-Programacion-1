# IMPORTO FUNCIONES
from funciones.altas import *
from funciones.archivo import *
from funciones.busqueda import buscar_pais
from funciones.filtros import ejecutar_filtros
from funciones.estadisticas import mostrar_estadisticas
from funciones.ordenamientos import ejecutar_ordenamientos
from funciones.menus import menu_principal

paises = cargar_paises()


opcion = 0

while True:
    try: 
        
        opcion = menu_principal()

        if opcion == 1:
            agregar_pais(paises)

        elif opcion == 2:
            actualizar_pais(paises)

        elif opcion == 3:
            buscar_pais(paises)

        elif opcion == 4:
            ejecutar_filtros(paises)

        elif opcion == 5:
            paises = ejecutar_ordenamientos(paises)

        elif opcion == 6:
            mostrar_estadisticas(paises)

        elif opcion == 7:   
            print("\n< Saliendo del sistema...\n")
            break

        else:
            raise ValueError("La opción ingresada está fuera de rango (debe ser entre 1 y 7)")

    except ValueError as e:
        print(f"ERROR: {e}")