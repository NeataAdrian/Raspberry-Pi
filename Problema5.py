a = []
b = []
prima_linie = list(input().split())
for i in range(len(prima_linie)):
    a.append(int(prima_linie[i]))


a_doua_linie = list(input().split())
for i in range(len(a_doua_linie)):
    b.append(int(a_doua_linie[i]))


Alice = 0
Bob = 0

for i in range(3):
    if a[i] > b[i]:
        Alice = Alice + 1
    elif a[i] <b[i]:
        Bob = Bob + 1

print(Alice, Bob)