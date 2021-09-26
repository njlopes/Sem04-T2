def area_e_perimetro(x):
    area = x ** 2
    perimetro = x * 4
    return area, perimetro

x = float(input('Lado do quadrado:'))
a, b = area_e_perimetro(x)
print(f'Área do quadrado igual a: {a:10.4f}')
print(f'Perímetro do quadrado igual a:{b:10.4f}')
