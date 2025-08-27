'''
Arithmetic Operations
- propriedade: distributiva da multiplicação em relação à adição
- se vc tem um numero a multiplicando uma soma (b + c), isso é igual a multiplicar a por cada termo separadamente e depois somar
'''

import numpy as np

print("Arithmetic Operations --------------------------- \n")
# Gerando valores int positivos aleatorios para a, b, c
a = np.random.randint(0, 10, 3) # 3 valores aleatorios entre 0 e 10
b = np.random.randint(0, 10, 3)
c = np.random.randint(0, 10, 3)

# Calculando os dois lados da igualdade
lado_e = a*b + a*c # ab + ac
lado_d = a*(b+c) # a(b + c)

# mostrando resultados
for i in range(len(a)):
    print(f"a={a[i]}, b={b[i]}, c={c[i]} -> Lado esquerdo = {lado_e[i]} | lado direito = {lado_d[i]} | Iguais? {lado_e[i] == lado_d[i]} \n")


'''
Exponent Properties 
- quando multiplicamos potências de mesma base (a), somamos os expoentes
'''

print("Exponent Properties --------------------------- \n")
# Escolhendo base a e alguns expoentes n e m
a = 2
n = np.array([1, 2, 3, 4, 5])
m = np.array([3, 4, 5, 6, 7])

# Calculando os dois lados da igualdade
lado_e2 = np.power(a, n) * np.power(a, m) # a^n * a^m
lado_d2 = np.power(a, n+m) # a^(n+m)

# mostrando resultados
for i in range(len(n)):
    print(f"a={a}, n={n[i]}, m={m[i]} -> Lado esquerdo = {lado_e2[i]} | lado direito = {lado_d2[i]} | Iguais? {lado_e2[i] == lado_d2[i]} \n")


'''
Properties of Radicals
- a raiz n-ésima de a é o numero que, elevado a n, resulta em a 
- escrever como potencia funcionaria é so outro modo de representar 
'''

print("Properties of Radicals --------------------------- \n")
# valores para a e n
a = np.array([16, 27, 81, 10, 2], dtype=float)
n = np.array([4,   3,   4,   2,   5])

# calculando os lados
lado_e3 = a**(1/n) # potência fracionária - raiz
lado_d3 = np.power(a, 1/n) # forma de raiz enésima - potencia
# nao existe uma função especifica np.sqrt() para raiz enésima, forma mais eficiente é a potência fracionária

for i in range(len(a)):
    print(f"a={a[i]}, n={n[i]} -> Lado esquerdo = {lado_e3[i]:.4f} | lado direito = {lado_d3[i]:.4f} | Iguais? {np.isclose(lado_e3[i], lado_d3[i])} \n")


'''
Properties of Inequalities
- se a < b entao: se somarmos o mesmo numero c nos dois lados, a desigualdade continua valida
- e, se subtrairmos o mesmo num c nos dois lados, a desigualdade ainda é a mesma 
'''

print("Properties of Inequalities --------------------------- \n")
# valores a, b, c
a = np.array([1, 2, 6])
b = np.array([2, 5, 8])
c = np.array([7, 8, 3])

for i in range(len(a)):
    if a[i] < b[i]:
        print(f"a={a[i]}, b={b[i]}, c={c[i]}")
        print(" a+c < b+c ? ", a[i] + c[i] < b[i] + c[i])
        print(" a-c < b-c ? ", a[i] - c[i] < b[i] - c[i])
        print("\n")


'''
Logarithm Properties
- o logaritmo de 1 em qualquer base b é sempre 0
- logaritmo: operação inversa da exponenciação
'''

# valor de b
b = np.array([10, 6, 8])

# calculo do logaritmo
log = np.log(1) / np.log(b)

#mostrando os valores
for i in range(len(b)):
    print(f"b={b[i]} | log = {log[i]} | resultado é 0? {log[i] == 0}")
