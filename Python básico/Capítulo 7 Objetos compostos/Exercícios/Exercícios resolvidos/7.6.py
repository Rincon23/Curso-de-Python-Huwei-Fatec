"""
Enunciado: Escreva um programa que permaneça em laço lendo números inteiros. O laço termina quando for
digitado 0 (zero). Cada valor diferente de zero digitado deve ser colocado em uma lista, desde que
ele ainda não esteja lá, ou seja, valores repetidos não são aceitos. Se um valor repetido for digitado,
o programa deve exibir uma mensagem na tela.
Ao final exiba a lista e a quantidade de elementos que ela contém.
"""

LstValores = []
valor = int(input('Digite um inteiro: '))
while valor != 0:
    if valor not in LstValores:
        LstValores.append(valor)
    else:
        print(f' erro! o valor {valor} já está na lista')
    valor = int(input('Digite um inteiro: '))
print('\nResultado')
print(LstValores)
print(f'A lista contém {len(LstValores)} elementos')
print('Fim do Programa')
