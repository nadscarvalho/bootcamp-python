conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)

resultado = conjunto_b.symmetric_difference(conjunto_a)
print(resultado)

resultado = conjunto_a ^ conjunto_b
print(resultado)
