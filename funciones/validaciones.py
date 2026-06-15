# VALIDACIONES (LETRAS Y ENTEROS)

def validacion_letras(variable_a_chequear):

    while not variable_a_chequear.isalpha():
        
        print("Error: debe ingresar unicamente letras.")
        
        variable_a_chequear = input("Ingrese nuevamente: ").lower()

    return variable_a_chequear

def validacion_numeros(variable_a_chequear):

    while not variable_a_chequear.isdigit() or int(variable_a_chequear) <= 0:
        
        print("Error: debe ingresar un número mayor que cero.")
        
        variable_a_chequear = input("Ingrese nuevamente: ").lower()

    return int(variable_a_chequear)

def validacion_pais_repetido(nombre_pais, paises):

    while True:

        repetido = False

        for pais in paises:
            if pais["nombre"].lower() == nombre_pais.lower():
                repetido = True
                break

        if not repetido:
            return nombre_pais

        print("Error: ese país ya existe.")

        nombre_pais = input("Ingrese otro país: ")