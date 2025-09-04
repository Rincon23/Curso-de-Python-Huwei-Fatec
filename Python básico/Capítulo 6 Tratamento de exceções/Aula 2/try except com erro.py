try:
    a = int(input('Digite A: '))
    b = int(input('Digite B: '))
    r = a/b
    print(r)
    
except ZeroDivisionError:
    print('Não é possivel calcular a divisão por zero!')
except ValueError:
    print('Só pode ser digitado numeros inteiros para a e b!')
except:
    print('Não é possivel calcular a divisão!')