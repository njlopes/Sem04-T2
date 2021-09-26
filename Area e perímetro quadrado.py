def area_quadrado(lado):
    return f'{lado * lado:10.4f}'
def perimetro_quadrado(lado):
    return f'{lado * 4:10.4f}'

valor_lado = float(input('Lado do quadrado:'))
print('Área do quadrado:', area_quadrado(valor_lado))
print('Perímetro do quadrado:', perimetro_quadrado(valor_lado))
