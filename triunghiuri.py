from math import sqrt
n = int(raw_input())
vectorcitire = []
vectorscriere = []
for i in range(n):
    l = [float(x) for x in raw_input().split(" ")]
    vectorcitire.append(l)

dict = {}
nr = 0

for i in vectorcitire:
    a = float(i[0])
    b = float(i[1])
    c = float(i[2])
    if b < a + c and a!=b!=c and a*a!=b*b + c*c:
        p = a + b + c
        s = float(p)/2
        heron = s * (s-a) * (s-b) * (s-c)
        if heron > 0:
            arie = sqrt(heron)
            raport = float(arie/p)
            vectorscriere.append(raport)
            dict[raport] = nr
    nr = nr + 1

print dict[max(vectorscriere)], round(max(vectorscriere), 3)