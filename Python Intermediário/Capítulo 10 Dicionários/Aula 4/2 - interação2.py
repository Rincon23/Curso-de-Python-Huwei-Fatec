d = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão'}
chaves = d.keys()
print(type(chaves))
print(chaves)

d = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão'}
valores = d.values()
print(type(valores))
print(valores)

d = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão'}
itens = d.items()
print(type(itens))
print(itens)

for valor in d.keys():
    print(valor)

for valor in d.values():
    print(valor)

for valor in d.items():
    print(valor)