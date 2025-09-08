while True:
    n = int(input('Digite um numero inteiro ou -1 para parar: '))
    match n:
        case 1:
            print('Você digitou 1')
        case 2:
            print('Você digitou 2')
        case -1:
            break
        case _:
            print('Você digitou outra coisa!')