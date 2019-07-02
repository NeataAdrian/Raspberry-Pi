import numpy as np
n = int(input())

linie = list(map(int, input().split()))

matrice = np.array(linie).reshape(n)
print(matrice)