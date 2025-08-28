import numpy as np

'''
1. Associatividade da adição
- u + (v + w) = (u + v) + w
'''

print("Associatividade da adição --------------------------- \n")
# Gerando os valores
u = np.random.randint(0, 10, 3) # 3 valores aleatorios entre 0 e 10
v = np.random.randint(0, 10, 3)
w = np.random.randint(0, 10, 3)

# Calculando os dois lados da igualdade
lado_e = u + (v + w)
lado_d = (u + v) + w

# mostrando resultados
for i in range(len(u)):
    print(f"u={u[i]}, v={v[i]}, w={w[i]} -> Lado esquerdo = {lado_e[i]} | lado direito = {lado_d[i]} | Iguais? {lado_e[i] == lado_d[i]} \n")


'''
2. Comutatividade da adição
- u + v = v + u.
'''

print("Comutatividade da adição --------------------------- \n")
# Gerando os valores
u2 = np.random.randint(0, 10, 3) # 3 valores aleatorios entre 0 e 10
v2 = np.random.randint(0, 10, 3)

# Calculando os dois lados da igualdade
lado_e2 = u2 + v2
lado_d2 = v2 + u2

# mostrando resultados
for i in range(len(u2)):
    print(f"u={u2[i]}, v={v2[i]} -> Lado esquerdo = {lado_e2[i]} | lado direito = {lado_d2[i]} | Iguais? {lado_e2[i] == lado_d2[i]} \n")


'''
3. Elemento identidade da adição
- v + 0 = v
'''

print("Elemento identidade da adição --------------------------- \n")
# Gerando os valores
v3 = np.random.randint(0, 10, 3) # 3 valores aleatorios entre 0 e 10

# Calculando os dois lados da igualdade
lado_e3 = v3 + 0
lado_d3 = v3

# mostrando resultados
for i in range(len(v3)):
    print(f"v={v3[i]} -> Lado esquerdo = {lado_e3[i]} | lado direito = {lado_d3[i]} | Iguais? {lado_e3[i] == lado_d3[i]} \n")


'''
4. Elemento inverso da adição
- v + (−v) = 0.
'''

print("Elemento inverso da adição --------------------------- \n")
# Gerando os valores
v4 = np.array([2, 3, 4]) # 3 valores listados
v4_negativo = np.array([-2, -3, -4])

# Calculando os dois lados da igualdade
lado_e4 = v4 + (v4_negativo)

# mostrando resultados
for i in range(len(v4)):
    print(f"v={v4[i]} -> Lado esquerdo = {lado_e4[i]} | lado direito = 0 | Iguais? {lado_e4[i] == 0} \n")


'''
5. Compatibilidade da mult por escalar com a mult do corpo
- a(bv) = (ab)v
'''

print("Compatibilidade da mult por escalar com a mult do corpo------------ \n")
# Gerando os valores
a = np.random.randint(0, 10, 3) # 3 valores aleatorios entre 0 e 10
b = np.random.randint(0, 10, 3)
v5 = np.random.randint(0, 10, 3)

# Calculando os dois lados da igualdade
lado_e5 = a * (b * v5)
lado_d5 = (a * b) * v5

# mostrando resultados
for i in range(len(a)):
    print(f"a={a[i]}, b={b[i]}, v={v5[i]} -> Lado esquerdo = {lado_e5[i]} | lado direito = {lado_d5[i]} | Iguais? {lado_e5[i] == lado_d5[i]} \n")


'''
6. Elemento identidade da multiplicação por escalar
- 1v = v
'''

print("Elemento identidade da multiplicação por escalar------------ \n")
# Gerando os valores
v6 = np.random.randint(1, 10, 3)

# Calculando os dois lados da igualdade
lado_e6 = 1 * v6
lado_d6 = v6

# mostrando resultados
for i in range(len(v6)):
    print(f"v={v6[i]} -> Lado esquerdo = {lado_e6[i]} | lado direito = {lado_d6[i]} | Iguais? {lado_e6[i] == lado_d6[i]} \n")


'''
7. Distributividade da mult por escalar em relação a adição de vetores 
- a(u + v) = au + av.
'''

print("Distributividade da mult por escalar em relação a adição de vetores ------------ \n")
# Gerando os valores
a7 = np.random.randint(1, 10, 3)
v7 = np.random.randint(1, 10, 3)
u7 = np.random.randint(1, 10, 3)

# Calculando os dois lados da igualdade
lado_e7 = a7 * (u7 + v7)
lado_d7 = a7 * u7 + a7 * v7

# mostrando resultados
for i in range(len(a7)):
    print(f"a={a7[i]}, v={v7[i]}, u={u7[i]} -> Lado esquerdo = {lado_e7[i]} | lado direito = {lado_d7[i]} | Iguais? {lado_e7[i] == lado_d7[i]} \n")


'''
8. Distributividade da mult por escalar em relação a adição do corpo
- (a + b)v = av + bv.
'''

print("Distributividade da mult por escalar em relação a adição do corpo ------------ \n")
# Gerando os valores
a8 = np.random.randint(1, 10, 3)
b8 = np.random.randint(1, 10, 3)
v8 = np.random.randint(1, 10, 3)

# Calculando os dois lados da igualdade
lado_e8 = (a8 + b8) * v8
lado_d8 = a8 * v8 + b8 * v8

# mostrando resultados
for i in range(len(a8)):
    print(f"a={a8[i]}, b={b8[i]}, v={v8[i]} -> Lado esquerdo = {lado_e8[i]} | lado direito = {lado_d8[i]} | Iguais? {lado_e8[i] == lado_d8[i]} \n")




