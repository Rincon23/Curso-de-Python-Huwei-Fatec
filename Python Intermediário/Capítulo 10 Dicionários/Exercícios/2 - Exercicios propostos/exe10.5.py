"""
Enunciado: Escreva um programa que leia e armazene em um dicionário os seguintes dados dos seus contatos:
nome, número celular, email e data de aniversário.

A chave deve o nome. O valor pode ser uma tupla ou um dicionário aninhado. Você escolhe.

Ao digitar um string vazio para o nome, o programa interrompe a leitura e apresente todos dados na
tela na mesma formatação dos exercícios anteriores.

Neste exercício os nomes devem estar em ordem alfabética.

Dica

Use a função sorted() de Python.
"""


d = {}

while True:
    nome = input('Digite o nome: ')

    if nome == '':
        break

    if nome in d.keys():
        alterar = input('O nome já existe, deseja alterar o cadastro? [s/n]')
        if alterar != 's':
            continue 
    
    numtel = int(input('Digite o numero de telefone: ')) 
    email = input('Digite o email: ') 
    date = input('Digite a data de aniversário: ') 

    d[nome] = {'Telefone':numtel,'Email':email,'Aniversário':date}

print('{:<15} {:<15} {:<15} {:<15}'.format('nome', 'numtel', 'email', 'date'))

ordem = sorted(d)

for valor in ordem: 
    for nome, dados in d.items(): 
        if valor == nome:
            print(f'{nome:<15} {dados['Telefone']:<15} {dados['Email']:<15} {dados['Aniversário']:<15}')