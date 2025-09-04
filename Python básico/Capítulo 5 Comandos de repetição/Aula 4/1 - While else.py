x = 1

while x > 0 :
    x = int(input('Digite o valor: '))
    if x == 0:
        print('Você digitou 0')
        break
    print(f'O X está valendo {x}')
else:
    print('O usuario digitou um numero negativo')