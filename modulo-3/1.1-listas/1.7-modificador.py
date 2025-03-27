numeros = [1, 30, 21, 2, 9, 64, 35, 78, 11, 90, 3, 4, 5, 6, 7, 8, 9, 10]
quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)
print(quadrado)

# Compreensão de listas
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)
