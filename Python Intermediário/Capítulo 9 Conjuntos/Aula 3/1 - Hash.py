v1 = 'Olá'
v2 = 'Olá'

print(hash(v1))
print(hash(v2))

try:
    v1 = {207,37.3, (9,10,11),[5,10,15],'abcd'}
except TypeError:
    print('listas são mutaveis, por isso não podem pertencer ao conjunto!')

v1 = {207,37.3, (9,10,11),'abcd'}
print(v1)

print(hash(207))

print(hash(207.093))

print(hash((207,10,11)))

try:
    print(hash([207,1234]))
except TypeError:
    print('Listas não tem hash!')


