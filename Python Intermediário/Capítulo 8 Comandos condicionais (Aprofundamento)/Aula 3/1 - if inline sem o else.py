cod = [103,117,121,135,161,189,200,204,216]
l = []

for valor in cod:
    #if valor >=120 and valor <= 200:
    #    l.append(valor)
    l.append(valor) if valor >=120 and valor <= 200 else 0
print(l)

