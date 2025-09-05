"""
Enunciado: Escreva um programa que leia um número inteiro N. Em seguida leia N números reais carregandoos em uma lista. 
Ao final exiba os elementos da lista na tela, sendo um em cada linha
"""

N = int(input('Digite a quantidade: '))
L = []
for i in range(N):
 X = float(input(f' elemento {i}: '))
 L.append(X)
print('\nResultado:')
for valor in L:
 print(f' {valor}')
print('Fim do Programa')