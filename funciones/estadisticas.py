# MOSTRAR ESTADISTICAS

def mostrar_estadisticas(paises):

    # Verifica que existan países cargados
    if len(paises) == 0:
        print("No hay países cargados")
        return

    # Variables necesarias para calcular máximos,
    # mínimos, promedios y cantidad por continente
    mayor = paises[0]
    menor = paises[0]

    suma_poblacion = 0
    suma_superficie = 0

    continentes = {}

    # Recorre todos los países realizando
    # los cálculos estadísticos necesarios
    for pais in paises:

        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais

        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    # Calcula los promedios generales
    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)

    # Muestra los resultados obtenidos
    print("\n--- ESTADÍSTICAS ---")

    print(
        f"País con mayor población: "
        f"{mayor['nombre']} ({mayor['poblacion']} habitantes)"
    )

    print(
        f"País con menor población: "
        f"{menor['nombre']} ({menor['poblacion']} habitantes)"
    )

    print(
        f"Promedio de población: "
        f"{promedio_poblacion:.2f}"
    )

    print(
        f"Promedio de superficie: "
        f"{promedio_superficie:.2f} km²"
    )

    print("\nCantidad de países por continente:")

    for continente, cantidad in continentes.items():
        print(f"{continente}: {cantidad}")