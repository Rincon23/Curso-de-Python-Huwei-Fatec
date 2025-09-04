# Variaveis 
nome = 'Enzo'
idade = 21
peso = 80
print(nome,idade,peso)

#Tipos de váriaveis
int 7 -4 0
float 4.5 0.03 -15.2345 7.0
bool True False
str (String) 'olá' '7.5' ''

#para testar o tipo
print(type(n))
n = input('Digite algo ')
print(n.isnumeric())
n.isalpha()
n.isalnum()
n.isupper()
n.islower()

#.format
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2

print('A soma entre {} e {} vale {}'.format(n1,n2,s))

#Aula 7

#Operadores aritiméticos

+ adição
- subtração
* multiplicação
/ divisão
** potência
// divisão inteira
% Resto da divisão

#ordem de precendência

1. ()
2. **
3. * / // %
4. + -

#Print e .format

print('=' *5)
=====

print('Olá', end=' ')
print('Mundo!')
Olá Mundo!

print('Olá\nMundo')
Olá
Mundo!

nome = 'enzo'
print('Prazer em te conhecer {:5}!'.format(nome))
print('Prazer em te conhecer {:>5}!'.format(nome))
print('Prazer em te conhecer {:^5}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))
Prazer em te conhecer enzo                !
Prazer em te conhecer                 enzo!
Prazer em te conhecer         enzo        !
Prazer em te conhecer ========enzo========!

div = 5/3
print('A divisao vale {:.3f}'.format(div))
A divisao vale 1.667

# Aula 8

# math

import math
from math import ceil, floor, trunc, sqrt, factorial

ceil        arredondamento para cima
floor       arredondamen para
trunc       retita a , para frente
pow         potencia
sqrt        raiz quadrada
factorial   fatorial

raiz = math.sqrt

#Random

import random
num = random.random()
print(num)
numero aleatório de 0 a 1

n2 = random.randint(1,10)
print('numero de 1 a 10: {}'.format(n2))


from random import choice

nome = choice(['Enzo','Jão'])
print('O escolhido foi', nome)


from random import sample

ordem = sample(['Enzo','Jão','Gau'], k=3)

print('A ordem de apresentação é:', ordem)
['Enzo', 'Gau', 'Jão']

#Aula 9

#Fatiamento

frase = 'Curso em video Python'
print(frase[9])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

v
video Python
vdoPto
Curso
Python
vePh

#Análise

frase = 'Curso em video Python'

print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,13)) #com fatiamento
print(frase.find('deo')) #mostra a posição em que começou
print(frase.find('Java'))
print('Curso' in frase)

21
3
1
11
-1
True

#Transformação

frase = 'Curso em video Python'

print(frase.replace('Python', 'Java'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

Curso em video Java
CURSO EM VIDEO PYTHON
curso em video python
Curso em video python
Curso Em Video Python

frase2 = '   Aprenda Python  '

print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

Aprenda Python
   Aprenda Python
Aprenda Python


#Divisão e junção

frase = 'Curso em video Python'
print(frase.split())
['Curso', 'em', 'video', 'Python']

frase = 'Curso em video Python'
print(frase.split())
print(frase.split()[0])
print(frase.split()[0][1]) #1° palavra 2° letra 
['Curso', 'em', 'video', 'Python']
Curso
u

frasejunta = frase.split()
print('-'.join(frasejunta))
Curso-em-video-Python

#print

print("""Olá
Mundo,
Tudo
Bem?""")

Olá 
Mundo, 
Tudo 
Bem?

#Aula 10

#if else

tempo = int(input('Quantos anos tem seu carro? '))

if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('---Fim---')

nome = str(input('Qual é seu nome? '))
if nome == 'Enzo':
    print('Você está escrevendo o código')
else:
    print('Olá {}'.format(nome))

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1+n2)/2
if m >= 6:
    print('Aprovado!')
else:
    print('Reprovado!')

#Simplificado

tempo = int(input('Quantos anos tem seu carro? '))
print('Carro novo' if tempo <= 3 else 'Carro velho')
print('---Fim---')

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1+n2)/2
print('Aprovado' if m >= 6 else 'Reprovado')

#Aula 11

#Cores no terminal

#\033[ style ; text ; back m

Style
0 none
1 bold (negrito)
4 underline (sublinhar)
7 negative

text
30 branco
31 vermelho
32 verde
33 amarelo
34 azul
35 magenta
36 ciano
37 cinza

back
40 branco
41 vermelho
42 verde
43 amarelo
44 azul
45 magenta
46 ciano
47 cinza

nome = 'Enzo'
cores = {'limpa':'\033[m',
            'azul':'\033[34m', 
            'amarelo':'\033[33m', 
            'pretoebranco':'\033[7;30m'}
print('Olá {}{}{}'.format('\033[34m',nome,'\033[m'))

print('Olá {}{}{}'.format(cores['pretoebranco'],nome,cores['limpa']))

#Aula 12

#elif

nome = input('Qual é seu nome? ')
if nome == 'enzo':
    print('mesmo nome do desenvolvedor!')
elif nome == 'gustavo':
    print('ganabara?')
elif nome in 'joâo pedro jose maria':
    print('Nome popular detectado!')
else:
    print('Olá {}!'.format(nome))


#Aula 13

#for

for i in range(0,3):
    print('oi')
print('fim')

oi
oi
oi
fim

for i in range(0,5):
    print(i)

0
1
2
3
4

for i in range(1,6):
    print(i)

1
2
3
4
5


for i in range(0,11,2):
    print(i)

0
2
4
6
8
10

for i in range(5,0, -1):
    print(i)

5
4
3
2
1

# For com variaveis
i = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))

for i in range(i,f,p):
    print(i)

# For com calculo
n = 0
for i in range(0,5):
    n = int(input('Qual numero quer somar: ')) + n
print('O resultado da soma é:',n)


# Biblioteca time 
import time

print("Iniciando...")
time.sleep(5)  # espera 5 segundos
print("Agora o programa continuou!")

from time import sleep

for i in range(10,-1,-1):
    print(i)
    sleep(1)

#Aula 14

#while
c = 1
while c<=10:
    print(c)
    c += 1 
print('fim')


n = 1
while n != 0:
    n = int(input('Digite: '))
print('Fim')


par = impar = 0
n = 1
while n != 0:
    n = int(input('Digite um numero: '))
    if n != 0:
        if n%2 == 0:
            par += 1
        else:
            impar += 1
print('Foram contados\nPares: {}\nImpares {}'.format(par,impar))

#Aula 15

# While true break

cont = 1
while True:
    print('-', end='')
    cont += 1
    if cont == 10:
        break