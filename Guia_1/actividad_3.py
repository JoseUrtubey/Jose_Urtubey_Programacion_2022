print(
    "elija la opcion 1 si quiere dibujar un triangulo o 2 si quiere dibujar un rectangulo"
)
x = int(input("ingrese la opcion: "))

if x == 1:
    n = int(input("ingrese el numero de filas: "))
    char = input("ingrese el caracter: ")

    def draw_triangle(n):
        for i in range(n):
            print(" " * (n - i - 1) + (char + " ") * (i + 1))

    draw_triangle(n)

elif x == 2:
    anchura = int(input("Anchura del rectángulo: "))
    altura = int(input("Altura del rectángulo: "))
    dibujo = str(input("ingrese el caracter con el cual hacer el dibujo:"))

    for i in range(altura):
        for j in range(anchura):
            print(dibujo, end="")
        print()
