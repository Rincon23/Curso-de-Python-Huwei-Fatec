"""
Enunciado: Altere a solução do exercício resolvido 10.1 para fazer a iteração com o método .items()

exercício resolvido 10.1:

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

for cod, preco in produtos.items():
    print(f' produto {cod} custa R${preco:7.2f}')
print("\nFim do programa")