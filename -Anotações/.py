#Tipos de váriaveis

complex 3.4j #(Numero imaginario ou numeros complexos)
None <class 'NoneType'>

#len
 
d = len('exemplo')
print(d)

7

#IDs
obj1 = 10
obj2 = 10
obj3 = 10.0

print(id(obj1))
print(id(obj2))
print(id(obj3))

140731493283016
140731493283016
2493216108976


L = [44,17,26,35,20]
print(type(L))
print(L)
print(len(L))
print(id(L))
print(L[0])
L[0] = 12
print(id(L))

<class 'list'>
[44, 17, 26, 35, 20]
5
2106021666816
44
2106021666816

#Incrementando

a = 10
a += 1
a *=2
a //= 2
print(a)

11

#print

x = 1
y = 2
print('numero x = {1} e y = {0}'.format(y, x))
print(x,y,sep=' <--> ')
print('Olá\ntabulação\tseria isso')

numero x = 1 e y = 2
1 <--> 2
Olá
tabulação       seria isso


a = 14
b = 32
s1 = 'Valores A é {} e B é {}'.format(a,b)
s2 = f'Valores A é {a} e B é {b}'
print(s1)
print(s2)

Valores A é 14 e B é 32
Valores A é 14 e B é 32

#Operadores lógicos

#Em ordem da algebra booleana

not
and
or

a = 0

if not a > 0:
    print('True')
else:
    print('False')


if True or False and False:
    print('True')
else:
    print('False')

True

if (True or False) and False:
    print('True')
else:
    print('False')

False