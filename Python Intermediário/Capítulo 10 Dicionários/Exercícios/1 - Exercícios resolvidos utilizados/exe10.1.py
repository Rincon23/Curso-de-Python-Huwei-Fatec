"""Enunciado: Escreva um programa que leia do teclado o código de um produto e seu preço unitário. O código é
um string e o preço é real. Acrescente o par código:preço em um dicionário. O laço termina quando
for fornecido um string vazio para o código. Ao final, exibir código e preço, um produto em cada linha.
"""

produtos = {}
print('Leitura dos dados')
cod = input(' Digite o código: ') # lê o primeiro código
while cod != '': # se cod diferente de vazio segue no laço
 preco = float(input(' Digite o preço: ')) # lê o preço
 produtos[cod] = preco # acrescenta novo item ao dicionário
 cod = input(' Digite o código: ') # lê o próximo cod
print('Fim da leitura dos dados\n')
print('Preço dos Produtos')
for cod in produtos.keys(): # faz iteração como Caso 1 – usando .keys()
 print(f' produto {cod} custa R$ {produtos[cod]:7.2f}')
print("\nFim do programa")
