#Afisati suma primelor n numere prime.

n = int(input("Introduceti numarul de numere prime:"))

s = 0

for i in range(n):
    nrr = 0

    for d in range (2,(i//2)):
        if i % d == 0:
            nrr =+ 1

    if nrr == 0:
        s = s + i

print("Suma primelor n numere prime este:", s)