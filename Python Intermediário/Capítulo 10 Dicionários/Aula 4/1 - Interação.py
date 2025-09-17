d = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão'}

print(d.get(120))
print(d[134])

d = {}
codigos = (111,139,143,157)
d = d.fromkeys(codigos,'algo')

print(d)

codigos = (111,139,143,157)
d = {}.fromkeys(codigos,'algo')
print(d)

{111: 'algo', 139: 'algo', 143: 'algo', 157: 'algo'}


d = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão'}
v = d.popitem()

print(v)

d = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão'}
d2 = d.setdefault(144,'Feijão')

print(d)
print(d2)


d = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão'}
d2 = d.setdefault(120, 'Berinjela')

print(d)
print(d2)

d = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão'}
d.update(((117, 'Cebola'), (217, 'Maçã'), (120, 'Tomate')))
print(d)
