def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingrese un numero entero valido.")


def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def factorial(n):
    if n < 0:
        return None
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def contar_vocales(texto):
    conteo = {v: 0 for v in "aeiou"}
    for c in texto.lower():
        if c in conteo:
            conteo[c] += 1
    return conteo


def opcion_primo():
    n = pedir_entero("Ingrese un numero: ")
    if es_primo(n):
        print(f"  {n} es primo.")
    else:
        print(f"  {n} no es primo.")


def opcion_factorial():
    n = pedir_entero("Ingrese un numero: ")
    resultado = factorial(n)
    if resultado is None:
        print("  El factorial no esta definido para numeros negativos.")
    else:
        print(f"  {n}! = {resultado}")


def opcion_vocales():
    texto = input("Ingrese un texto: ")
    conteo = contar_vocales(texto)
    print()
    for vocal, cantidad in conteo.items():
        print(f"  '{vocal}' : {cantidad}")


def mostrar_menu():
    print()
    print("  1. Verificar si un numero es primo")
    print("  2. Calcular factorial")
    print("  3. Contar vocales en un texto")
    print("  0. Salir")
    print()


def main():
    opciones = {
        "1": opcion_primo,
        "2": opcion_factorial,
        "3": opcion_vocales,
    }

    while True:
        mostrar_menu()
        opcion = input("  Seleccione una opcion: ").strip()

        if opcion == "0":
            break
        elif opcion in opciones:
            print()
            opciones[opcion]()
        else:
            print("  Opcion no valida, intente de nuevo.")


if __name__ == "__main__":
    main()