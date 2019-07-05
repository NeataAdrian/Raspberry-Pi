n = int(raw_input())
vector = []

for i in range(n):
    vector.append(float(raw_input()))

a = 0
b = 0

valmax = []
if vector[0] > a and vector[0] > vector [1]:
    valmax.append(vector[0])

for i in range(1, n-1):
    if vector[i] > vector[i-1] and vector[i] > vector[i+1]:
        valmax.append(vector[i])

if vector[-1] > b and vector[-1] > vector[-2]:
    valmax.append(vector[-1])

suma = 0
nr = 0
for i in range(len(valmax)):
    suma = suma + valmax[i]
    nr = nr + 1

medie = float(suma/nr)

nr2 = 0
for i in range(n):
    if vector[i] > medie:
        nr2 = nr2 + 1

print(nr2)