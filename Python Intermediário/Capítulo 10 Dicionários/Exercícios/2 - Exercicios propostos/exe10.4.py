"""
Enunciado: Escreva um programa que leia e armazene em um dicionário os seguintes dados dos seus contatos:
nome, número celular, email e data de aniversário.

A chave deve o nome. O valor deve ser um dicionário aninhado contendo os demais dados. Se o
nome já existir no dicionário o programa deve perguntar se o usuário deseja alterar o cadastro.

Ao digitar um string vazio para o nome, o programa interrompe a leitura. Antes de encerrar o programa
apresente os dados em um formato de tabela.
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
for nome, dados in d.items(): 
    print(f'{nome:<15} {dados['Telefone']:<15} {dados['Email']:<15} {dados['Aniversário']:<15}')