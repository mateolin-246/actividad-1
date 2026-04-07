def pedir_valor():
    while True:
        entrada = input("Ingrese el valor base: ")
        try:
            valor = float(entrada)
            if valor < 0:
                print("El valor no puede ser negativo, intente de nuevo.")
                continue
            return valor
        except ValueError:
            print("Entrada invalida, ingrese un numero.")


def calcular_impuesto(base):
    return base * 0.19


def calcular_descuento(base):
    if base >= 200000:
        return base * 0.10
    return 0.0


def calcular_total(base, impuesto, descuento):
    return base + impuesto - descuento


def mostrar_resumen(base, impuesto, descuento, total):
    print()
    print(f"  Valor base  : ${base:>12,.2f}")
    print(f"  Impuesto 19%: ${impuesto:>12,.2f}")
    print(f"  Descuento   : ${descuento:>12,.2f}")
    print(f"  {'─' * 28}")
    print(f"  Total final : ${total:>12,.2f}")
    print()


def main():
    base = pedir_valor()
    impuesto = calcular_impuesto(base)
    descuento = calcular_descuento(base)
    total = calcular_total(base, impuesto, descuento)
    mostrar_resumen(base, impuesto, descuento, total)


if __name__ == "__main__":
    main()