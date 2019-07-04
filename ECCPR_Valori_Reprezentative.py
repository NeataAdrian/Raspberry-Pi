lista1 = []
lista2 = []
n = int(raw_input())
for i in range(n):
    lista1.append(int(raw_input()))

m = int(raw_input())
for i in range(m):
    lista2.append(int(raw_input()))

suma = 0
nr = 0

lista3 = []
lista3 = lista1 + lista2
lung = len(lista3)
lista3.sort()
for i in range(lung):
    if nr < (lung - 5):
        suma = suma + int(lista3[lung - i - 1])
        lista3.remove(lista3[lung - i - 1])
        nr = nr + 1

medie = float(suma)/nr
print("{}".format(round(medie, 2)))

