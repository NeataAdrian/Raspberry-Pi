#Afisati caracterele mici, mari si cifrele dintr-un sir de caractere introdus de la tastatura.

sir = input("Introduceti caractere:")
LitereMici = []
LitereMari = []
Cifre = []
for i in range(len(sir)):
    if sir[i].islower():
        LitereMici.append(sir[i])
    if sir[i].isupper():
        LitereMari.append(sir[i])
    if sir[i].isdigit():
        Cifre.append(sir[i])

print("Litere mici:", ''.join(LitereMici), "\n")
print("Litere mari:", ''.join(LitereMari), "\n")
print("Cifre:", ''.join(Cifre))