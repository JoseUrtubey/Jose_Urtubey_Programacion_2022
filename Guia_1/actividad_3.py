anchura = int(input("Anchura del rectángulo: "))
altura = int(input("Altura del rectángulo: "))
dibujo = str(input("ingrese el caracter con el cual hacer el dibujo:"))

for i in range(altura):
    for j in range(anchura):
        print(dibujo, end="")
    print()