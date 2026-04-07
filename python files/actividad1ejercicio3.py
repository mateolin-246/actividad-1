def pedir_entero(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            return int(entrada)
        except ValueError:
            print("Ingrese un numero entero valido.")


def generar_fibonacci(inicio, iteraciones):
    a, b = 0, 1
    serie = []

    for _ in range(inicio - 1):
        a, b = b, a + b

    for _ in range(iteraciones):
        serie.append(b)
        a, b = b, a + b

    return serie


def mostrar_resultados(serie):
    print()
    print(f"  Serie generada : {serie}")
    print(f"  Terminos       : {len(serie)}")
    print(f"  Ultimo valor   : {serie[-1]}")
    print()


def main():
    inicio = pedir_entero("Inicio de la serie (posicion): ")
    iteraciones = pedir_entero("Numero de iteraciones: ")

    if iteraciones < 0:
        print("Error: el numero de iteraciones no puede ser negativo.")
        return

    if iteraciones == 0:
        print("No se generaron terminos.")
        return

    serie = generar_fibonacci(inicio, iteraciones)
    mostrar_resultados(serie)


if __name__ == "__main__":
    main()