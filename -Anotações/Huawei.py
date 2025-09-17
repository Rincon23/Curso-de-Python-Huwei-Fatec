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

#Continue

i = 0

while i < 5:
    i= i + 1
    if i == 4:
        continue
    print(i, end='  ')

1  2  3  5

#while else

x = 1

while x > 0 :
    x = int(input('Digite o valor: '))
    if x == 0:
        print('Você digitou 0')
        break
    print(f'O X está valendo {x}')
else:
    print('O usuario digitou um numero negativo')

#try except

a = int(input('Digite A: '))
b = int(input('Digite B: '))

try:
    r = a/b
    print(r)
except:
    print('Não é possivel calcular a divisão!')



try:
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    r = a/b
    print(r)
    
except ZeroDivisionError:
    print('Não é possivel calcular a divisão por zero!')
except ValueError:
    print('Só pode ser digitado numeros inteiros para a e b!')
except:
    print('Não é possivel calcular a divisão!')

#Lista

l = [36, 25, 21, 48, 17, 9, 16, 23, 29, 31]
i=0
while i < len(l):
    print(l[i], end=' ')
    i += 1

36 25 21 48 17 9 16 23 29 31

l = [36, 25, 21, 48, 17, 9, 16, 23, 29, 31]
print(l[-1],l[-2])

31 29

#Fatiamento

l = [36, 25, 21, 48, 17, 9, 16, 23, 29, 31]
origem = l
destino = origem[3:6]
destino2 = origem[1:7:2]
destino3 = origem[:4]
destino4 = origem[6:]

print(destino)
print(destino2)
print(destino3)
print(destino4)

[48, 17, 9]
[25, 48, 9]
[36, 25, 21, 48]
[16, 23, 29, 31]

#append

l = []
l.append(81)
l.append(17)
l.append(49)
l.append(53)
print(l)

[81, 17, 49, 53]

#clear
l = [81,17,49,53]
l.clear()
print(l)

[]

#copy

l = [81,17,49,53]
a = l
b = l.copy()

print(id(l))
print(id(a))
print(id(b))

2637383640256
2637383640256
2637383491584

#Count

l = [81,17,49,53]
print(l.count(81))

1

#extend

l = [81,17,49,53]
l2 = [1,2,3,4]

l.extend(l2)
print(l)

[81, 17, 49, 53, 1, 2, 3, 4]

#index e in 

l = [81,17,49,53]
print(l.index(17))
"""print(l.index(300)) ValueError: 300 is not in list"""
print(300 in l)
print(81 in l)

1
False
True

l = [81,17,49,53,17]
print(l.index(17))
print(l.index(17,2))
print(l.index(17,l.index(17)+1))

1
4
4

#insert
l = [81,17,49,53]
l.insert(1, 195)
l.insert(30,100)
print(l)

[81, 195, 17, 49, 53, 100]

#pop
l = [81,17,49,53]
a = l.pop(0)
print(l)
print(a)
[17, 49, 53]
81

#del e remove
l = [81,17,49,53]
del l[0]
l.remove(53)
"""l.remove(300) ValueError: 300 is not in list"""
print(l)

[17, 49]

#reverse
l = [2,81,195,17,49,81,1,2,3,4,35]
l.reverse()
print(l)

[35, 4, 3, 2, 1, 81, 49, 17, 195, 81, 2]

#sort
l = [2,81,195,17,49,81,1,2,3,4,35]
l.sort()
print(l)

[1, 2, 2, 3, 4, 17, 35, 49, 81, 81, 195]


l = [2,81,195,17,49,81,1,2,3,4,35]
l.sort(reverse=True)
print(l)

[195, 81, 81, 49, 35, 17, 4, 3, 2, 2, 1]


#For em listas
l = [81,17,49,53]

for i in l:
    print(i)

81
17
49
53


l = [81,17,49,53]
pos = 0
for i in l:
    print(f'A posição {pos} contém {i}')
    pos +=1

A posição 0 contém 81
A posição 1 contém 17
A posição 2 contém 49
A posição 3 contém 53


#match case

while True:
    n = int(input('Digite um numero inteiro ou -1 para parar: '))
    match n:
        case 1:
            print('Você digitou 1')
        case 2:
            print('Você digitou 2')
        case -1:
            break
        case _:
            print('Você digitou outra coisa!')


#if inline
x = 10
y = 9
print(x) if x>=y else print(y)

10

#if inline sem o else
cod = [103,117,121,135,161,189,200,204,216]
l = []
for valor in cod:
    #if valor >=120 and valor <= 200:
    #    l.append(valor)
    l.append(valor) if valor >=120 and valor <= 200 else 0
print(l)

[121, 135, 161, 189, 200]

#if inline com retorno de valor
x = int(input('Digite um inteiro: '))
parimpar = 'par' if x % 2 == 0 else 'ímpar'
print(f'O valor {x} é {parimpar}')

#Conjunto set

#Formas de criar

