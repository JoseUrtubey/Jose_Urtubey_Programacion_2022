f = open("Ejercicio_5.txt", "a")

try:
    f.write(input("Ingrese algo para agregar al archivo de texto: "))
    print(f.read())
except Exception as e:
    print(e)
    f.close()
