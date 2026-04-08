class Articulo:
    def __init__(self, nombre, precio, codigo, disponible=True, descripcion="Sin descripcion"):
        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo
        self.disponible = disponible
        self.descripcion = descripcion

    def __str__(self):
        estado = "Disponible" if self.disponible else "Agotado"
        return (
            f"[{self.codigo}] {self.nombre} — ${self.precio:,.0f} — {estado}\n"
            f"  {self.descripcion}"
        )


class Electronico(Articulo):
    def __init__(self, nombre, precio, codigo, marca, garantia_meses, disponible=True, descripcion="Sin descripcion"):
        super().__init__(nombre, precio, codigo, disponible, descripcion)
        self.marca = marca
        self.garantia_meses = garantia_meses

    def __str__(self):
        estado = "Disponible" if self.disponible else "Agotado"
        return (
            f"[{self.codigo}] {self.nombre} | {self.marca} — ${self.precio:,.0f} — {estado}\n"
            f"  Garantia: {self.garantia_meses} meses\n"
            f"  {self.descripcion}"
        )


def main():
    a1 = Articulo("Silla de oficina", 350000, "ART-001")
    a2 = Articulo("Escritorio", 520000, "ART-002", disponible=False)
    a3 = Articulo("Lampara de escritorio", 89000, "ART-003", descripcion="Luz LED regulable, 3 niveles de brillo.")

    print("══ ARTÍCULOS ══\n")
    print(a1)
    print()
    print(a2)
    print()
    print(a3)

    e1 = Electronico("Laptop", 3200000, "ELE-001", "Lenovo", 12, descripcion="Core i5, 16GB RAM, 512GB SSD.")
    e2 = Electronico("Monitor 27'", 1150000, "ELE-002", "Samsung", 6, disponible=False, descripcion="Panel IPS, resolución 2K.")
    e3 = Electronico("Teclado mecánico", 280000, "ELE-003", "Redragon", 3, descripcion="Switches rojos, retroiluminado RGB.")

    print("\n══ ELECTRÓNICOS ══\n")
    print(e1)
    print()
    print(e2)
    print()
    print(e3)


if __name__ == "__main__":
    main()