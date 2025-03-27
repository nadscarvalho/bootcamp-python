numeros = [1, 30, 21, 2, 9, 64, 35, 78, 11, 90, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

# Compreensão de listas
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)