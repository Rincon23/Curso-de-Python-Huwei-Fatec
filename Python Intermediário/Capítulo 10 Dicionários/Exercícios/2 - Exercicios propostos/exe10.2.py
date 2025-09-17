"""
Enunciado: Escreva um programa que permaneça em laço lendo do teclado números inteiros entre 1 e 9. Outros
valores devem ser ignorados. Esse laço termina quando for digitado zero ou qualquer valor negativo.
O objetivo deste programa é contar quantas vezes cada valor entre 1 e 9 foi digitado.

Ao término do laço de leitura o programa deve mostrar quais valores foram digitados e quantas vezes
cada um. Obrigatoriamente use um dicionário.
"""
d = {}

while True:
    n = int(input('Digite um numero entre 1 - 9: '))

    if n < 1:
        break

    if n>0 and n<10:
        if n in d:
            d[n] += 1 
        else:
            d[n] = 1
    
for num, qtd in d.items():
    print(f'{num} - {qtd}')