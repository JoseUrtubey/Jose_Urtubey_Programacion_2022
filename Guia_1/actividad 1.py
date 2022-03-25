mylist = [21, 8, 67, 52,90, 21, 87]
print(mylist)
item = int(input("Ingrese el numero que desea ver la posicion de la lista"))
start=0

index = mylist.index(item, start)

print('The index of', item, 'in the list is:', index)