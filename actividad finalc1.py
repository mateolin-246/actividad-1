from abc import ABC, abstractmethod

class Aeronave(ABC):
    def __init__(self, matricula, fabricante, anio_fabricacion):
        self.matricula = matricula
        self.fabricante = fabricante
        self.anio_fabricacion = anio_fabricacion

    @abstractmethod
    def despegar(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class SistemaNavegacion:
    def __init__(self):
        self._ruta_activa = None

    def establecer_ruta(self, origen, destino):
        self._ruta_activa = f"{origen} → {destino}"

    def mostrar_ruta(self):
        if self._ruta_activa:
            print(f"  Ruta activa: {self._ruta_activa}")
        else:
            print("  Sin ruta asignada.")


class SistemaCombustible:
    def __init__(self, capacidad_max):
        self._capacidad_max = capacidad_max
        self._nivel = 0

    def cargar_combustible(self, litros):
        total = self._nivel + litros
        if total > self._capacidad_max:
            print(f"  Capacidad maxima ({self._capacidad_max}L). Solo se cargaron {self._capacidad_max - self._nivel}L.")
            self._nivel = self._capacidad_max
        else:
            self._nivel = total

    def consumir(self, litros):
        if litros > self._nivel:
            print("  Combustible insuficiente para la operacion.")
        else:
            self._nivel -= litros

    def estado_combustible(self):
        porcentaje = (self._nivel / self._capacidad_max) * 100
        print(f"  Combustible: {self._nivel}L / {self._capacidad_max}L ({porcentaje:.1f}%)")



class AviónComercial(Aeronave, SistemaNavegacion, SistemaCombustible):

    ESTADOS_VALIDOS = ["en_tierra", "en_vuelo", "mantenimiento"]

    def __init__(self, matricula, fabricante, anio_fabricacion, modelo, capacidad_pasajeros, capacidad_combustible):
        Aeronave.__init__(self, matricula, fabricante, anio_fabricacion)
        SistemaNavegacion.__init__(self)
        SistemaCombustible.__init__(self, capacidad_combustible)

        self.__modelo = modelo
        self._capacidad_pasajeros = capacidad_pasajeros
        self._estado = "en_tierra"


    @property
    def capacidad_pasajeros(self):
        return self._capacidad_pasajeros

    @capacidad_pasajeros.setter
    def capacidad_pasajeros(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            print("  Error: la capacidad debe ser un entero positivo.")
            return
        if valor > 853:
            print("  Error: ninguna aeronave comercial supera los 853 pasajeros.")
            return
        self._capacidad_pasajeros = valor

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado):
        if nuevo_estado not in self.ESTADOS_VALIDOS:
            print(f"  Estado invalido. Opciones: {self.ESTADOS_VALIDOS}")
            return
        self._estado = nuevo_estado

    def despegar(self):
        if self._estado != "en_tierra":
            print(f"  [{self.matricula}] No puede despegar, estado actual: {self._estado}.")
            return
        if self._nivel == 0:
            print(f"  [{self.matricula}] No puede despegar sin combustible.")
            return
        self._estado = "en_vuelo"
        print(f"  [{self.matricula}] Despegando hacia {self._ruta_activa or 'destino no definido'}.")

    def __str__(self):
        return (
            f"  Matricula  : {self.matricula}\n"
            f"  Modelo     : {self.__modelo}\n"
            f"  Fabricante : {self.fabricante} ({self.anio_fabricacion})\n"
            f"  Pasajeros  : {self._capacidad_pasajeros}\n"
            f"  Estado     : {self._estado}"
        )

def main():
    a1 = AviónComercial("HK-4801", "Boeing", 2015, "737 MAX", 180, 26000)
    a2 = AviónComercial("HK-5523", "Airbus", 2019, "A320neo", 165, 26730)
    a3 = AviónComercial("HK-1390", "Boeing", 2008, "777-200", 396, 171170)

    aeronaves = [a1, a2, a3]

    print("\n════════ FICHA TÉCNICA ════════\n")
    for a in aeronaves:
        print(a)
        print()

    # Preparar y despegar
    print("════════ OPERACIONES ════════\n")
    a1.establecer_ruta("Bogotá", "Medellín")
    a1.cargar_combustible(20000)
    a1.despegar()
    a1.estado_combustible()

    print()

    a2.establecer_ruta("Cali", "Cartagena")
    a2.cargar_combustible(15000)
    a2.despegar()
    a2.mostrar_ruta()

    print()

    a3.establecer_ruta("Barranquilla", "Bucaramanga")
    a3.despegar()

    print("\n════════ ENCAPSULAMIENTO ════════\n")
    print(f"  Capacidad actual de {a1.matricula}: {a1.capacidad_pasajeros} pasajeros")
    a1.capacidad_pasajeros = 200
    print(f"  Capacidad actualizada           : {a1.capacidad_pasajeros} pasajeros")

    print()
    print(f"  Estado actual de {a2.matricula}: {a2.estado}")
    a2.estado = "mantenimiento"
    print(f"  Estado actualizado             : {a2.estado}")

    print()
    print("  Intentando asignar estado invalido:")
    a3.estado = "estrellado"

    print()
    print("  Intentando asignar capacidad invalida (negativa):")
    a1.capacidad_pasajeros = -50


if __name__ == "__main__":
    main()