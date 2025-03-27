numeros = [1, 2, 3, 4, 5]
menor = min(numeros)
print(menor)

linguagens = ["python", "js", "c", "java", "csharp"]
menor = min(linguagens, key=lambda x: len(x))
print(menor)
