class Persona:
    def __init__(self):
        self.nombre = str(input("ingrese su nombre: "))
        self.edad = int(input("ingrese su edad: "))

    def printeo(self):
        print("nombre: ", self.nombre)
        print("edad: ", self.edad)


class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = int(input("ingrese su sueldo: "))

    def printeo(self):
        super().printeo()
        print("Sueldo ", self.sueldo)

    def paga_impuestos(self):
        if self.sueldo > 3000:
            print("Usted debe pagar impuestos")
        else:
            print("Usted no debe pagar impuestos")


P1 = Persona()
P1.printeo()
E1 = Empleado()
E1.printeo()
E1.paga_impuestos()
