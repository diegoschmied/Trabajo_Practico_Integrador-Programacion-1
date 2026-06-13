# IMPORTO FUNCIONES
from funciones.mostrar_resultados import mostrar_resultados


opcion = 0

while opcion != 7:
    try: 
        print("\n<---- MENÚ ---->\n")
        print(" 1 - AGREGAR PAIS")
        print(" 2 - ACTUALIZAR DATOS DE UN PAIS")
        print(" 3 - BUSCAR PAIS")
        print(" 4 - FILTRAR PAISES")
        print(" 5 - ORDENAR PAISES")
        print(" 6 - MOSTRAR ESTADISTICAS")
        print(" 7 - SALIR")
        print(" 8 - PRUEBA CSV")
        print("\n<------------------------->\n")
        opcion = int(input("<<< Seleccione una opción: "))

        if opcion == 8:
            mostrar_resultados()

        elif opcion == 7:   
            print("Saliendo del sistema...")

        else:
            raise ValueError("La opción ingresada está fuera de rango (debe ser entre 1 y 7)")

    except ValueError as e:
        print(f"ERROR: {e}")