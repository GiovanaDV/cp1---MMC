'''
1. Division by zero is undefined!
- divisao por 0 é indefinida


print("Division by zero is undefined! --------------------------- \n")
num = 2
den = 0

fracao = num / den
print(fracao)
print("\n")
'''

'''
2. Potenciação de numeros negativos
- a ordem das operacoes determina que a potenciacao deve ser feita antes do sinal de menos
'''

print("Potenciação de numeros negativos --------------------------- \n")
pot_parenteses = (-3)**(2)
pot_sem = -3**(2)

print(f"Potenciação com num entre parenteses: {pot_parenteses} \nSem parenteses: {pot_sem} \n")


'''
3. Potencia de potencia
- quando elevamos uma potencia a outra potencia devemos mult os expoentes, nao somar
'''

print("Potencia de potencia --------------------------- \n")
base = 2
expoente1 = 3
expoente2 = 4

soma = 3 + 4
resultado_soma = 2**(soma)

mult = 3 * 4
resultado_mult = 2**(mult)

potencia = ((2**(3))**4)

print(f"Potencia somando os expoentes: {resultado_soma}, potencia multiplicando os expoentes: {resultado_mult} | Resultado correto: {potencia}")




