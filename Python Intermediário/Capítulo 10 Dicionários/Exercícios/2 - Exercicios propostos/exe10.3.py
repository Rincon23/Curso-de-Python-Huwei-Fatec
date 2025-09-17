"""
Enunciado: Escreva um programa que leia e armazene em um dicionário os seguintes dados dos seus contatos:
nome, número celular, email e data de aniversário.

A chave deve ser o nome. O valor deve ser uma tupla contendo os demais dados. Se o nome já
existir no dicionário o programa deve perguntar se o usuário deseja alterar o cadastro.

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

    d[nome] = (numtel,email,date)

print('{:<15} {:<15} {:<15} {:<15}'.format('nome', 'numtel', 'email', 'date'))
for nome, (numtel,email,date) in d.items(): 
    print(f'{nome:<15} {numtel:<15} {email:<15} {date:<15}')


        