import numbers


numero = int(input("Dígame cuantos elementos tiene la lista: "))

if numero < 1:
    print("No se puede hacer una lista asi")
else:
    lista = []
    for i in range(numero):
        print("Dígame el numero", int(i + 1))
        lista.sort(reverse=True)
        number = input()
        lista += [number]
    print("La lista creada es:", lista)