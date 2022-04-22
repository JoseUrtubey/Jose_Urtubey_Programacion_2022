class Calculadora:
    def __init__(self):
        self.n1 = int(input("Ingrese el valor del numero 1: "))
        self.n2 = int(input("Ingrese el valor del numero 2: "))
        self.suma()
        self.resta()
        self.multiplicacion()
        self.division()

    def suma(self):
        ress = self.n1 + self.n2
        print(ress)

    def resta(self):
        resr = self.n1 - self.n2
        print(resr)

    def multiplicacion(self): 
        resm = self.n1 * self.n2
        print(resm)

    def division(self):
        resd = self.n1 / self.n2
        print(resd)


        
N = Calculadora()