c = set()
c1 = {4,5,6,2}
c2 = set([4,5,6,2])
c3 = set((4,5,6,2))
"""c4 = set(4,9,14,21)""" # Dará erro!
"""c5 = {}""" #Resultara na classe Dict e não set!


c1 = {16,8,21,30,41,28}
print(c1)
{16, 21, 8, 41, 28, 30}

c1 = {16,8,21,30,41,28,8}
print(c1)
{16, 21, 8, 41, 28, 30}

c1 = {16,8,21,30,41,28,'8'}
print(c1)
{16, '8', 21, 8, 41, 28, 30}

c1 = {16,8,21,30,41,28,8.00}
print(c1)
{16, 21, 8, 41, 28, 30}

c1 = {16,8,21,30,41,28,8.00001}
print(c1)
{16, 21, 8.00001, 8, 41, 28, 30}

texto = 'qualquer texto'
c1 = set(texto) 
print(c1)
{'r', 'o', 'e', ' ', 'u', 't', 'a', 'l', 'q', 'x'}

tupla = (26,73,41,26)
c2 = set(tupla)
print(c2)
{73, 26, 41}

lista = [26,73,41,26,41]
c3 = set(lista)
print(c3)
{73, 26, 41}

#hash

v1 = 'Olá'
v2 = 'Olá'
print(hash(v1))
print(hash(v2))

-6753406829026499667
-6753406829026499667

v1 = {207,37.3, (9,10,11),'abcd'}
print(v1)
{'abcd', (9, 10, 11), 37.3, 207}

print(hash(207))
207

print(hash(207.093))
214443399856849103

print(hash((207,10,11)))
1370363275065463132

#Listas não possuem hash pois são mutaveis!
"""print(hash([207,1234]))"""
"""v1 = {207,37.3, (9,10,11),[5,10,15],'abcd'}""" 
#Listas não possuem hash pois são mutaveis!


# Métodos set

#add e clear

c = set()
c.add(85)
c.add(190)
c.add(260)
c.add(89)
c.add('olá')
print(c)
c.clear()
print(c)

{260, 'olá', 85, 89, 190}
set()

#id
c = set()
c2 = c.copy()
print(id(c))
print(id(c2))

1769186092064
1769185805024


c = set()
c2 = c
print(id(c))
print(id(c2))

1769186091616
1769186091616

#difference -
c1 = {26,32,45,58,63}
c2 = {19,34,58,67,82}
c3 = c1.difference(c2)
print(c3)

{32, 26, 45, 63}

c1 = {26,32,45,58,63}
c2 = {19,34,58,67,82}
c1.difference_update(c2)
print(c1)
{32, 26, 45, 63}


#discart
c1 = {26,32,45,58,63}
c1.discard(58)
print(c1)
{32, 58, 26, 45}


#intersection &
c1 = {26,32,45,58,63}
c2 = {19,34,58,67,82}
c3 = c1.intersection(c2)
print(c3)
{58}

c1 = {26,32,45,58,63}
c2 = {19,34,58,67,82}
c1.intersection_update(c2)
print(c1)
{58}


#isdisjoint
c1 = {34,17,50,82,88}
c2 = {34,67,82,19,63}
print(c1.isdisjoint(c2))

False

c1.discard(34)
c1.discard(82)
print(c1.isdisjoint(c2))

True


#issubset e issuperset
c1 = {34,17,50,82,88}
c2 = {34,67,82,19,63}
print(c1.issubset(c2))

False

c1 = {34,82}
c2 = {34,67,82,19,63}
print(c1.issubset(c2))


True

c1 = {34,82}
c2 = {34,67,82,19,63}
print(c2.issuperset(c1))

True


#pop
c1 = {34,17,50,82,88}
v = c1.pop()
print(v) #Remove algum valor
print(c1)

17 
{34, 50, 82, 88}


#remove
c1 = {34,17,50,82,88}
c1.remove(50)
"""c1.remove(999)""" #Erro
print(c1)

{17, 34, 82, 88}

#in
c1 = {34,17,50,82,88}
print(50 in c1)
print(999 in c1)

True
False

#union |
c1 = {34,17,50,82,88}
c2 = {34,67,82,19,63}
u = c1.union(c2)
print(u)

{34, 67, 17, 50, 82, 19, 88, 63}

c1 = {34,17,50,82,88}
c2 = {34,67,82,19,63}
c1.update(c2)
print(c1)

{34, 67, 17, 50, 82, 19, 88, 63}

#symmetric_difference ^
c1 = {34,17,50,82,88}
c2 = {34,67,82,19,63}
s = c1.symmetric_difference(c2)
print(s)

{17, 50, 67, 19, 88, 63}


c1 = {34,17,50,82,88}
c2 = {34,67,82,19,63}
c1.symmetric_difference_update(c2)
print(c1)

{17, 50, 67, 19, 88, 63}

#frozenset #Versão imutavel do conjunto set

c = frozenset()
print(type(c))

<class 'set'>


