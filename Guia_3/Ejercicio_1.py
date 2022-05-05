while True:
    try:
        n1 = int(input("Ingrese un numero: "))
        n2 = int(input("Ingrese otro numero: "))
        suma = n1 + n2
        print("La suma es: ", suma)
    except ValueError:
        print("Error, ingrese un numero")

    x = input("Desea continuar? (S/N): ")
    if x == "N":
        break
