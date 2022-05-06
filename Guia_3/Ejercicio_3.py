meses=("enero","febrero","marzo","abril","mayo","junio",
       "julio","agosto","septiembre","octubre","noviembre","diciembre")
try:
    n=int(input("Ingrese un número de mes [1-12]:"))
    if n>0:
        print(meses[n-1])
    else:
        print("En número de mes debe ir entre 1 y 12")
except IndexError:
    print("En número de mes debe ir entre 1 y 12")