#Dicionários
uf = {'SP':'São Paulo', 'RJ' : 'Rio de Janeiro', 'MG':'Minas Gerais'}
print(type(uf))
print(uf)

<class 'dict'>
{'SP': 'São Paulo', 'RJ': 'Rio de Janeiro', 'MG': 'Minas Gerais'}


uf = {}
uf['SP'] = 'São Paulo'
uf['RJ'] = 'Rio de Janeiro'
uf['MG'] = 'Minas Gerais'
print(uf)

{'SP': 'São Paulo', 'RJ': 'Rio de Janeiro', 'MG': 'Minas Gerais'}


d = {}
d['a'] = 120
d['a'] = 250
print(d)

{'a': 250}


d['a'] = 250
d['b'] = 521
print(d)

{'a': 250, 'b': 521}


d['a'] = 250
d['b'] = 521
v = d['a'] + d['b']
print(v)

771


d['a'] += 100
print(d)
350


d['a'] = 250
chave = 'a'
print(d[chave])

250

m = {}
m[110] = 45.6
m[4.2] = 'xpt'
m[(1,0,5)] = 28
print(m)

{110: 45.6, 4.2: 'xpt', (1, 0, 5): 28}

#Métodos dos dicionários

len()

d.clear()

d2 = d.copy()

v = d.pop(x)

#get
d = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão'}
print(d.get(120))
print(d[134])

Queijo
Arroz

#fromkeys
d = {}
codigos = (111,139,143,157)
d = d.fromkeys(codigos,'algo')
print(d)

{111: 'algo', 139: 'algo', 143: 'algo', 157: 'algo'}

codigos = (111,139,143,157)
d = {}.fromkeys(codigos,'algo')
print(d)

{111: 'algo', 139: 'algo', 143: 'algo', 157: 'algo'}


#popitem
d = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão'}
v = d.popitem() #Retira sempre o ultimo
print(v)

(133, 'Macarrão')


#setdefault
d = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão'}
d2 = d.setdefault(144,'Feijão')
print(d)
print(d2)

{120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão', 144: 'Feijão'}
Feijão


d = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão'}
d2 = d.setdefault(120, 'Berinjela')

print(d)
print(d2)

{120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão'}
Queijo


#update
d = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão'}
d.update(((117, 'Cebola'), (217, 'Maçã'), (120, 'Tomate')))
print(d)

{120: 'Tomate', 134: 'Arroz', 117: 'Cebola', 125: 'Açucar', 133: 'Macarrão', 217: 'Maçã'}


#keys
d = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão'}
chaves = d.keys()
print(type(chaves))
print(chaves)

<class 'dict_keys'>
dict_keys([120, 134, 117, 125, 133])


for valor in d.keys():
    print(valor)

120
134
117
125
133


#values
d = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão'}
valores = d.values()
print(type(valores))
print(valores)

<class 'dict_values'>
dict_values(['Queijo', 'Arroz', 'Farinha', 'Açucar', 'Macarrão'])


for valor in d.values():
    print(valor)

Queijo
Arroz
Farinha
Açucar
Macarrão


#items
d = {120: 'Queijo', 134: 'Arroz', 117: 'Farinha', 125: 'Açucar', 133: 'Macarrão'}
itens = d.items()
print(type(itens))
print(itens)

<class 'dict_items'>
dict_items([(120, 'Queijo'), (134, 'Arroz'), (117, 'Farinha'), (125, 'Açucar'), (133, 'Macarrão')])


for valor in d.items():
    print(valor)

(120, 'Queijo')
(134, 'Arroz')
(117, 'Farinha')
(125, 'Açucar')
(133, 'Macarrão')


#for em dicionários

#keys
cores = {1: 'Azul', 2: 'Verde', 3: 'Amarelo', 5:'Vermelho'}
for valor in cores.keys():
    print(f'{valor} - {cores[valor]}')

1 - Azul
2 - Verde
3 - Amarelo
5 - Vermelho


cores = {1: 'Azul', 2: 'Verde', 3: 'Amarelo', 5:'Vermelho'}
for valor in cores:
    print(f'{valor} - {cores[valor]}')

1 - Azul
2 - Verde
3 - Amarelo
5 - Vermelho


#values
cores = {1: 'Azul', 2: 'Verde', 3: 'Amarelo', 5:'Vermelho'}

for valor in cores.values():
    print(f'{valor}')

Azul
Verde
Amarelo
Vermelho


#items
cores = {1: 'Azul', 2: 'Verde', 3: 'Amarelo', 5:'Vermelho'}

for valor in cores.items():
    print(f'{valor[0]} - {valor[1]}')

1 - Azul
2 - Verde
3 - Amarelo
5 - Vermelho


cores = {1: 'Azul', 2: 'Verde', 3: 'Amarelo', 5:'Vermelho'}

for num, cor in cores.items():
    print(f'{num} - {cor}')
    
1 - Azul
2 - Verde
3 - Amarelo
5 - Vermelho