def inveter(numero):
    u = numero % 10
    numero = numero // 10
    d = numero % 10
    numero = numero // 10
    c = numero % 10
    numero = numero // 10
    m = numero % 10
    numero_invertido = (u * 1000) + (d * 100) + (c *10) + m
    return numero_invertido

n = int(input("Digite um número inteiro entre 1000 e 9999:"))
print(f'O inverso de {n} correponde a {inveter(n)}')
