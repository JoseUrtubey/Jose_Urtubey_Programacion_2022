class Familia:
    def __init__(self, padre, madre, hijos=[]):
        self.padre = padre
        self.madre = madre
        self.hijos = hijos

    def __str__(self):
        cadena = self.padre + "," + self.madre
        for hi in self.hijos:
            cadena = cadena + "," + hi
        return cadena


familia1 = Familia("Carlos", "Sofia", ["Juan", "Julieta"])
familia2 = Familia("Jorge", "Carla")
familia3 = Familia("Federico", "Maria", ["Pedro"])

print(familia1)
print(familia2)
print(familia3)
