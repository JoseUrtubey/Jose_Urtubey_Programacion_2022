class Calculadora:
    def __init__(self,n1,n2):
        self.n1 = int(n1)
        self.n2 = int(n2)

    def suma(self):
        res = self.n1 + self.n2
        print(res)

    def resta(self):
        res = self.n1 - self.n2
        print(res)

    def multiplicacion(self): 
        res = self.n1 * self.n2
        print(res)

    def division(self):
        res = self.n1 / self.n2
        print(res)

n1 = input("Ingrese el valor del numero 1: ")
n2 = input("Ingrese el valor del numero 2: ")
        
N = Calculadora(n1,n2)

N.suma()
N.resta()
N.multiplicacion()
N.division()
