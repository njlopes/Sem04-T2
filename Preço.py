def percentual(valor,porcentagem):
    return valor * (porcentagem/100)

pr = float(input('Digite um preço:'))
vr_p = float(input('Digite um desconto percentual:'))
pr_acres = pr + percentual(pr,vr_p)
pr_desc = pr - percentual(pr,vr_p)
print(f'{pr_acres:.2f}')
print(f'{pr_desc:.2f}')
