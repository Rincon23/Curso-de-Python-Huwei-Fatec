"""
Enunciado: Escreva um programa para registrar os seguintes dados de uma frota de veículos de uma empresa:

Placa (string - chave - obrigatório todas as letras maiúsculas)

Marca

Modelo

Tipo (caminhão, furgão, automóvel, motocicleta, etc)

Kilometragem

Data da Compra (string no formato AAAAMMDD - ano,mês,dia)

O programa deve ficar em laço enquanto a Placa for digitada. O laço termina quando for digitado FIM
para a placa. Se for digitada uma placa com letras minúsculas o programa deve convertê-las para
maiúsculas com o método .upper().

Para cada veículo leia todos os dados e carregue em um dicionário. Se uma placa já existente for
digitada o programa deve avisar que já existe, mostrar seus dados e se usuário quiser fazer alteração
em algum dado basta digitar o novo valor. Para os campos em que nada for digitado deve ser mantido
o valor já cadastrado.

Ao final do laço mostre os dados na tela com uma formatação legível.

Desafio Inclua no programa uma validação da placa, seguindo as seguintes regras:

a) Deve ter 7 caracteres
b) Os três primeiros devem ser letras
c) Os caracteres 4, 6 e 7 devem ser algarismos
d) O caractere 5 pode ser número (placa antiga) ou letra (nova placa padrão Mercosul)
"""

placas = {}


while True:
    alterando = False

    while True:
        placa = (input('Escreva a placa: ')).upper()

        if placa == 'FIM':
           break

        if len(placa) == 7:
            if placa[0:2].isalpha() == True:
                if placa[3].isnumeric() == True and placa[5].isnumeric() == True and placa[6].isnumeric() == True:
                    break
                else:
                    print('Os caracteres 4, 6 e 7 devem ser algarismos!') 
            else:
                print('Os três primeiros devem ser letras!') 
        else:
            print('Deve ter 7 caracteres!')

    if placa == 'FIM':
           break

    if placa in placas.keys():
        
        print('A placa já existe estão aqui as informações:')
        print('\t{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}'.format('placa','Marca', 'Modelo', 'Tipo', 'Kilometragem','Data'))
        print('\t{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}'.format(placa, placas[placa]['Marca'],placas[placa]['Modelo'], placas[placa]['Tipo'], placas[placa]['Kilometragem'],placas[placa]['Data']))
        
        alterar = (input('Quer alterar aluma informação? [S/N]')).upper()
        if alterar == 'S':
            alterando = True
            placaa = placa
            marcaa = placas[placa]['Marca']
            modeloa = placas[placa]['Modelo']
            tipoa = placas[placa]['Tipo']
            kilometragema = placas[placa]['Kilometragem']
            dataa = placas[placa]['Data']
        else:
            continue
             
    marca = input('Marca: ')
    modelo = input('Modelo: ')
    tipo = input('caminhão, furgão, automóvel, motocicleta? ')
    kilometragem = input('kilometragem: ')
    data = input('Data da Compra: [AAAAMMDD]')

    if alterando == False:
        placas[placa] = {'Marca':marca, 'Modelo':modelo, 'Tipo':tipo, 'Kilometragem':kilometragem, 'Data':data}

    elif alterando == True:
        if marca == '':
            marca = marcaa
        if modelo == '':
            modelo = modeloa
        if tipo == '':
            tipo = tipoa
        if kilometragem == '':
            kilometragem = kilometragema
        if data == '':
            data = dataa
        placas[placa] = {'Marca':marca, 'Modelo':modelo, 'Tipo':tipo, 'Kilometragem':kilometragem, 'Data':data}
 
print('\t{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}'.format('placa','Marca', 'Modelo', 'Tipo', 'Kilometragem','Data'))
for placa, dados in placas.items():
    print('\t{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}'.format(placa, dados['Marca'],dados['Modelo'], dados['Tipo'], dados['Kilometragem'],dados['Data']))