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