DOMINIOS_VALIDOS = [".com", ".edu.co"]


def pedir_nombre():
    while True:
        nombre = input("Nombre: ").strip()
        if len(nombre) < 3:
            print("El nombre debe tener al menos 3 caracteres.")
            continue
        return nombre


def pedir_edad():
    while True:
        entrada = input("Edad: ").strip()
        try:
            edad = int(entrada)
        except ValueError:
            print("Ingrese un numero entero.")
            continue
        if not (0 <= edad <= 120):
            print("La edad debe estar entre 0 y 120.")
            continue
        return edad


def correo_valido(correo):
    if "@" not in correo:
        return False
    return any(correo.endswith(dominio) for dominio in DOMINIOS_VALIDOS)


def pedir_correo():
    while True:
        correo = input("Correo: ").strip()
        if correo_valido(correo):
            return correo
        print("El correo debe contener '@' y terminar en .com o .edu.co.")


def registrar_persona():
    print()
    nombre = pedir_nombre()
    edad = pedir_edad()
    correo = pedir_correo()
    return {"nombre": nombre, "edad": edad, "correo": correo}


def mostrar_lista(personas):
    print()
    if not personas:
        print("No hay personas registradas.")
        return
    for i, p in enumerate(personas, 1):
        print(f"  {i}. {p['nombre']} | {p['edad']} años | {p['correo']}")
    print()


def main():
    personas = []

    while True:
        print("\n  1. Registrar persona")
        print("  2. Ver lista")
        print("  0. Salir")
        opcion = input("\n  Opcion: ").strip()

        if opcion == "1":
            persona = registrar_persona()
            personas.append(persona)
            print(f"  '{persona['nombre']}' registrado correctamente.")
        elif opcion == "2":
            mostrar_lista(personas)
        elif opcion == "0":
            break
        else:
            print("  Opcion no valida.")


if __name__ == "__main__":
    main()