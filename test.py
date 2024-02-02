# Início
x = float(input("Digite o valor de x: "))
y = float(input("Digite o valor de y: "))

z = (x * y) + 5

if z <= 0:
    resposta = 'A'
else:
    if z <= 100:
        resposta = 'B'
    else:
        resposta = 'C'

# Escrever z e resposta
print(f"z = {z}, resposta = {resposta}")
