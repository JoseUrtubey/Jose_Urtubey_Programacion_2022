while True:
    try:
        n1 = int(input("Ingrese un numero: "))
        n2 = int(input("Ingrese otro numero: "))
        suma = n1/n2
        print("La dicision es: ", suma)
    except ZeroDivisionError:
        print("Error, no se puede dividir por cero")
    except ValueError:
        print("Error, ingrese un numero")

    x = input("Desea continuar? (S/N): ")
    if x == "N":
        break