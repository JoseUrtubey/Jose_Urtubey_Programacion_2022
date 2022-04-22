class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = int(lado1)
        self.lado2 = int(lado2)
        self.lado3 = int(lado3)
        self.Lista = [lado1, lado2, lado3]

    def lado_mayor(self):
        print("el lado mayor es:", (max(self.Lista)))

    def equilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("el triangulo es equilatero")

        else:
            print("el triangulo no es equilatero")


lado1 = input("ingrese el largo del lado 1 del triangulo")
lado2 = input("ingrese el largo del lado 2 del triangulo")
lado3 = input("ingrese el largo del lado 3 del triangulo")


T1 = Triangulo(lado1, lado2, lado3)
T1.lado_mayor()
T1.equilatero()
